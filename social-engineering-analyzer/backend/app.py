"""
Main FastAPI application for Social Engineering Analyzer
This is the backend API that handles analysis requests
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv

from services.qdrant_service import QdrantService
from services.analyzer import AnalyzerService
from services.credit_manager import CreditManager

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Social Engineering Analyzer API",
    description="API for detecting social engineering attacks using vector search",
    version="1.0.0"
)

# CORS middleware (allows frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
qdrant_service = QdrantService()
analyzer_service = AnalyzerService(qdrant_service)
credit_manager = CreditManager()

# Request/Response models
class AnalysisRequest(BaseModel):
    content: str  # The text/message to analyze
    user_address: Optional[str] = None  # User's wallet address

class AnalysisResult(BaseModel):
    threat_score: float  # 0-100, how likely it's a threat
    similarity_score: float  # 0-1, similarity to known patterns
    detected_patterns: List[str]  # List of detected attack patterns
    recommendation: str  # What the user should do
    credits_used: int

class CreditBalance(BaseModel):
    address: str
    balance: int
    tier: str  # free, pro, enterprise

# API Routes

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Social Engineering Analyzer API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    """Detailed health check"""
    qdrant_status = await qdrant_service.check_health()
    return {
        "status": "healthy" if qdrant_status else "degraded",
        "qdrant": "connected" if qdrant_status else "disconnected"
    }

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_content(request: AnalysisRequest):
    """
    Analyze content for social engineering patterns
    
    ELI5: This endpoint takes text you send, converts it to numbers (vectors),
    compares it to known scam patterns, and tells you if it's suspicious.
    """
    try:
        # Check if user has credits (if address provided)
        if request.user_address:
            has_credits = await credit_manager.check_credits(request.user_address)
            if not has_credits:
                raise HTTPException(
                    status_code=402,
                    detail="Insufficient credits. Please top up your account."
                )
        
        # Perform analysis
        result = await analyzer_service.analyze(request.content)
        
        # Deduct credits if address provided
        if request.user_address:
            await credit_manager.deduct_credits(
                request.user_address,
                amount=1  # 1 credit per analysis
            )
        
        return AnalysisResult(
            threat_score=result["threat_score"],
            similarity_score=result["similarity_score"],
            detected_patterns=result["patterns"],
            recommendation=result["recommendation"],
            credits_used=1
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/credits/{address}", response_model=CreditBalance)
async def get_credits(address: str):
    """Get credit balance for a wallet address"""
    balance, tier = await credit_manager.get_balance(address)
    return CreditBalance(
        address=address,
        balance=balance,
        tier=tier
    )

@app.post("/credits/topup")
async def topup_credits(address: str, amount: int):
    """
    Add credits to an account
    Note: In production, this should verify payment on blockchain first
    """
    await credit_manager.add_credits(address, amount)
    return {"message": f"Added {amount} credits to {address}"}

@app.get("/patterns")
async def get_known_patterns():
    """Get list of known attack patterns in database"""
    patterns = await qdrant_service.get_collection_info()
    return {
        "total_patterns": patterns.get("vectors_count", 0),
        "collection_name": "social_engineering_vectors"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


