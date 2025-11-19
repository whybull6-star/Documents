"""
Enhanced Seed Data - Real-world attack patterns for Web3 social engineering
Includes SIM swapping, wallet stalking, address spoofing, and crypto-specific attacks
"""

import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.enhanced_qdrant_service import EnhancedQdrantService

# SIM Swapping Attack Patterns
SIM_SWAPPING_PATTERNS = [
    {
        "id": 1001,
        "text": "We need to verify your identity. Please provide your phone number and the last 4 digits of your SSN to port your number to a new SIM card.",
        "attack_type": "sim_swapping",
        "metadata": {
            "severity": "critical",
            "source": "phone_call",
            "tactic": "identity_verification_request"
        }
    },
    {
        "id": 1002,
        "text": "Your carrier account shows suspicious activity. We need to transfer your phone number to a new SIM card for security. Can you confirm your account PIN?",
        "attack_type": "sim_swapping",
        "metadata": {
            "severity": "critical",
            "source": "phone_call",
            "tactic": "fake_security_alert"
        }
    },
    {
        "id": 1003,
        "text": "Click here to verify your phone number and receive your SMS verification code. This is required to secure your crypto wallet.",
        "attack_type": "sim_swapping",
        "metadata": {
            "severity": "high",
            "source": "phishing_email",
            "tactic": "crypto_wallet_verification"
        }
    },
    {
        "id": 1004,
        "text": "Your two-factor authentication has been disabled. To re-enable, please verify your phone number by clicking this link and entering the code we'll send via SMS.",
        "attack_type": "sim_swapping",
        "metadata": {
            "severity": "high",
            "source": "phishing_email",
            "tactic": "2fa_manipulation"
        }
    },
    {
        "id": 1005,
        "text": "URGENT: Your phone number will be deactivated in 24 hours. Call us immediately at this number to prevent service interruption and verify your account.",
        "attack_type": "sim_swapping",
        "metadata": {
            "severity": "critical",
            "source": "smishing",
            "tactic": "urgency_manipulation"
        }
    }
]

# Wallet Stalking Patterns
WALLET_STALKING_PATTERNS = [
    {
        "id": 2001,
        "text": "I noticed you have a large balance in your wallet. I can help you invest it safely. Send me your wallet address for a free consultation.",
        "attack_type": "wallet_stalking",
        "metadata": {
            "severity": "medium",
            "source": "social_media",
            "tactic": "balance_observation"
        }
    },
    {
        "id": 2002,
        "text": "I've been tracking your transactions. You seem to be doing well. Want to join my exclusive trading group? Just send 0.1 ETH to verify.",
        "attack_type": "wallet_stalking",
        "metadata": {
            "severity": "high",
            "source": "direct_message",
            "tactic": "transaction_monitoring"
        }
    },
    {
        "id": 2003,
        "text": "Your wallet address 0x1234...5678 has been flagged for suspicious activity. Click here to verify your identity and avoid account suspension.",
        "attack_type": "wallet_stalking",
        "metadata": {
            "severity": "high",
            "source": "phishing_email",
            "tactic": "address_exposure"
        }
    },
    {
        "id": 2004,
        "text": "I see you just received a large transaction. Congratulations! I have an investment opportunity that could double your money. Interested?",
        "attack_type": "wallet_stalking",
        "metadata": {
            "severity": "medium",
            "source": "telegram",
            "tactic": "transaction_timing_exploit"
        }
    },
    {
        "id": 2005,
        "text": "Your wallet is being monitored by scammers. Send 0.05 ETH to this address to enable advanced security protection for your funds.",
        "attack_type": "wallet_stalking",
        "metadata": {
            "severity": "critical",
            "source": "direct_message",
            "tactic": "fake_security_service"
        }
    }
]

