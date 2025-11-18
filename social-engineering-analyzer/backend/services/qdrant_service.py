"""
Qdrant Service - Handles all interactions with Qdrant vector database
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
import os
from typing import List, Dict, Optional
import asyncio

class QdrantService:
    """
    Service for interacting with Qdrant vector database
    
    ELI5: Qdrant is like a smart filing cabinet that finds similar things,
    not just exact matches. This service puts data in and gets similar data out.
    """
    
    def __init__(self):
        # Get Qdrant URL from environment or use default
        self.qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        
        # Initialize Qdrant client
        self.client = QdrantClient(url=self.qdrant_url)
        
        # Initialize sentence transformer model for converting text to vectors
        # This model converts sentences into numbers (vectors) that represent meaning
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.vector_size = 384  # Size of vectors this model produces
        
        # Collection name where we store attack patterns
        self.collection_name = "social_engineering_vectors"
        
        # Ensure collection exists
        self._ensure_collection()
    
    def _ensure_collection(self):
        """Create collection if it doesn't exist"""
        try:
            # Try to get collection info
            self.client.get_collection(self.collection_name)
        except Exception:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,
                    distance=Distance.COSINE  # Cosine similarity (measures angle between vectors)
                )
            )
            print(f"Created collection: {self.collection_name}")
    
    async def check_health(self) -> bool:
        """Check if Qdrant is accessible"""
        try:
            self.client.get_collections()
            return True
        except Exception:
            return False
    
    def encode_text(self, text: str) -> List[float]:
        """
        Convert text to vector (numbers that represent meaning)
        
        ELI5: Like translating words into a special number language
        where similar words have similar numbers
        """
        vector = self.model.encode(text).tolist()
        return vector
    
    async def search_similar(
        self,
        query_text: str,
        limit: int = 5,
        score_threshold: float = 0.5
    ) -> List[Dict]:
        """
        Search for similar attack patterns
        
        Args:
            query_text: Text to search for
            limit: How many similar results to return
            score_threshold: Minimum similarity score (0-1)
        
        Returns:
            List of similar patterns with scores
        """
        # Convert query text to vector
        query_vector = self.encode_text(query_text)
        
        # Search in Qdrant
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit,
            score_threshold=score_threshold
        )
        
        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                "id": result.id,
                "score": result.score,  # Similarity score (higher = more similar)
                "payload": result.payload  # Additional data stored with the vector
            })
        
        return formatted_results
    
    async def add_pattern(
        self,
        pattern_id: int,
        text: str,
        metadata: Optional[Dict] = None
    ):
        """
        Add a new attack pattern to the database
        
        Args:
            pattern_id: Unique identifier
            text: Pattern text
            metadata: Additional information (type, source, etc.)
        """
        vector = self.encode_text(text)
        
        point = PointStruct(
            id=pattern_id,
            vector=vector,
            payload={
                "text": text,
                **(metadata or {})
            }
        )
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )
    
    async def get_collection_info(self) -> Dict:
        """Get information about the collection"""
        info = self.client.get_collection(self.collection_name)
        return {
            "vectors_count": info.vectors_count,
            "points_count": info.points_count
        }


