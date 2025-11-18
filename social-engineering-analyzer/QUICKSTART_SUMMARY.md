# ⚡ Lurantis Quickstart - At a Glance

## 🎯 What You're Building

A **Qdrant-powered threat detection system** that identifies:
- ✅ SIM swapping attempts
- ✅ Wallet stalking patterns  
- ✅ Address spoofing (similar-looking wallet addresses)
- ✅ General phishing attacks

## 🚀 5-Minute Setup

```bash
# 1. Start Qdrant
docker run -d -p 6333:6333 --name qdrant qdrant/qdrant

# 2. Setup backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Create .env file
echo "QDRANT_URL=http://localhost:6333" > .env

# 4. Seed database
python scripts/seed_enhanced_patterns.py

# 5. Start server
python app_enhanced.py
```

## ✅ Verify It Works

```bash
# Health check
curl http://localhost:8000/health

# Test analysis
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"content": "URGENT: Your wallet is compromised. Send funds to 0x..."}'
```

## 📚 Full Guide

👉 **[QDRANT_QUICKSTART.md](./QDRANT_QUICKSTART.md)** - Complete step-by-step guide

## 🎓 What Happens Behind the Scenes

1. **Text → Vector**: Your message is converted to numbers (768 dimensions)
2. **Search**: Qdrant finds similar attack patterns in milliseconds
3. **Analyze**: System checks for SIM swapping, wallet stalking, address spoofing
4. **Alert**: Returns threat score (0-100) and recommendations

## 🔥 Key Features

- **Multi-Collection Search**: Searches across 4 specialized attack pattern databases
- **Address Spoofing Detection**: Character-by-character comparison of wallet addresses
- **Real-Time Analysis**: < 10ms response time
- **Actionable Recommendations**: Tells users exactly what to do

## 📊 API Endpoints

- `POST /analyze` - Basic threat analysis
- `POST /analyze-enhanced` - Full analysis with all features
- `POST /detect-address-spoofing` - Dedicated address spoofing check
- `GET /health` - System health check
- `GET /patterns` - Database statistics

## 🐛 Troubleshooting

**Qdrant not starting?**
```bash
docker ps  # Check if running
docker logs qdrant  # Check logs
```

**Backend can't connect?**
- Verify Qdrant: `curl http://localhost:6333/health`
- Check `.env` file has correct URL

**Need more help?**
👉 See [QDRANT_QUICKSTART.md](./QDRANT_QUICKSTART.md) troubleshooting section

---

**Ready to go?** Follow the full guide: [QDRANT_QUICKSTART.md](./QDRANT_QUICKSTART.md)

