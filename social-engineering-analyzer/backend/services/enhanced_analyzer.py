"""
Enhanced Analyzer Service - Comprehensive threat detection for Web3 social engineering
Handles SIM swapping, wallet stalking, address spoofing, and general phishing
"""

from services.enhanced_qdrant_service import EnhancedQdrantService
from typing import Dict, List, Optional
import re

class EnhancedAnalyzerService:
    """
    Enhanced analyzer that provides comprehensive threat detection
    """
    
    def __init__(self, qdrant_service: EnhancedQdrantService):
        self.qdrant = qdrant_service
        
        # Red flag keywords for different attack types
        self.red_flags = {
            "urgency": [
                "urgent", "immediately", "asap", "right now", "limited time",
                "expires soon", "act now", "don't delay"
            ],
            "authority": [
                "verify your account", "confirm your identity", "security check",
                "account suspended", "account locked", "compliance required"
            ],
            "financial": [
                "send funds", "transfer money", "payment required", "transaction fee",
                "unlock wallet", "verify payment", "refund processing"
            ],
            "crypto_specific": [
                "seed phrase", "private key", "mnemonic", "wallet connect",
                "gas fee", "smart contract", "defi protocol", "airdrop"
            ]
        }
    
    async def analyze_comprehensive(
        self,
        content: str,
        user_address: Optional[str] = None,
        known_addresses: Optional[List[str]] = None,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Comprehensive analysis of content for all threat types
        
        Args:
            content: Text/message to analyze
            user_address: User's wallet address (optional)
            known_addresses: List of addresses user owns/trusts (optional)
            context: Additional context (phone number, transaction data, etc.)
        
        Returns:
            Comprehensive threat analysis with scores and recommendations
        """
        results = {
            "overall_threat_score": 0.0,
            "threat_level": "LOW",
            "detected_attacks": [],
            "detailed_analysis": {},
            "recommendations": [],
            "address_analysis": None,
            "sim_swap_analysis": None,
            "wallet_stalking_analysis": None
        }
        
        # 1. General pattern matching
        general_results = await self.qdrant.search_attack_patterns(
            content,
            attack_types=None,  # Search all collections
            limit=10,
            score_threshold=0.4
        )
        
        # 2. Extract wallet addresses from content
        addresses_in_content = self.qdrant.extract_wallet_addresses(content)
        
        # 3. Address spoofing detection (if addresses found and user addresses provided)
        if addresses_in_content and known_addresses:
            address_analysis = await self.qdrant.detect_address_spoofing(
                addresses_in_content[0],
                known_addresses
            )
            results["address_analysis"] = address_analysis
            
            if address_analysis["is_spoofed"]:
                results["detected_attacks"].append({
                    "type": "address_spoofing",
                    "severity": "CRITICAL",
                    "confidence": 0.9
                })
        
        # 4. SIM swapping detection
        sim_swap_analysis = await self.qdrant.detect_sim_swapping(
            content,
            context
        )
        results["sim_swap_analysis"] = sim_swap_analysis
        
        if sim_swap_analysis["is_sim_swap"]:
            results["detected_attacks"].append({
                "type": "sim_swapping",
                "severity": "CRITICAL",
                "confidence": 0.85
            })
        
        # 5. Wallet stalking detection (if transaction context provided)
        if context and context.get("transaction_data"):
            stalking_analysis = await self.qdrant.detect_wallet_stalking(
                context["transaction_data"],
                user_address or ""
            )
            results["wallet_stalking_analysis"] = stalking_analysis
            
            if stalking_analysis["is_stalking"]:
                results["detected_attacks"].append({
                    "type": "wallet_stalking",
                    "severity": "HIGH",
                    "confidence": 0.75
                })
        
        # 6. Calculate overall threat score
        threat_scores = []
        
        # Score from general pattern matching
        if general_results:
            max_similarity = 0.0
            for attack_type, patterns in general_results.items():
                if patterns and len(patterns) > 0:
                    pattern_score = patterns[0].get("score", 0.0)
                    max_similarity = max(max_similarity, pattern_score)
            if max_similarity > 0:
                threat_scores.append(max_similarity * 100)
        
        # Score from address spoofing
        if results["address_analysis"] and results["address_analysis"]["is_spoofed"]:
            threat_scores.append(90)  # Critical threat
        
        # Score from SIM swapping
        if results["sim_swap_analysis"] and results["sim_swap_analysis"]["is_sim_swap"]:
            threat_scores.append(85)  # Critical threat
        
        # Score from wallet stalking
        if results["wallet_stalking_analysis"] and results["wallet_stalking_analysis"]["is_stalking"]:
            threat_scores.append(70)  # High threat
        
        # Score from red flags
        red_flag_score = self._calculate_red_flag_score(content)
        threat_scores.append(red_flag_score)
        
        # Overall threat score (take maximum, but weight multiple detections)
        if threat_scores:
            base_score = max(threat_scores)
            # Boost score if multiple attack types detected
            if len(results["detected_attacks"]) > 1:
                base_score = min(base_score * 1.2, 100)
            results["overall_threat_score"] = round(base_score, 2)
        
        # Determine threat level
        if results["overall_threat_score"] >= 80:
            results["threat_level"] = "CRITICAL"
        elif results["overall_threat_score"] >= 60:
            results["threat_level"] = "HIGH"
        elif results["overall_threat_score"] >= 40:
            results["threat_level"] = "MEDIUM"
        else:
            results["threat_level"] = "LOW"
        
        # Generate recommendations
        results["recommendations"] = self._generate_recommendations(results)
        
        # Detailed analysis breakdown
        results["detailed_analysis"] = {
            "pattern_matches": general_results,
            "red_flags_detected": self._detect_red_flags(content),
            "addresses_found": addresses_in_content,
            "threat_breakdown": {
                "pattern_similarity": self._get_max_pattern_similarity(general_results),
                "address_spoofing": 90 if (results["address_analysis"] and results["address_analysis"]["is_spoofed"]) else 0,
                "sim_swapping": 85 if (results["sim_swap_analysis"] and results["sim_swap_analysis"]["is_sim_swap"]) else 0,
                "wallet_stalking": 70 if (results["wallet_stalking_analysis"] and results["wallet_stalking_analysis"]["is_stalking"]) else 0,
                "red_flags": red_flag_score
            }
        }
        
        return results
    
    def _get_max_pattern_similarity(self, general_results: Dict) -> float:
        """Get maximum pattern similarity score from results"""
        if not general_results:
            return 0.0
        
        similarities = []
        for attack_type, patterns in general_results.items():
            if patterns and len(patterns) > 0:
                score = patterns[0].get("score", 0.0)
                similarities.append(score * 100)
        
        return max(similarities) if similarities else 0.0
    
    def _calculate_red_flag_score(self, content: str) -> float:
        """Calculate threat score based on red flag keywords"""
        content_lower = content.lower()
        score = 0.0
        
        for category, keywords in self.red_flags.items():
            matches = sum(1 for keyword in keywords if keyword in content_lower)
            if category == "urgency":
                score += matches * 15
            elif category == "authority":
                score += matches * 20
            elif category == "financial":
                score += matches * 25
            elif category == "crypto_specific":
                score += matches * 30
        
        return min(score, 100)
    
    def _detect_red_flags(self, content: str) -> List[str]:
        """Detect specific red flag phrases in content"""
        content_lower = content.lower()
        detected = []
        
        for category, keywords in self.red_flags.items():
            for keyword in keywords:
                if keyword in content_lower:
                    detected.append(f"{category}: {keyword}")
        
        return detected
    
    def _generate_recommendations(self, analysis_results: Dict) -> List[str]:
        """Generate actionable recommendations based on analysis"""
        recommendations = []
        
        threat_level = analysis_results["threat_level"]
        detected_attacks = analysis_results["detected_attacks"]
        
        if threat_level == "CRITICAL":
            recommendations.append("🚨 CRITICAL THREAT DETECTED: Do NOT interact with this message in any way.")
            recommendations.append("Do NOT click any links, download files, or provide any information.")
            recommendations.append("If this involves your wallet, verify all addresses manually character-by-character.")
        
        if any(attack["type"] == "address_spoofing" for attack in detected_attacks):
            recommendations.append("⚠️ Address spoofing detected: The address in this message is similar to yours but different. This is a scam.")
            recommendations.append("Always copy addresses from trusted sources and verify the full address before sending funds.")
        
        if any(attack["type"] == "sim_swapping" for attack in detected_attacks):
            recommendations.append("⚠️ SIM swapping attempt detected: Contact your carrier immediately if you didn't request any changes.")
            recommendations.append("Switch to hardware security keys or authenticator apps instead of SMS for 2FA.")
        
        if any(attack["type"] == "wallet_stalking" for attack in detected_attacks):
            recommendations.append("⚠️ Wallet stalking detected: Someone may be monitoring your wallet activity.")
            recommendations.append("Consider using a new wallet address if you're concerned about privacy.")
            recommendations.append("Be cautious about sharing your wallet address publicly.")
        
        if threat_level in ["HIGH", "MEDIUM"]:
            recommendations.append("Exercise extreme caution. Verify the sender through a separate, trusted channel.")
            recommendations.append("Never share private keys, seed phrases, or passwords.")
        
        if not recommendations:
            recommendations.append("✓ No significant threats detected, but always verify unexpected messages.")
            recommendations.append("When in doubt, contact the organization directly through their official website.")
        
        return recommendations
    
    async def analyze_simple(self, content: str) -> Dict:
        """
        Simplified analysis for basic use cases
        Returns a simplified version compatible with the original API
        """
        comprehensive = await self.analyze_comprehensive(content)
        
        # Format for backward compatibility
        pattern_similarity = comprehensive["detailed_analysis"]["threat_breakdown"]["pattern_similarity"]
        similarity_score = pattern_similarity / 100.0 if pattern_similarity > 0 else 0.0
        
        patterns = [
            f"{attack['type']} ({attack['severity']})" 
            for attack in comprehensive["detected_attacks"]
        ]
        
        # If no patterns detected, add a default message
        if not patterns:
            patterns = ["No specific attack patterns detected"]
        
        recommendations = comprehensive["recommendations"][:2] if comprehensive["recommendations"] else ["No threats detected"]
        
        return {
            "threat_score": comprehensive["overall_threat_score"],
            "similarity_score": similarity_score,
            "patterns": patterns,
            "recommendation": " | ".join(recommendations)
        }

