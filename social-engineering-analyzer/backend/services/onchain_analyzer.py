"""
On-Chain Analyzer - Advanced blockchain analysis using Qdrant
Detects wallet relationships, transaction patterns, and suspicious activity
"""

from services.enhanced_qdrant_service import EnhancedQdrantService
from typing import Dict, List, Optional, Tuple
from web3 import Web3
import asyncio
from collections import defaultdict
from datetime import datetime, timedelta

class OnChainAnalyzer:
    """
    High-level on-chain analysis system
    
    Features:
    - Wallet behavior clustering
    - Transaction flow analysis
    - Address relationship mapping
    - Anomaly detection
    - Pattern recognition in on-chain activity
    """
    
    def __init__(self, qdrant_service: EnhancedQdrantService, rpc_url: str):
        self.qdrant = qdrant_service
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.rpc_url = rpc_url
    
    async def analyze_wallet_activity(
        self,
        wallet_address: str,
        block_range: Optional[Tuple[int, int]] = None
    ) -> Dict:
        """
        Comprehensive on-chain wallet analysis
        
        Returns:
            - Wallet metrics (balance, tx count, etc.)
            - Behavioral patterns
            - Risk assessment
            - Similar wallet clusters
            - Transaction flow analysis
        """
        if not self.w3.is_address(wallet_address):
            raise ValueError(f"Invalid address: {wallet_address}")
        
        wallet_address = self.w3.to_checksum_address(wallet_address)
        
        # Get basic wallet info
        balance = self.w3.eth.get_balance(wallet_address)
        balance_eth = float(self.w3.from_wei(balance, 'ether'))
        
        # ACTUALLY FETCH TRANSACTION HISTORY
        tx_patterns = await self._analyze_transaction_patterns(wallet_address, block_range)
        
        # Detect behavioral cluster
        behavioral_cluster = await self._find_behavioral_cluster(wallet_address, tx_patterns)
        
        # Identify relationships
        relationships = await self._identify_wallet_relationships(wallet_address, tx_patterns)
        
        # Detect anomalies
        anomalies = await self._detect_anomalies(wallet_address, tx_patterns)
        
        # Calculate risk score
        risk_analysis = self._calculate_risk(tx_patterns, anomalies, behavioral_cluster)
        
        return {
            "wallet": wallet_address,
            "balance_eth": balance_eth,
            "balance_wei": str(balance),
            "transaction_patterns": tx_patterns,
            "behavioral_cluster": behavioral_cluster,
            "relationships": relationships,
            "anomalies": anomalies,
            "risk_analysis": risk_analysis,
            "insights": self._generate_insights(tx_patterns, anomalies, behavioral_cluster)
        }
    
    async def _analyze_transaction_patterns(
        self,
        wallet_address: str,
        block_range: Optional[Tuple[int, int]]
    ) -> Dict:
        """ACTUALLY fetch and analyze transaction history from blockchain"""
        
        # Get wallet balance
        try:
            balance = self.w3.eth.get_balance(wallet_address)
            balance_eth = float(self.w3.from_wei(balance, 'ether'))
        except Exception as e:
            print(f"DEBUG: Error getting balance: {e}")
            balance_eth = 0.0
        
        # Get latest block
        try:
            latest_block = self.w3.eth.block_number
        except Exception as e:
            print(f"DEBUG: Error getting latest block: {e}")
            latest_block = 0
        
        # Fetch actual transactions - use a smaller range for faster performance
        if block_range:
            start_block, end_block = block_range
        else:
            # Analyze last 1000 blocks (~3.5 hours) - faster and more recent
            start_block = max(0, latest_block - 1000)
            end_block = latest_block
        
        print(f"DEBUG: Fetching transactions from block {start_block} to {end_block}")
        
        # Fetch transactions with better error handling
        transactions = []
        tx_count = 0
        incoming_txs = 0
        outgoing_txs = 0
        total_in = 0.0
        total_out = 0.0
        unique_addresses = set()
        tx_amounts = []
        time_between_txs = []
        last_tx_time = None
        
        # Get transactions - sample blocks for performance (every 10th block)
        # This is faster than scanning every block
        max_blocks_to_check = 500  # Limit to 500 blocks max
        blocks_checked = 0
        
        try:
            # Sample blocks for faster analysis
            block_range_size = end_block - start_block
            sample_interval = max(1, block_range_size // max_blocks_to_check)
            
            for block_offset in range(0, block_range_size + 1, sample_interval):
                if blocks_checked >= max_blocks_to_check:
                    break
                
                block_num = start_block + block_offset
                if block_num > end_block:
                    break
                
                try:
                    # Use timeout to prevent hanging
                    block = self.w3.eth.get_block(block_num, full_transactions=True, timeout=5)
                    if not block or not block.transactions:
                        blocks_checked += 1
                        continue
                    
                    for tx in block.transactions:
                        tx_from = tx.get('from', '').lower()
                        tx_to = tx.get('to', '').lower() if tx.get('to') else None
                        wallet_lower = wallet_address.lower()
                        
                        # Check if transaction involves this wallet
                        if tx_from == wallet_lower or (tx_to and tx_to == wallet_lower):
                            tx_value = float(self.w3.from_wei(tx.get('value', 0), 'ether'))
                            tx_amounts.append(tx_value)
                            unique_addresses.add(tx_from)
                            if tx_to:
                                unique_addresses.add(tx_to)
                            
                            if tx_from == wallet_lower:
                                outgoing_txs += 1
                                total_out += tx_value
                            else:
                                incoming_txs += 1
                                total_in += tx_value
                            
                            tx_count += 1
                            transactions.append({
                                'hash': tx['hash'].hex() if hasattr(tx['hash'], 'hex') else str(tx['hash']),
                                'from': tx_from,
                                'to': tx_to,
                                'value': tx_value,
                                'block': block_num,
                                'timestamp': block.get('timestamp', 0)
                            })
                            
                            # Calculate time between transactions
                            if last_tx_time and block.get('timestamp'):
                                time_diff = block.get('timestamp') - last_tx_time
                                time_between_txs.append(time_diff)
                            if block.get('timestamp'):
                                last_tx_time = block.get('timestamp')
                            
                            if tx_count >= 50:  # Limit to 50 most recent for performance
                                break
                    
                    blocks_checked += 1
                    if tx_count >= 50:
                        break
                        
                except Exception as e:
                    # Skip blocks that fail (might not exist or RPC timeout)
                    print(f"DEBUG: Skipping block {block_num}: {e}")
                    blocks_checked += 1
                    continue
                    
        except Exception as e:
            print(f"DEBUG: Error fetching transactions: {e}")
            # Continue with whatever we got
        
        print(f"DEBUG: Found {tx_count} transactions ({incoming_txs} in, {outgoing_txs} out)")
        
        # Calculate behavioral metrics
        avg_amount = sum(tx_amounts) / len(tx_amounts) if tx_amounts else 0
        max_amount = max(tx_amounts) if tx_amounts else 0
        min_amount = min(tx_amounts) if tx_amounts else 0
        
        # Analyze patterns to create REAL behavioral signature
        behavioral_signature_parts = []
        
        # 1. Transaction frequency pattern
        if tx_count == 0:
            behavioral_signature_parts.append("wallet with no transaction history completely inactive address")
        elif tx_count < 3:
            behavioral_signature_parts.append("wallet with very few transactions low activity pattern")
        elif tx_count > 50:
            behavioral_signature_parts.append("wallet with high transaction frequency active trading pattern")
        
        # 2. Balance pattern
        if balance_eth == 0:
            if tx_count > 0:
                behavioral_signature_parts.append("wallet with zero balance but transaction history emptied wallet pattern")
        elif balance_eth < 0.01:
            behavioral_signature_parts.append("wallet with very low balance minimal funds")
        elif balance_eth > 1000:
            behavioral_signature_parts.append("high value wallet large balance significant funds")
        
        # 3. Transaction flow pattern
        if incoming_txs > 0 and outgoing_txs == 0:
            behavioral_signature_parts.append("wallet only receiving transactions no outgoing activity accumulation pattern")
        elif outgoing_txs > 0 and incoming_txs == 0:
            behavioral_signature_parts.append("wallet only sending transactions no incoming activity distribution pattern")
        
        # 4. Amount patterns
        if tx_amounts and max_amount > 100:
            behavioral_signature_parts.append("wallet with large transaction amounts high value transfers")
        if tx_amounts and avg_amount < 0.001:
            behavioral_signature_parts.append("wallet with very small transaction amounts micro transactions pattern")
        
        # 5. Address diversity
        if len(unique_addresses) == 2:  # Only wallet itself + one other
            behavioral_signature_parts.append("wallet interacting with single address limited network pattern")
        elif len(unique_addresses) > 20:
            behavioral_signature_parts.append("wallet interacting with many addresses diverse network pattern")
        
        # 6. Time patterns
        if time_between_txs:
            avg_time = sum(time_between_txs) / len(time_between_txs)
            if avg_time < 300:  # Less than 5 minutes
                behavioral_signature_parts.append("wallet with rapid sequential transactions automated trading pattern")
            elif avg_time > 86400:  # More than 1 day
                behavioral_signature_parts.append("wallet with slow transaction pattern infrequent activity")
        
        # Create comprehensive behavioral signature
        behavioral_signature = " ".join(behavioral_signature_parts) if behavioral_signature_parts else "normal wallet activity standard transaction pattern"
        
        print(f"DEBUG: Behavioral signature: {behavioral_signature[:200]}")
        
        # Search Qdrant for similar patterns
        similar_patterns = await self.qdrant.search_attack_patterns(
            behavioral_signature,
            attack_types=["transaction_analysis", "wallet_stalking"],
            limit=10,
            score_threshold=0.3  # Lower threshold to catch more patterns
        )
        
        pattern_matches_count = sum(len(patterns) for patterns in similar_patterns.values())
        
        print(f"DEBUG: Qdrant search found {pattern_matches_count} pattern matches")
        if similar_patterns:
            for attack_type, patterns in similar_patterns.items():
                if patterns:
                    top_score = patterns[0].get("score", 0.0)
                    print(f"DEBUG: {attack_type}: {len(patterns)} patterns, top score: {top_score:.3f}")
        
        return {
            "signature": behavioral_signature,
            "similar_patterns": similar_patterns,
            "balance_eth": balance_eth,
            "transaction_count": tx_count,
            "incoming_count": incoming_txs,
            "outgoing_count": outgoing_txs,
            "total_in_eth": total_in,
            "total_out_eth": total_out,
            "avg_amount": avg_amount,
            "max_amount": max_amount,
            "min_amount": min_amount,
            "unique_addresses_count": len(unique_addresses),
            "pattern_matches_count": pattern_matches_count,
            "transactions": transactions[:10]  # Return first 10 for inspection
        }
    
    async def _find_behavioral_cluster(
        self,
        wallet_address: str,
        tx_patterns: Dict
    ) -> Optional[Dict]:
        """Find which behavioral cluster this wallet belongs to"""
        
        cluster_text = tx_patterns.get("signature", f"wallet behavior pattern {wallet_address}")
        
        # Search for similar behaviors
        results = await self.qdrant.search_attack_patterns(
            cluster_text,
            attack_types=["transaction_analysis", "wallet_stalking"],
            limit=5,
            score_threshold=0.35
        )
        
        if results.get("transaction_analysis"):
            best_match = results["transaction_analysis"][0]
            return {
                "cluster_id": best_match.get("id"),
                "similarity": best_match.get("score"),
                "pattern_type": best_match.get("payload", {}).get("metadata", {}).get("tactic", "unknown")
            }
        
        return None
    
    async def _identify_wallet_relationships(
        self,
        wallet_address: str,
        tx_patterns: Dict
    ) -> List[Dict]:
        """Identify relationships with other wallets"""
        
        transactions = tx_patterns.get("transactions", [])
        relationships = []
        
        # Analyze transaction partners
        address_frequency = defaultdict(int)
        for tx in transactions:
            if tx.get('from') and tx['from'].lower() != wallet_address.lower():
                address_frequency[tx['from']] += 1
            if tx.get('to') and tx['to'].lower() != wallet_address.lower():
                address_frequency[tx['to']] += 1
        
        # Find frequent interactions
        for addr, count in sorted(address_frequency.items(), key=lambda x: x[1], reverse=True)[:5]:
            if count >= 3:  # At least 3 transactions
                relationships.append({
                    "type": "frequent_interaction",
                    "address": addr,
                    "transaction_count": count,
                    "confidence": min(count / 10.0, 1.0)
                })
        
        # Search Qdrant for relationship patterns
        relationship_text = f"wallet relationships {wallet_address} {len(transactions)} transactions {len(address_frequency)} partners"
        
        results = await self.qdrant.search_attack_patterns(
            relationship_text,
            attack_types=["wallet_stalking", "transaction_analysis"],
            limit=5,
            score_threshold=0.4
        )
        
        for attack_type, matches in results.items():
            for match in matches:
                if match.get("score", 0) > 0.4:
                    relationships.append({
                        "type": "suspicious_connection",
                        "pattern": match.get("payload", {}).get("text", "")[:100],
                        "confidence": match.get("score", 0.0)
                    })
        
        return relationships
    
    async def _detect_anomalies(
        self,
        wallet_address: str,
        tx_patterns: Dict
    ) -> List[Dict]:
        """Detect anomalies in wallet behavior"""
        
        anomalies = []
        
        tx_count = tx_patterns.get("transaction_count", 0)
        balance_eth = tx_patterns.get("balance_eth", 0)
        incoming = tx_patterns.get("incoming_count", 0)
        outgoing = tx_patterns.get("outgoing_count", 0)
        unique_addrs = tx_patterns.get("unique_addresses_count", 0)
        
        # Anomaly 1: Zero balance but many transactions (drained wallet)
        if balance_eth == 0 and tx_count > 5:
            anomalies.append({
                "type": "transaction_analysis",
                "description": "Wallet has zero balance but significant transaction history - may be drained or emptied",
                "severity": "high",
                "confidence": 0.8
            })
        
        # Anomaly 2: Many incoming but no outgoing (accumulation wallet)
        if incoming > 10 and outgoing == 0:
            anomalies.append({
                "type": "transaction_analysis",
                "description": "Wallet only receives funds, never sends - accumulation pattern",
                "severity": "medium",
                "confidence": 0.7
            })
        
        # Anomaly 3: Very few unique addresses (limited network)
        if tx_count > 5 and unique_addrs <= 2:
            anomalies.append({
                "type": "transaction_analysis",
                "description": "Wallet interacts with very few addresses - limited network pattern",
                "severity": "medium",
                "confidence": 0.6
            })
        
        # Search Qdrant for anomaly patterns
        anomaly_text = tx_patterns.get("signature", f"anomaly detection wallet {wallet_address}")
        
        results = await self.qdrant.search_attack_patterns(
            anomaly_text,
            attack_types=["transaction_analysis"],
            limit=5,
            score_threshold=0.35
        )
        
        for attack_type, matches in results.items():
            for match in matches:
                if match.get("score", 0) > 0.35:
                    anomalies.append({
                        "type": attack_type,
                        "description": match.get("payload", {}).get("text", "")[:150],
                        "severity": match.get("payload", {}).get("metadata", {}).get("severity", "medium"),
                        "confidence": match.get("score", 0.0)
                    })
        
        return anomalies
    
    def _calculate_risk(
        self,
        tx_patterns: Dict,
        anomalies: List[Dict],
        cluster: Optional[Dict]
    ) -> Dict:
        """Calculate risk based on ACTUAL Qdrant pattern matches and real transaction data"""
        
        risk_score = 0.0
        risk_factors = []
        
        # PRIMARY: Pattern matches from Qdrant
        pattern_matches = tx_patterns.get("pattern_matches_count", 0)
        similar_patterns = tx_patterns.get("similar_patterns", {})
        
        max_pattern_score = 0.0
        for attack_type, patterns in similar_patterns.items():
            if patterns:
                for pattern in patterns:
                    score = pattern.get("score", 0.0)
                    max_pattern_score = max(max_pattern_score, score)
                    
                    # Use pattern similarity scores from Qdrant
                    if score > 0.7:  # Very high similarity
                        risk_score += score * 50
                        pattern_text = pattern.get("payload", {}).get("text", "")[:60]
                        severity = pattern.get("payload", {}).get("metadata", {}).get("severity", "medium")
                        risk_factors.append(f"[{severity.upper()}] Strong pattern match ({attack_type}): {pattern_text}...")
                    elif score > 0.5:  # High similarity
                        risk_score += score * 40
                        pattern_text = pattern.get("payload", {}).get("text", "")[:60]
                        severity = pattern.get("payload", {}).get("metadata", {}).get("severity", "medium")
                        risk_factors.append(f"[{severity.upper()}] Pattern match ({attack_type}): {pattern_text}...")
                    elif score > 0.3:  # Moderate similarity
                        risk_score += score * 25
                        risk_factors.append(f"Potential pattern match ({attack_type}, similarity: {score:.2f})")
        
        # Pattern match count bonus
        if pattern_matches >= 5:
            risk_score += 25
            risk_factors.append(f"Multiple suspicious patterns detected ({pattern_matches} matches)")
        elif pattern_matches >= 3:
            risk_score += 15
            risk_factors.append(f"Several suspicious patterns ({pattern_matches} matches)")
        elif pattern_matches >= 1:
            risk_score += 10
            risk_factors.append(f"Pattern match detected ({pattern_matches} match)")
        
        # Anomalies from real transaction analysis
        for anomaly in anomalies:
            severity = anomaly.get("severity", "medium")
            confidence = anomaly.get("confidence", 0.0)
            
            if severity == "critical":
                risk_score += confidence * 40
            elif severity == "high":
                risk_score += confidence * 30
            elif severity == "medium":
                risk_score += confidence * 20
            risk_factors.append(f"{severity.upper()} anomaly: {anomaly.get('description', '')[:80]}")
        
        # Behavioral cluster from Qdrant
        if cluster:
            similarity = cluster.get("similarity", 0)
            if similarity > 0.4:
                risk_score += similarity * 25
                pattern_type = cluster.get("pattern_type", "unknown")
                risk_factors.append(f"Behavioral cluster match: {pattern_type} (similarity: {similarity:.1%})")
        
        # Real transaction-based risk factors
        tx_count = tx_patterns.get("transaction_count", 0)
        balance_eth = tx_patterns.get("balance_eth", 0)
        incoming = tx_patterns.get("incoming_count", 0)
        outgoing = tx_patterns.get("outgoing_count", 0)
        
        # Drained wallet pattern (zero balance + transactions = likely drained)
        if balance_eth == 0 and tx_count > 5:
            risk_score += 30
            risk_factors.append("High risk: Zero balance with transaction history (possibly drained wallet)")
        
        # Accumulation wallet (only receives, suspicious if high value)
        if incoming > 10 and outgoing == 0 and balance_eth > 100:
            risk_score += 15
            risk_factors.append("Medium risk: Accumulation wallet pattern (only receives, never sends)")
        
        # If NO patterns matched AND wallet is normal, it's low risk
        if pattern_matches == 0 and len(anomalies) == 0 and tx_count > 0:
            # Normal active wallet
            risk_score = max(risk_score, 5.0)  # Minimum baseline
            risk_factors.append("No suspicious patterns detected - wallet appears normal")
        elif pattern_matches == 0 and len(anomalies) == 0 and tx_count == 0:
            # Completely new wallet
            risk_score = 0.0
            risk_factors.append("New wallet with no transaction history")
        
        risk_score = min(risk_score, 100.0)
        
        print(f"DEBUG: Risk calculation - pattern_matches: {pattern_matches}, max_score: {max_pattern_score:.3f}, anomalies: {len(anomalies)}, final_risk: {risk_score}")
        
        return {
            "score": round(risk_score, 2),
            "level": self._get_risk_level(risk_score),
            "factors": risk_factors,
            "pattern_matches": pattern_matches,
            "max_pattern_similarity": round(max_pattern_score, 3)
        }
    
    def _get_risk_level(self, score: float) -> str:
        """Get risk level from score"""
        if score >= 80:
            return "CRITICAL"
        elif score >= 60:
            return "HIGH"
        elif score >= 40:
            return "MEDIUM"
        elif score >= 20:
            return "LOW"
        else:
            return "SAFE"
    
    def _generate_insights(
        self,
        tx_patterns: Dict,
        anomalies: List[Dict],
        cluster: Optional[Dict]
    ) -> List[str]:
        """Generate actionable insights"""
        
        insights = []
        tx_count = tx_patterns.get("transaction_count", 0)
        balance_eth = tx_patterns.get("balance_eth", 0)
        
        if tx_count == 0:
            insights.append("📭 New wallet with no transaction history")
        else:
            insights.append(f"📊 Wallet has {tx_count} transactions")
            if balance_eth > 0:
                insights.append(f"💰 Current balance: {balance_eth:.4f} xDAI")
        
        if anomalies:
            insights.append(f"⚠️ Detected {len(anomalies)} behavioral anomalies")
            insights.append("This wallet shows patterns that deviate from normal activity")
        
        if cluster:
            insights.append(f"🔗 Behavioral cluster: {cluster.get('pattern_type', 'Unknown')}")
            insights.append(f"Similarity to known patterns: {cluster.get('similarity', 0):.1%}")
        
        if not anomalies and tx_count > 0:
            insights.append("✓ No significant anomalies detected")
            insights.append("Wallet behavior appears normal based on transaction patterns")
        
        return insights
    
    async def trace_transaction_flow(
        self,
        wallet_address: str,
        depth: int = 2
    ) -> Dict:
        """
        Trace transaction flow from a wallet
        
        This would analyze:
        - Where funds come from
        - Where funds go to
        - Intermediate wallets
        - Circular transactions
        - Dusting attacks
        """
        
        flow_text = f"transaction flow analysis wallet {wallet_address} depth {depth}"
        
        # Search for flow patterns
        results = await self.qdrant.search_attack_patterns(
            flow_text,
            attack_types=["transaction_analysis", "wallet_stalking"],
            limit=5,
            score_threshold=0.3
        )
        
        return {
            "source_wallet": wallet_address,
            "depth": depth,
            "flow_patterns": results,
            "analysis": "Transaction flow analysis would show fund movements and relationships"
        }
    
    async def detect_wallet_cluster(
        self,
        wallet_addresses: List[str]
    ) -> Dict:
        """
        Detect if multiple wallets belong to the same cluster/entity
        
        Uses vector similarity to group related wallets
        """
        
        if len(wallet_addresses) < 2:
            return {"error": "Need at least 2 wallets to detect clusters"}
        
        # Create signatures for each wallet
        signatures = []
        for addr in wallet_addresses:
            sig = f"wallet address {addr} behavioral pattern"
            vector = []
            if hasattr(self.qdrant, 'encode_text'):
                vector = self.qdrant.encode_text(sig)
            signatures.append({
                "address": addr,
                "signature": sig,
                "vector": vector
            })
        
        # Calculate pairwise similarities
        clusters = []
        for i, sig1 in enumerate(signatures):
            for j, sig2 in enumerate(signatures[i+1:], i+1):
                similarity = self._cosine_similarity(sig1["vector"], sig2["vector"])
                if similarity > 0.7:
                    clusters.append({
                        "wallet1": sig1["address"],
                        "wallet2": sig2["address"],
                        "similarity": similarity,
                        "likely_same_entity": similarity > 0.8
                    })
        
        return {
            "wallets_analyzed": len(wallet_addresses),
            "clusters_found": len(clusters),
            "relationships": clusters
        }
    
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity"""
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.0
        
        import math
        dot = sum(a * b for a, b in zip(vec1, vec2))
        mag1 = math.sqrt(sum(a * a for a in vec1))
        mag2 = math.sqrt(sum(a * a for a in vec2))
        return dot / (mag1 * mag2) if (mag1 * mag2) > 0 else 0.0
