"""
Wallet Analyzer - High-level on-chain analysis using Qdrant
Analyzes wallet behavior, transaction patterns, and detects anomalies
"""

from services.enhanced_qdrant_service import EnhancedQdrantService
from typing import Dict, List, Optional, Tuple
import re
from web3 import Web3
import asyncio

class WalletAnalyzer:
    """
    Analyzes on-chain wallet activity to detect suspicious patterns
    
    Uses Qdrant to:
    - Store transaction pattern vectors
    - Cluster similar wallet behaviors
    - Detect anomalies in transaction flows
    - Identify wallet relationships
    """
    
    def __init__(self, qdrant_service: EnhancedQdrantService, rpc_url: str):
        self.qdrant = qdrant_service
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        
    async def analyze_wallet(
        self,
        wallet_address: str,
        include_transactions: bool = True,
        depth: int = 100
    ) -> Dict:
        """
        Comprehensive wallet analysis
        
        Args:
            wallet_address: Wallet address to analyze
            include_transactions: Whether to fetch and analyze transactions
            depth: Number of transactions to analyze
        
        Returns:
            Comprehensive wallet analysis with risk scores and patterns
        """
        if not self.w3.is_address(wallet_address):
            raise ValueError(f"Invalid wallet address: {wallet_address}")
        
        wallet_address = self.w3.to_checksum_address(wallet_address)
        
        results = {
            "wallet_address": wallet_address,
            "risk_score": 0.0,
            "risk_level": "LOW",
            "patterns_detected": [],
            "anomalies": [],
            "transaction_summary": {},
            "behavioral_cluster": None,
            "recommendations": []
        }
        
        # Get wallet balance
        try:
            balance = self.w3.eth.get_balance(wallet_address)
            balance_eth = self.w3.from_wei(balance, 'ether')
            results["transaction_summary"]["balance"] = float(balance_eth)
        except Exception as e:
            results["transaction_summary"]["balance"] = 0.0
        
        if include_transactions:
            # Analyze transaction patterns
            tx_analysis = await self._analyze_transaction_patterns(wallet_address, depth)
            results.update(tx_analysis)
        
        # Detect behavioral patterns using Qdrant
        behavioral_patterns = await self._detect_behavioral_patterns(wallet_address, results)
        results["patterns_detected"].extend(behavioral_patterns)
        
        # Calculate overall risk score
        results["risk_score"] = self._calculate_risk_score(results)
        results["risk_level"] = self._get_risk_level(results["risk_score"])
        
        # Generate recommendations
        results["recommendations"] = self._generate_recommendations(results)
        
        return results
    
    async def _analyze_transaction_patterns(
        self,
        wallet_address: str,
        depth: int
    ) -> Dict:
        """Analyze transaction patterns for a wallet"""
        patterns = {
            "transaction_count": 0,
            "unique_interactions": set(),
            "incoming_txns": 0,
            "outgoing_txns": 0,
            "total_volume_in": 0.0,
            "total_volume_out": 0.0,
            "average_tx_value": 0.0,
            "time_patterns": [],
            "anomalies": []
        }
        
        try:
            # Get recent transactions (this is a simplified version)
            # In production, you'd use a block explorer API or indexer
            
            # For now, we'll create a pattern vector from wallet characteristics
            wallet_signature = self._create_wallet_signature(wallet_address, patterns)
            
            # Search for similar wallet behaviors in Qdrant
            similar_wallets = await self.qdrant.search_attack_patterns(
                wallet_signature,
                attack_types=["wallet_stalking", "transaction_analysis"],
                limit=5,
                score_threshold=0.3
            )
            
            return {
                "transaction_summary": {
                    "count": patterns["transaction_count"],
                    "unique_interactions": len(patterns["unique_interactions"]),
                    "incoming": patterns["incoming_txns"],
                    "outgoing": patterns["outgoing_txns"],
                    "volume_in": patterns["total_volume_in"],
                    "volume_out": patterns["total_volume_out"]
                },
                "similar_wallet_patterns": similar_wallets,
                "anomalies": patterns["anomalies"]
            }
        except Exception as e:
            return {
                "transaction_summary": {},
                "similar_wallet_patterns": {},
                "anomalies": [f"Error analyzing transactions: {str(e)}"]
            }
    
    def _create_wallet_signature(self, address: str, patterns: Dict) -> str:
        """Create a text signature representing wallet behavior"""
        signature_parts = [
            f"wallet address {address}",
            f"transaction count {patterns.get('transaction_count', 0)}",
            f"incoming transactions {patterns.get('incoming_txns', 0)}",
            f"outgoing transactions {patterns.get('outgoing_txns', 0)}",
            f"unique interactions {len(patterns.get('unique_interactions', set()))}"
        ]
        return " ".join(signature_parts)
    
    async def _detect_behavioral_patterns(
        self,
        wallet_address: str,
        wallet_data: Dict
    ) -> List[Dict]:
        """Detect behavioral patterns using vector search"""
        patterns = []
        
        # Create analysis text
        analysis_text = f"""
        Wallet {wallet_address}
        Balance: {wallet_data.get('transaction_summary', {}).get('balance', 0)} ETH
        Transaction patterns: {wallet_data.get('transaction_summary', {})}
        """
        
        # Search for similar patterns
        results = await self.qdrant.search_attack_patterns(
            analysis_text,
            attack_types=["wallet_stalking", "transaction_analysis"],
            limit=3,
            score_threshold=0.4
        )
        
        for attack_type, matches in results.items():
            if matches:
                for match in matches:
                    patterns.append({
                        "type": attack_type,
                        "pattern": match.get("payload", {}).get("text", ""),
                        "similarity": match.get("score", 0.0),
                        "severity": match.get("payload", {}).get("metadata", {}).get("severity", "medium")
                    })
        
        return patterns
    
    def _calculate_risk_score(self, results: Dict) -> float:
        """Calculate overall risk score based on detected patterns"""
        score = 0.0
        
        # Base score from patterns
        for pattern in results.get("patterns_detected", []):
            similarity = pattern.get("similarity", 0.0)
            severity = pattern.get("severity", "medium")
            
            if severity == "critical":
                score += similarity * 40
            elif severity == "high":
                score += similarity * 30
            elif severity == "medium":
                score += similarity * 20
            else:
                score += similarity * 10
        
        # Anomaly detection
        if results.get("anomalies"):
            score += len(results["anomalies"]) * 15
        
        # Transaction pattern analysis
        tx_summary = results.get("transaction_summary", {})
        if tx_summary.get("outgoing_txns", 0) > 100:
            score += 10  # High activity
        
        return min(score, 100.0)
    
    def _get_risk_level(self, score: float) -> str:
        """Get risk level from score"""
        if score >= 80:
            return "CRITICAL"
        elif score >= 60:
            return "HIGH"
        elif score >= 40:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _generate_recommendations(self, results: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        risk_level = results["risk_level"]
        patterns = results.get("patterns_detected", [])
        
        if risk_level == "CRITICAL":
            recommendations.append("🚨 CRITICAL: This wallet shows highly suspicious patterns. Exercise extreme caution.")
            recommendations.append("Do not interact with this wallet or send funds to it.")
        
        if any(p.get("type") == "wallet_stalking" for p in patterns):
            recommendations.append("⚠️ Wallet stalking patterns detected. This wallet may be monitoring other addresses.")
        
        if results.get("anomalies"):
            recommendations.append(f"⚠️ {len(results['anomalies'])} anomalies detected in transaction patterns.")
        
        if not recommendations:
            recommendations.append("✓ No significant threats detected in wallet behavior.")
        
        return recommendations
    
    async def compare_wallets(
        self,
        wallet1: str,
        wallet2: str
    ) -> Dict:
        """Compare two wallets to find similarities"""
        analysis1 = await self.analyze_wallet(wallet1, include_transactions=False)
        analysis2 = await self.analyze_wallet(wallet2, include_transactions=False)
        
        # Calculate similarity
        sig1 = self._create_wallet_signature(wallet1, analysis1.get("transaction_summary", {}))
        sig2 = self._create_wallet_signature(wallet2, analysis2.get("transaction_summary", {}))
        
        # Use Qdrant to find similarity
        vector1 = self.qdrant.encode_text(sig1)
        vector2 = self.qdrant.encode_text(sig2)
        
        # Calculate cosine similarity
        similarity = self._cosine_similarity(vector1, vector2)
        
        return {
            "wallet1": wallet1,
            "wallet2": wallet2,
            "similarity_score": similarity,
            "analysis1": analysis1,
            "analysis2": analysis2,
            "likely_related": similarity > 0.7
        }
    
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two vectors"""
        import math
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(a * a for a in vec2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        return dot_product / (magnitude1 * magnitude2)

