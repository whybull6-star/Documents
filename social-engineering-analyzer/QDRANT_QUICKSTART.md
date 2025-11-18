# 🚀 Qdrant Quickstart Guide - Lurantis

Get your Qdrant-powered threat detection system up and running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Docker installed (for running Qdrant)
- Node.js 18+ installed (for frontend)

## Step 1: Start Qdrant (30 seconds)

Open a terminal and run:

```bash
docker run -d -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant
```

**Verify it's running:**
```bash
curl http://localhost:6333/health
```

You should see: `{"status":"ok"}`

## Step 2: Set Up Backend (2 minutes)

### 2.1 Navigate to backend directory
```bash
cd social-engineering-analyzer/backend
```

### 2.2 Create virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Install dependencies
```bash
pip install -r requirements.txt
```

**Note:** First install will download the AI model (~420MB). This is a one-time download.

### 2.4 Create `.env` file
Create a file named `.env` in the `backend/` directory:

```env
QDRANT_URL=http://localhost:6333
API_URL=http://localhost:8000
```

## Step 3: Seed the Database (1 minute)

Populate Qdrant with attack patterns:

```bash
python scripts/seed_enhanced_patterns.py
```

**Expected output:**
```
🚀 Initializing Enhanced Qdrant Service...
📊 Seeding 20 attack patterns across 4 collections...
  ✓ [SIM_SWAPPING] Added pattern #1001
  ✓ [WALLET_STALKING] Added pattern #2001
  ✓ [ADDRESS_SPOOFING] Added pattern #3001
  ...
✅ Database seeded successfully!
📈 Collection Statistics:
   sim_swapping: 5 patterns
   wallet_stalking: 5 patterns
   address_spoofing: 5 patterns
   general_phishing: 5 patterns
```

## Step 4: Start the Backend Server (30 seconds)

```bash
python app_enhanced.py
```

**Expected output:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

The API is now running at `http://localhost:8000`

## Step 5: Test the API (1 minute)

### Test 1: Health Check
```bash
curl http://localhost:8000/health
```

**Expected response:**
```json
{
  "status": "healthy",
  "qdrant": "connected",
  "collections": {
    "sim_swapping": {"vectors_count": 5},
    "wallet_stalking": {"vectors_count": 5},
    ...
  }
}
```

### Test 2: Basic Analysis
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "content": "URGENT: Your wallet has been compromised. Send all funds immediately to 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"
  }'
```

**Expected response:**
```json
{
  "threat_score": 85.5,
  "similarity_score": 0.89,
  "detected_patterns": ["address_spoofing (CRITICAL)", "general_phishing (HIGH)"],
  "recommendation": "⚠️ HIGH RISK: This appears to be a social engineering attack...",
  "credits_used": 1
}
```

### Test 3: Enhanced Analysis with Address Spoofing Detection
```bash
curl -X POST http://localhost:8000/analyze-enhanced \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Your wallet needs verification. Send 0.1 ETH to 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
    "user_address": "0x1234567890123456789012345678901234567890",
    "known_addresses": ["0x742d35Cc6634C0532925a3b844Bc9e7595f0bEa"]
  }'
```

**Expected response:**
```json
{
  "overall_threat_score": 92.3,
  "threat_level": "CRITICAL",
  "detected_attacks": [
    {
      "type": "address_spoofing",
      "severity": "CRITICAL",
      "confidence": 0.9
    }
  ],
  "address_analysis": {
    "is_spoofed": true,
    "similarity_matches": [...],
    "recommendation": "⚠️ HIGH RISK: Address is very similar to your known address..."
  },
  "recommendations": [
    "🚨 CRITICAL THREAT DETECTED: Do NOT interact with this message...",
    "⚠️ Address spoofing detected..."
  ]
}
```

## Step 6: Connect Frontend (Optional)

### 6.1 Update frontend environment
Create/update `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 6.2 Test frontend connection
The frontend should automatically connect to the backend when you run:

```bash
cd ../frontend
npm run dev
```

## 🎯 Quick Test Scenarios

### Test SIM Swapping Detection
```bash
curl -X POST http://localhost:8000/analyze-enhanced \
  -H "Content-Type: application/json" \
  -d '{
    "content": "We need to verify your identity. Please provide your phone number to port your SIM card for security.",
    "context": {"phone": "+1234567890"}
  }'
```

### Test Wallet Stalking Detection
```bash
curl -X POST http://localhost:8000/analyze-enhanced \
  -H "Content-Type: application/json" \
  -d '{
    "content": "I noticed you have a large balance. Want to join my exclusive trading group?",
    "context": {
      "transaction_data": {
        "value": 0.00001,
        "from": "0xUnknownAddress"
      }
    }
  }'
```

## 📊 Verify Everything Works

Run this command to see all your patterns:

```bash
curl http://localhost:8000/patterns
```

You should see:
```json
{
  "collections": {
    "sim_swapping": {"vectors_count": 5},
    "wallet_stalking": {"vectors_count": 5},
    "address_spoofing": {"vectors_count": 5},
    "general_phishing": {"vectors_count": 5}
  },
  "total_patterns": 20
}
```

## 🐛 Troubleshooting

### Qdrant not starting?
```bash
# Check if Docker is running
docker ps

# Check Qdrant logs
docker logs qdrant

# Restart Qdrant
docker restart qdrant
```

### Backend can't connect to Qdrant?
- Make sure Qdrant is running: `curl http://localhost:6333/health`
- Check your `.env` file has `QDRANT_URL=http://localhost:6333`
- Try restarting the backend server

### Model download slow?
- First run downloads ~420MB model
- Subsequent runs use cached model
- Be patient on first run!

### Port 8000 already in use?
```bash
# Find what's using port 8000
# Windows
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :8000

# Or change port in app_enhanced.py
uvicorn.run(app, host="0.0.0.0", port=8001)
```

## ✅ Success Checklist

- [ ] Qdrant is running (`curl http://localhost:6333/health`)
- [ ] Backend dependencies installed
- [ ] Database seeded (20 patterns)
- [ ] Backend server running (`http://localhost:8000`)
- [ ] Health check returns "healthy"
- [ ] Test analysis returns threat scores

## 🚀 Next Steps

1. **Add more patterns**: Edit `backend/scripts/seed_enhanced_patterns.py`
2. **Integrate with frontend**: Connect the analysis UI
3. **Production deployment**: Use Qdrant Cloud for scalability
4. **Monitor performance**: Check `/health` endpoint regularly

## 📚 Additional Resources

- Full setup guide: `backend/QDRANT_SETUP.md`
- API documentation: Visit `http://localhost:8000/docs` (Swagger UI)
- Qdrant docs: https://qdrant.tech/documentation/

## 🎉 You're Done!

Your Qdrant-powered threat detection system is now running! 

**Quick commands reference:**
```bash
# Start Qdrant
docker start qdrant

# Stop Qdrant
docker stop qdrant

# Start backend
cd backend && python app_enhanced.py

# Seed database
cd backend && python scripts/seed_enhanced_patterns.py

# Check health
curl http://localhost:8000/health
```

Need help? Check the troubleshooting section or see `backend/QDRANT_SETUP.md` for detailed documentation.

