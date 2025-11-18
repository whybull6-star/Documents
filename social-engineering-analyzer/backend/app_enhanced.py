"""
Enhanced FastAPI application for Lurantis
Includes comprehensive threat detection with Qdrant
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import os
from dotenv import load_dotenv

from services.enhanced_qdrant_service import EnhancedQdrantService
from services.enhanced_analyzer import EnhancedAnalyzerService
from services.credit_manager import CreditManager
from services.onchain_analyzer import OnChainAnalyzer

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Lurantis API - Social Engineering Detection",
    description="Qdrant-leveraged, AI-powered platform for detecting social engineering attacks",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
qdrant_service = EnhancedQdrantService()
analyzer_service = EnhancedAnalyzerService(qdrant_service)
credit_manager = CreditManager()

# Initialize on-chain analyzer (lazy initialization to prevent startup errors)
gnosis_rpc = os.getenv("GNOSIS_RPC_URL", "https://rpc.gnosischain.com")
onchain_analyzer = None

def get_onchain_analyzer():
    """Get or create on-chain analyzer instance"""
    global onchain_analyzer
    if onchain_analyzer is None:
        try:
            onchain_analyzer = OnChainAnalyzer(qdrant_service, gnosis_rpc)
        except Exception as e:
            print(f"Warning: Failed to initialize OnChainAnalyzer: {e}")
            raise HTTPException(status_code=500, detail=f"On-chain analyzer initialization failed: {str(e)}")
    return onchain_analyzer

# Request/Response models
class AnalysisRequest(BaseModel):
    content: str
    user_address: Optional[str] = None

class EnhancedAnalysisRequest(BaseModel):
    content: str
    user_address: Optional[str] = None
    known_addresses: Optional[List[str]] = None
    context: Optional[Dict] = None

class AnalysisResult(BaseModel):
    threat_score: float
    similarity_score: float
    detected_patterns: List[str]
    recommendation: str
    credits_used: int

class EnhancedAnalysisResult(BaseModel):
    overall_threat_score: float
    threat_level: str
    detected_attacks: List[Dict]
    recommendations: List[str]
    address_analysis: Optional[Dict] = None
    sim_swap_analysis: Optional[Dict] = None
    wallet_stalking_analysis: Optional[Dict] = None
    detailed_analysis: Dict

class CreditBalance(BaseModel):
    address: str
    balance: int
    tier: str

# API Routes

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Lurantis API - Social Engineering Detection",
        "status": "running",
        "version": "2.0.0",
        "features": [
            "SIM Swapping Detection",
            "Wallet Stalking Detection",
            "Address Spoofing Detection",
            "General Phishing Detection"
        ]
    }

@app.get("/health")
async def health():
    """Detailed health check"""
    qdrant_status = await qdrant_service.check_health()
    stats = await qdrant_service.get_collection_stats()
    
    return {
        "status": "healthy" if qdrant_status else "degraded",
        "qdrant": "connected" if qdrant_status else "disconnected",
        "collections": stats
    }

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_content(request: AnalysisRequest):
    """
    Basic analysis endpoint (backward compatible)
    """
    try:
        # Check credits if address provided
        if request.user_address:
            has_credits = await credit_manager.check_credits(request.user_address)
            if not has_credits:
                raise HTTPException(
                    status_code=402,
                    detail="Insufficient credits. Please subscribe to continue."
                )
        
        # Perform analysis
        result = await analyzer_service.analyze_simple(request.content)
        
        # Deduct credits if address provided
        if request.user_address:
            await credit_manager.deduct_credits(
                request.user_address,
                amount=1
            )
        
        return AnalysisResult(
            threat_score=result["threat_score"],
            similarity_score=result["similarity_score"],
            detected_patterns=result["patterns"],
            recommendation=result["recommendation"],
            credits_used=1
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-enhanced", response_model=EnhancedAnalysisResult)
async def analyze_enhanced(request: EnhancedAnalysisRequest):
    """
    Enhanced analysis with comprehensive threat detection
    
    Features:
    - SIM swapping detection
    - Wallet stalking detection
    - Address spoofing detection
    - Multi-vector pattern matching
    """
    try:
        # Check credits if address provided
        if request.user_address:
            has_credits = await credit_manager.check_credits(request.user_address)
            if not has_credits:
                raise HTTPException(
                    status_code=402,
                    detail="Insufficient credits. Please subscribe to continue."
                )
        
        # Perform comprehensive analysis
        result = await analyzer_service.analyze_comprehensive(
            content=request.content,
            user_address=request.user_address,
            known_addresses=request.known_addresses,
            context=request.context
        )
        
        # Deduct credits if address provided
        if request.user_address:
            await credit_manager.deduct_credits(
                request.user_address,
                amount=1
            )
        
        return EnhancedAnalysisResult(**result)
    
    except HTTPException:
        raise
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

@app.get("/patterns")
async def get_patterns():
    """Get statistics about attack patterns in database"""
    stats = await qdrant_service.get_collection_stats()
    return {
        "collections": stats,
        "total_patterns": sum(
            stat.get("vectors_count", 0) 
            for stat in stats.values() 
            if "error" not in stat
        )
    }

@app.post("/detect-address-spoofing")
async def detect_address_spoofing(
    suspicious_address: str,
    known_addresses: List[str]
):
    """
    Detect if an address is a spoofed version of known addresses
    """
    try:
        result = await qdrant_service.detect_address_spoofing(
            suspicious_address,
            known_addresses
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# On-chain wallet analysis endpoints
class WalletAnalysisRequest(BaseModel):
    wallet_address: str
    user_address: Optional[str] = None
    include_transactions: bool = True

class WalletCompareRequest(BaseModel):
    wallet1: str
    wallet2: str
    user_address: Optional[str] = None

@app.post("/analyze-wallet")
async def analyze_wallet(request: WalletAnalysisRequest):
    """
    High-level on-chain wallet analysis
    
    Analyzes:
    - Wallet balance and activity
    - Transaction patterns
    - Behavioral clusters
    - Risk assessment
    - Anomaly detection
    """
    try:
        if request.user_address:
            has_credits = await credit_manager.check_credits(request.user_address)
            if not has_credits:
                raise HTTPException(status_code=402, detail="Insufficient credits.")
        
        analyzer = get_onchain_analyzer()
        result = await analyzer.analyze_wallet_activity(
            request.wallet_address,
            block_range=None
        )
        
        if request.user_address:
            await credit_manager.deduct_credits(request.user_address, amount=1)
        
        return {
            **result,
            "credits_used": 1
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/compare-wallets")
async def compare_wallets(request: WalletCompareRequest):
    """
    Compare two wallets to find similarities and relationships
    """
    try:
        if request.user_address:
            has_credits = await credit_manager.check_credits(request.user_address)
            if not has_credits:
                raise HTTPException(status_code=402, detail="Insufficient credits.")
        
        analyzer = get_onchain_analyzer()
        result = await analyzer.detect_wallet_cluster([
            request.wallet1,
            request.wallet2
        ])
        
        if request.user_address:
            await credit_manager.deduct_credits(request.user_address, amount=1)
        
        return {
            **result,
            "credits_used": 1
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/trace-transaction-flow")
async def trace_transaction_flow(
    wallet_address: str,
    depth: int = 2,
    user_address: Optional[str] = None
):
    """
    Trace transaction flow from a wallet
    Shows where funds come from and go to
    """
    try:
        if user_address:
            has_credits = await credit_manager.check_credits(user_address)
            if not has_credits:
                raise HTTPException(status_code=402, detail="Insufficient credits.")
        
        analyzer = get_onchain_analyzer()
        result = await analyzer.trace_transaction_flow(
            wallet_address,
            depth=depth
        )
        
        if user_address:
            await credit_manager.deduct_credits(user_address, amount=1)
        
        return {
            **result,
            "credits_used": 1
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