# Address Spoofing Patterns
ADDRESS_SPOOFING_PATTERNS = [
    {
        "id": 3001,
        "text": "Your wallet address has been compromised. Send all your funds immediately to this secure address: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb (Note: This is a spoofed address, last character changed)",
        "attack_type": "address_spoofing",
        "metadata": {
            "severity": "critical",
            "source": "phishing_email",
            "tactic": "fake_compromise_alert"
        }
    },
    {
        "id": 3002,
        "text": "We need to update your wallet address for security. Please send your funds to the new address: 0x8ba1f109551bD432803012645Hac136c22C9e7c (Similar to your address but different)",
        "attack_type": "address_spoofing",
        "metadata": {
            "severity": "critical",
            "source": "phishing_email",
            "tactic": "fake_address_update"
        }
    },
    {
        "id": 3003,
        "text": "Your transaction failed. Please resend to this corrected address: 0x1234567890123456789012345678901234567890 (Looks similar but is different)",
        "attack_type": "address_spoofing",
        "metadata": {
            "severity": "high",
            "source": "fake_transaction_error",
            "tactic": "transaction_redirect"
        }
    },
    {
        "id": 3004,
        "text": "Airdrop claim: Send 0.01 ETH to 0xABCDEF1234567890ABCDEF1234567890ABCDEF12 to receive 1000 tokens. This address looks legitimate but is actually a scam.",
        "attack_type": "address_spoofing",
        "metadata": {
            "severity": "high",
            "source": "fake_airdrop",
            "tactic": "fake_reward"
        }
    },
    {
        "id": 3005,
        "text": "Your wallet needs verification. Send a small amount (0.001 ETH) to verify address: 0x9876543210987654321098765432109876543210. This is a test transaction.",
        "attack_type": "address_spoofing",
        "metadata": {
            "severity": "medium",
            "source": "fake_verification",
            "tactic": "small_amount_test"
        }
    }
]

# General Phishing Patterns (Crypto-specific)
GENERAL_PHISHING_PATTERNS = [
    {
        "id": 4001,
        "text": "Your MetaMask wallet has been locked due to suspicious activity. Click here to unlock and verify your seed phrase.",
        "attack_type": "general_phishing",
        "metadata": {
            "severity": "critical",
            "source": "phishing_email",
            "tactic": "wallet_lock_scam"
        }
    },
    {
        "id": 4002,
        "text": "Congratulations! You've been selected for our exclusive NFT airdrop. Connect your wallet and claim your free NFT now!",
        "attack_type": "general_phishing",
        "metadata": {
            "severity": "high",
            "source": "social_media",
            "tactic": "fake_airdrop"
        }
    },
    {
        "id": 4003,
        "text": "Your DeFi protocol has been compromised. Withdraw all funds immediately to this secure address before they're lost forever.",
        "attack_type": "general_phishing",
        "metadata": {
            "severity": "critical",
            "source": "fake_protocol_alert",
            "tactic": "fake_emergency"
        }
    },
    {
        "id": 4004,
        "text": "We detected unauthorized access to your crypto exchange account. Click here to secure your account and verify your identity.",
        "attack_type": "general_phishing",
        "metadata": {
            "severity": "high",
            "source": "phishing_email",
            "tactic": "fake_breach_alert"
        }
    },
    {
        "id": 4005,
        "text": "Your wallet needs to be upgraded to support the latest security features. Download this update and enter your private key to complete the upgrade.",
        "attack_type": "general_phishing",
        "metadata": {
            "severity": "critical",
            "source": "fake_software_update",
            "tactic": "malware_distribution"
        }
    }
]

