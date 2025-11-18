"""
Enhanced Qdrant Service - Specialized for Web3 Social Engineering Detection
Handles SIM swapping, wallet stalking, address spoofing, and other crypto-specific attacks
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer
import os
from typing import List, Dict, Optional, Tuple
import hashlib
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EnhancedQdrantService:
    """
    Enhanced Qdrant service with specialized collections for different attack types
    
    Collections:
    1. sim_swapping_patterns - SIM swap attack indicators
    2. wallet_stalking_patterns - Wallet tracking and stalking attempts
    3. address_spoofing_patterns - Address spoofing and phishing
    4. general_phishing - General social engineering patterns
    """
    
    def __init__(self):
        # Get Qdrant URL from environment or use default
        self.qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        self.qdrant_api_key = os.getenv("QDRANT_API_KEY", None)
        
        # Initialize Qdrant client (with API key if provided for Qdrant Cloud)
        if self.qdrant_api_key:
            self.client = QdrantClient(url=self.qdrant_url, api_key=self.qdrant_api_key)
        else:
            self.client = QdrantClient(url=self.qdrant_url)
        
        # Use a better model for financial/crypto context
        # all-mpnet-base-v2 is better for semantic similarity
        self.model = SentenceTransformer('all-mpnet-base-v2')
        self.vector_size = 768  # Size of vectors for this model
        
        # Collection names
        self.collections = {
            "sim_swapping": "sim_swapping_patterns",
            "wallet_stalking": "wallet_stalking_patterns",
            "address_spoofing": "address_spoofing_patterns",
            "general_phishing": "general_phishing_patterns",
            "transaction_analysis": "transaction_analysis_patterns"
        }
        
        # Initialize all collections
        self._ensure_all_collections()
    
    def _ensure_all_collections(self):
        """Create all collections if they don't exist"""
        for collection_name in self.collections.values():
            try:
                self.client.get_collection(collection_name)
            except Exception:
                # Collection doesn't exist, create it
                self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(
                        size=self.vector_size,
                        distance=Distance.COSINE
                    )
                )
                print(f"Created collection: {collection_name}")
    
    def encode_text(self, text: str) -> List[float]:
        """Convert text to vector representation"""
        vector = self.model.encode(text, normalize_embeddings=True).tolist()
        return vector
    
    def extract_wallet_addresses(self, text: str) -> List[str]:
        """Extract Ethereum-style addresses from text"""
        # Ethereum address pattern: 0x followed by 40 hex characters
        pattern = r'0x[a-fA-F0-9]{40}'
        addresses = re.findall(pattern, text)
        return addresses
    
    def calculate_address_similarity(self, addr1: str, addr2: str) -> float:
        """
        Calculate similarity between two wallet addresses
        Used to detect address spoofing (similar-looking addresses)
        """
        if not addr1 or not addr2:
            return 0.0
        
        # Normalize addresses
        addr1 = addr1.lower().replace('0x', '')
        addr2 = addr2.lower().replace('0x', '')
        
        if len(addr1) != 40 or len(addr2) != 40:
            return 0.0
        
        # Count matching characters in same positions
        matches = sum(1 for a, b in zip(addr1, addr2) if a == b)
        similarity = matches / 40.0
        
        # Also check for common spoofing patterns
        # (e.g., only first/last few characters differ)
        if addr1[:6] == addr2[:6] and addr1[-4:] == addr2[-4:]:
            similarity = max(similarity, 0.7)  # Boost similarity for common spoof pattern
        
        return similarity
    
    async def search_attack_patterns(
        self,
        query_text: str,
        attack_types: Optional[List[str]] = None,
        limit: int = 5,
        score_threshold: float = 0.5
    ) -> Dict[str, List[Dict]]:
        """
        Search across multiple collections for attack patterns
        
        Args:
            query_text: Text to analyze
            attack_types: List of attack types to search (None = search all)
            limit: Number of results per collection
            score_threshold: Minimum similarity score
        
        Returns:
            Dict mapping attack type to list of similar patterns
        """
        query_vector = self.encode_text(query_text)
        results = {}
        
        # Determine which collections to search
        collections_to_search = (
            [self.collections[at] for at in attack_types]
            if attack_types
            else list(self.collections.values())
        )
        
        for collection_name in collections_to_search:
            try:
                search_results = self.client.search(
                    collection_name=collection_name,
                    query_vector=query_vector,
                    limit=limit,
                    score_threshold=score_threshold
                )
                
                formatted_results = []
                for result in search_results:
                    formatted_results.append({
                        "id": result.id,
                        "score": result.score,
                        "payload": result.payload
                    })
                
                # Get collection type name
                collection_type = next(
                    k for k, v in self.collections.items() if v == collection_name
                )
                results[collection_type] = formatted_results
            except Exception as e:
                print(f"Error searching {collection_name}: {e}")
                results[collection_name] = []
        
        return results
    
    async def detect_address_spoofing(
        self,
        suspicious_address: str,
        known_addresses: List[str]
    ) -> Dict:
        """
        Detect if an address is a spoofed version of a known address
        
        Args:
            suspicious_address: The address to check
            known_addresses: List of addresses the user owns/trusts
        
        Returns:
            Dict with spoofing detection results
        """
        spoofing_results = []
        
        for known_addr in known_addresses:
            similarity = self.calculate_address_similarity(
                suspicious_address,
                known_addr
            )
            
            if similarity > 0.6:  # Threshold for potential spoofing
                spoofing_results.append({
                    "known_address": known_addr,
                    "suspicious_address": suspicious_address,
                    "similarity": similarity,
                    "risk_level": "HIGH" if similarity > 0.8 else "MEDIUM"
                })
        
        # Also search for similar addresses in our database
        query_text = f"wallet address {suspicious_address} transaction"
        vector_results = await self.search_attack_patterns(
            query_text,
            attack_types=["address_spoofing"],
            limit=3,
            score_threshold=0.4
        )
        
        return {
            "is_spoofed": len(spoofing_results) > 0,
            "similarity_matches": spoofing_results,
            "database_matches": vector_results.get("address_spoofing", []),
            "recommendation": self._generate_spoofing_recommendation(spoofing_results)
        }
    
    def _generate_spoofing_recommendation(self, matches: List[Dict]) -> str:
        """Generate recommendation for address spoofing"""
        if not matches:
            return "✓ No address spoofing detected. Always verify addresses manually."
        
        high_risk = [m for m in matches if m["risk_level"] == "HIGH"]
        if high_risk:
            return f"⚠️ HIGH RISK: Address {high_risk[0]['suspicious_address']} is very similar to your known address {high_risk[0]['known_address']}. This is likely a spoofing attempt. DO NOT send funds to this address."
        
        return f"⚠️ MEDIUM RISK: Address shows similarity to your known addresses. Double-check the full address before sending any transactions."
    
    async def detect_wallet_stalking(
        self,
        transaction_data: Dict,
        user_address: str
    ) -> Dict:
        """
        Detect wallet stalking patterns
        
        Args:
            transaction_data: Dict with transaction details
            user_address: User's wallet address
        
        Returns:
            Dict with stalking detection results
        """
        # Extract relevant text from transaction
        analysis_text = f"""
        Transaction from {transaction_data.get('from', '')} 
        to {transaction_data.get('to', '')}
        Amount: {transaction_data.get('value', '0')}
        Message: {transaction_data.get('message', '')}
        """
        
        # Search for stalking patterns
        results = await self.search_attack_patterns(
            analysis_text,
            attack_types=["wallet_stalking"],
            limit=5,
            score_threshold=0.4
        )
        
        # Check for suspicious patterns
        suspicious_indicators = []
        
        # Check if transaction is from unknown address with small amount (dusting attack)
        if transaction_data.get('value', 0) < 0.0001:
            suspicious_indicators.append("Dusting attack detected (very small transaction)")
        
        # Check for repeated transactions from same address
        if transaction_data.get('repeated_from', False):
            suspicious_indicators.append("Repeated transactions from same address")
        
        return {
            "is_stalking": len(results.get("wallet_stalking", [])) > 0 or len(suspicious_indicators) > 0,
            "patterns_found": results.get("wallet_stalking", []),
            "indicators": suspicious_indicators,
            "recommendation": self._generate_stalking_recommendation(results, suspicious_indicators)
        }
    
    def _generate_stalking_recommendation(self, results: Dict, indicators: List[str]) -> str:
        """Generate recommendation for wallet stalking"""
        if not results.get("wallet_stalking") and not indicators:
            return "✓ No wallet stalking patterns detected."
        
        if indicators:
            return f"⚠️ WARNING: {indicators[0]}. Consider using a new wallet address if you're concerned about privacy."
        
        return "⚠️ Potential wallet stalking detected. Be cautious about sharing your wallet address publicly."
    
    async def detect_sim_swapping(
        self,
        message_text: str,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Detect SIM swapping attack indicators
        
        Args:
            message_text: Message to analyze
            context: Additional context (phone number, carrier, etc.)
        
        Returns:
            Dict with SIM swapping detection results
        """
        # Enhance query with context
        enhanced_query = message_text
        if context:
            enhanced_query += f" phone {context.get('phone', '')} carrier {context.get('carrier', '')}"
        
        # Search for SIM swapping patterns
        results = await self.search_attack_patterns(
            enhanced_query,
            attack_types=["sim_swapping"],
            limit=5,
            score_threshold=0.4
        )
        
        # Check for SIM swap indicators
        indicators = []
        text_lower = message_text.lower()
        
        sim_swap_keywords = [
            "port your number",
            "transfer your sim",
            "carrier verification",
            "phone number change",
            "sim card replacement",
            "two-factor authentication",
            "sms verification code",
            "text message code"
        ]
        
        for keyword in sim_swap_keywords:
            if keyword in text_lower:
                indicators.append(f"Contains SIM swap keyword: {keyword}")
        
        return {
            "is_sim_swap": len(results.get("sim_swapping", [])) > 0 or len(indicators) > 2,
            "patterns_found": results.get("sim_swapping", []),
            "indicators": indicators,
            "recommendation": self._generate_sim_swap_recommendation(results, indicators)
        }
    
    def _generate_sim_swap_recommendation(self, results: Dict, indicators: List[str]) -> str:
        """Generate recommendation for SIM swapping"""
        if not results.get("sim_swapping") and len(indicators) < 2:
            return "✓ No SIM swapping indicators detected."
        
        return "⚠️ HIGH RISK: Potential SIM swapping attempt detected. Contact your carrier immediately if you didn't request any changes. Use hardware security keys instead of SMS for 2FA."
    
    async def add_attack_pattern(
        self,
        pattern_id: int,
        text: str,
        attack_type: str,
        metadata: Optional[Dict] = None
    ):
        """
        Add a new attack pattern to the appropriate collection
        
        Args:
            pattern_id: Unique identifier
            text: Pattern text
            attack_type: Type of attack (sim_swapping, wallet_stalking, etc.)
            metadata: Additional information
        """
        if attack_type not in self.collections:
            raise ValueError(f"Unknown attack type: {attack_type}")
        
        collection_name = self.collections[attack_type]
        vector = self.encode_text(text)
        
        point = PointStruct(
            id=pattern_id,
            vector=vector,
            payload={
                "text": text,
                "attack_type": attack_type,
                **(metadata or {})
            }
        )
        
        self.client.upsert(
            collection_name=collection_name,
            points=[point]
        )
    
    async def get_collection_stats(self) -> Dict:
        """Get statistics for all collections"""
        stats = {}
        for attack_type, collection_name in self.collections.items():
            try:
                info = self.client.get_collection(collection_name)
                # Handle both old and new API versions
                vectors_count = getattr(info, 'vectors_count', getattr(info, 'points_count', 0))
                points_count = getattr(info, 'points_count', vectors_count)
                stats[attack_type] = {
                    "vectors_count": vectors_count,
                    "points_count": points_count
                }
            except Exception as e:
                stats[attack_type] = {"error": str(e)}
        
        return stats
    
    async def check_health(self) -> bool:
        """Check if Qdrant is accessible"""
        try:
            self.client.get_collections()
            return True
        except Exception:
            return False

