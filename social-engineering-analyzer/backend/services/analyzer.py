"""
Analyzer Service - Main logic for analyzing content for threats
"""

from services.qdrant_service import QdrantService
from typing import Dict, List

class AnalyzerService:
    """
    Service that analyzes content for social engineering patterns
    
    ELI5: This is the detective that looks at your message,
    compares it to known scams, and tells you if it's dangerous.
    """
    
    def __init__(self, qdrant_service: QdrantService):
        self.qdrant = qdrant_service
        
        # Common social engineering indicators
        self.red_flags = [
            "urgent action required",
            "verify your account",
            "click here immediately",
            "limited time offer",
            "your account will be closed",
            "suspended",
            "verify identity",
            "unusual activity",
        ]
    
    async def analyze(self, content: str) -> Dict:
        """
        Analyze content for social engineering threats
        
        Returns:
            Dict with threat_score, similarity_score, patterns, recommendation
        """
        # Step 1: Search for similar patterns in Qdrant
        similar_patterns = await self.qdrant.search_similar(
            query_text=content,
            limit=5,
            score_threshold=0.3  # Lower threshold to catch more potential threats
        )
        
        # Step 2: Calculate threat score based on similarity
        similarity_score = 0.0
        if similar_patterns:
            # Get highest similarity score
            similarity_score = similar_patterns[0]["score"]
        
        # Step 3: Check for red flag keywords
        content_lower = content.lower()
        detected_flags = []
        for flag in self.red_flags:
            if flag in content_lower:
                detected_flags.append(flag)
        
        # Step 4: Calculate overall threat score (0-100)
        # Base score from similarity
        threat_score = similarity_score * 70  # Convert 0-1 to 0-70
        
        # Add points for red flags
        red_flag_score = len(detected_flags) * 10
        threat_score = min(threat_score + red_flag_score, 100)  # Cap at 100
        
        # Step 5: Generate recommendation
        recommendation = self._generate_recommendation(threat_score, similarity_score)
        
        # Step 6: Extract detected patterns
        patterns = []
        if similar_patterns:
            for pattern in similar_patterns[:3]:  # Top 3 patterns
                pattern_type = pattern.get("payload", {}).get("type", "Unknown")
                patterns.append(f"{pattern_type} (similarity: {pattern['score']:.2f})")
        
        if detected_flags:
            patterns.extend([f"Red flag: {flag}" for flag in detected_flags[:3]])
        
        return {
            "threat_score": round(threat_score, 2),
            "similarity_score": round(similarity_score, 3),
            "patterns": patterns,
            "recommendation": recommendation
        }
    
    def _generate_recommendation(self, threat_score: float, similarity_score: float) -> str:
        """Generate user-friendly recommendation based on threat score"""
        if threat_score >= 80:
            return "⚠️ HIGH RISK: This appears to be a social engineering attack. Do NOT click any links, download files, or provide personal information. Delete this message."
        elif threat_score >= 60:
            return "⚠️ MODERATE RISK: This message shows characteristics of social engineering. Be very cautious. Verify the sender through a separate channel before taking any action."
        elif threat_score >= 40:
            return "ℹ️ LOW RISK: Some suspicious indicators detected, but not conclusive. Exercise caution and verify the source."
        else:
            return "✓ LOW RISK: No significant threat patterns detected. However, always be cautious with unexpected messages."