# Transaction Analysis Patterns (On-chain behavior patterns)
TRANSACTION_ANALYSIS_PATTERNS = [
    {
        "id": 5001,
        "text": "wallet with zero balance but transaction history emptied wallet pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "high",
            "source": "on_chain_analysis",
            "tactic": "drained_wallet"
        }
    },
    {
        "id": 5002,
        "text": "wallet with no transaction history completely inactive address",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "new_wallet"
        }
    },
    {
        "id": 5003,
        "text": "wallet only receiving transactions no outgoing activity accumulation pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "medium",
            "source": "on_chain_analysis",
            "tactic": "accumulation_wallet"
        }
    },
    {
        "id": 5004,
        "text": "wallet only sending transactions no incoming activity distribution pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "medium",
            "source": "on_chain_analysis",
            "tactic": "distribution_wallet"
        }
    },
    {
        "id": 5005,
        "text": "wallet with very few transactions low activity pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "low_activity"
        }
    },
    {
        "id": 5006,
        "text": "wallet with high transaction frequency active trading pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "high_activity"
        }
    },
    {
        "id": 5007,
        "text": "wallet with large transaction amounts high value transfers",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "medium",
            "source": "on_chain_analysis",
            "tactic": "high_value_transfers"
        }
    },
    {
        "id": 5008,
        "text": "wallet with very small transaction amounts micro transactions pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "medium",
            "source": "on_chain_analysis",
            "tactic": "dusting_attack"
        }
    },
    {
        "id": 5009,
        "text": "wallet interacting with single address limited network pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "medium",
            "source": "on_chain_analysis",
            "tactic": "isolated_wallet"
        }
    },
    {
        "id": 5010,
        "text": "wallet interacting with many addresses diverse network pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "network_wallet"
        }
    },
    {
        "id": 5011,
        "text": "wallet with rapid sequential transactions automated trading pattern",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "medium",
            "source": "on_chain_analysis",
            "tactic": "bot_activity"
        }
    },
    {
        "id": 5012,
        "text": "wallet with slow transaction pattern infrequent activity",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "long_term_holder"
        }
    },
    {
        "id": 5013,
        "text": "wallet relationships transaction flow suspicious connections",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "high",
            "source": "on_chain_analysis",
            "tactic": "suspicious_relationships"
        }
    },
    {
        "id": 5014,
        "text": "wallet stalking pattern monitoring other addresses tracking behavior",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "high",
            "source": "on_chain_analysis",
            "tactic": "wallet_stalking"
        }
    },
    {
        "id": 5015,
        "text": "high value wallet large balance significant funds",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "whale_wallet"
        }
    },
    {
        "id": 5016,
        "text": "wallet with very low balance minimal funds",
        "attack_type": "transaction_analysis",
        "metadata": {
            "severity": "low",
            "source": "on_chain_analysis",
            "tactic": "low_balance"
        }
    }
]

async def seed_database():
    """Seed all collections with attack patterns"""
    print("Initializing Enhanced Qdrant Service...")
    qdrant = EnhancedQdrantService()
    
    all_patterns = [
        *SIM_SWAPPING_PATTERNS,
        *WALLET_STALKING_PATTERNS,
        *ADDRESS_SPOOFING_PATTERNS,
        *GENERAL_PHISHING_PATTERNS,
        *TRANSACTION_ANALYSIS_PATTERNS
    ]
    
    print(f"\nSeeding {len(all_patterns)} attack patterns across {len(qdrant.collections)} collections...\n")
    
    for pattern in all_patterns:
        await qdrant.add_attack_pattern(
            pattern_id=pattern["id"],
            text=pattern["text"],
            attack_type=pattern["attack_type"],
            metadata=pattern.get("metadata", {})
        )
        print(f"  [OK] [{pattern['attack_type'].upper()}] Added pattern #{pattern['id']}")
    
    print("\nDatabase seeded successfully!")
    
    # Get statistics
    stats = await qdrant.get_collection_stats()
    print("\nCollection Statistics:")
    for attack_type, stat in stats.items():
        if "error" not in stat:
            print(f"   {attack_type}: {stat['vectors_count']} patterns")
        else:
            print(f"   {attack_type}: Error - {stat['error']}")

if __name__ == "__main__":
    asyncio.run(seed_database())

