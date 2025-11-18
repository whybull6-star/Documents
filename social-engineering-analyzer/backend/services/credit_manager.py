"""
Credit Manager - Handles user credits and billing
In production, this should integrate with smart contracts on Gnosis chain
"""

from typing import Dict, Optional
import os
from web3 import Web3
import json

class CreditManager:
    """
    Manages user credits and billing
    
    ELI5: Like a bank account balance system, but for API usage.
    Each analysis costs credits, users pay in crypto to get credits.
    """
    
    def __init__(self):
        # In production, connect to Gnosis chain
        self.gnosis_rpc = os.getenv("GNOSIS_RPC", "https://rpc.gnosischain.com")
        self.w3 = Web3(Web3.HTTPProvider(self.gnosis_rpc))
        
        # In-memory storage for credits (in production, use database or blockchain)
        # Format: {address: {"balance": int, "tier": str}}
        self._credits_db: Dict[str, Dict] = {}
        
        # Default free tier credits
        self.free_tier_credits = 10
        self.pro_tier_credits = 1000
        self.enterprise_credits = float('inf')
    
    async def check_credits(self, address: str) -> bool:
        """Check if user has credits available"""
        balance = await self.get_balance(address)
        return balance[0] > 0
    
    async def get_balance(self, address: str) -> tuple[int, str]:
        """
        Get credit balance for an address
        
        Returns:
            Tuple of (balance, tier)
        """
        # Normalize address (lowercase)
        address = address.lower()
        
        # Check in-memory DB
        if address not in self._credits_db:
            # First time user - give free tier
            self._credits_db[address] = {
                "balance": self.free_tier_credits,
                "tier": "free"
            }
        
        user_data = self._credits_db[address]
        return user_data["balance"], user_data["tier"]
    
    async def deduct_credits(self, address: str, amount: int = 1):
        """Deduct credits from user account"""
        address = address.lower()
        
        if address not in self._credits_db:
            raise ValueError("User not found")
        
        current_balance = self._credits_db[address]["balance"]
        
        if current_balance < amount:
            raise ValueError("Insufficient credits")
        
        self._credits_db[address]["balance"] = current_balance - amount
    
    async def add_credits(self, address: str, amount: int, tier: str = "pro"):
        """
        Add credits to user account
        In production, verify payment on blockchain first
        """
        address = address.lower()
        
        if address not in self._credits_db:
            self._credits_db[address] = {"balance": 0, "tier": tier}
        
        # Set tier and add credits
        if tier == "pro":
            self._credits_db[address]["balance"] = self.pro_tier_credits
        elif tier == "enterprise":
            self._credits_db[address]["balance"] = self.enterprise_credits
        else:
            self._credits_db[address]["balance"] += amount
        
        self._credits_db[address]["tier"] = tier
    
    async def verify_payment(self, tx_hash: str) -> bool:
        """
        Verify payment transaction on Gnosis chain
        This should check if payment was successful before adding credits
        """
        try:
            receipt = self.w3.eth.get_transaction_receipt(tx_hash)
            return receipt.status == 1  # 1 = success
        except Exception:
            return False


