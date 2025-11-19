# Run Lurantis Locally

## Quick Start (Local Development)

### Step 1: Start Backend

**Open Terminal/CMD (Backend):**

```bash
cd backend

# Activate virtual environment (if you have one)
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Make sure Qdrant is running
# If using Docker:
docker ps | grep qdrant
# If not running:
docker-compose up -d

# Start backend
python -m uvicorn app_enhanced:app --reload --host 0.0.0.0 --port 8000
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**Keep this terminal open!**

---

### Step 2: Start Frontend

**Open NEW Terminal/CMD (Frontend):**

```bash
cd frontend

# Install dependencies (if not done)
npm install

# Start frontend
npm run dev
```

**You should see:**
```
  ▲ Next.js 14.x.x
  - Local:        http://localhost:3000
  - ready started server on 0.0.0.0:3000
```

**Keep this terminal open!**

---

### Step 3: Open in Browser

Open: **http://localhost:3000**

You should see the Lurantis landing page!

---

## Test Wallet Analysis

1. **Scroll down** to "On-Chain Wallet Analysis" section
2. **Enter a wallet address** (e.g., `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb`)
3. **Click "🔍 Analyze Wallet"**
4. **Wait a few seconds** (it fetches real transactions)
5. **See results** with risk score, patterns, etc.

---

## Troubleshooting

### Backend won't start?

**Check:**
- Python 3.8+ installed? `python --version`
- Dependencies installed? `pip install -r requirements.txt`
- Qdrant running? `docker ps | grep qdrant` or check Qdrant Cloud

**Common errors:**

1. **"Module not found"**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **"Qdrant connection failed"**
   - If using Docker: `docker-compose up -d`
   - If using Qdrant Cloud: Check `.env` has `QDRANT_URL` and `QDRANT_API_KEY`

3. **"Port 8000 already in use"**
   ```bash
   # Kill process on port 8000
   # Windows:
   netstat -ano | findstr :8000
   taskkill /PID <PID> /F
   # Mac/Linux:
   lsof -ti:8000 | xargs kill
   ```

### Frontend won't start?

**Check:**
- Node.js installed? `node --version`
- Dependencies installed? `cd frontend && npm install`

**Common errors:**

1. **"Port 3000 already in use"**
   ```bash
   # Kill process on port 3000
   # Windows:
   netstat -ano | findstr :3000
   taskkill /PID <PID> /F
   # Mac/Linux:
   lsof -ti:3000 | xargs kill
   ```

2. **"Failed to fetch" in browser**
   - Is backend running on port 8000?
   - Check `frontend/.env.local` or `frontend/next.config.js` has correct API URL
   - Default should be: `http://localhost:8000`

---

## Environment Setup

### Backend `.env` file

Create `backend/.env`:
```env
GNOSIS_RPC_URL=https://rpc.gnosischain.com
QDRANT_URL=http://localhost:6333
# OR for Qdrant Cloud:
# QDRANT_URL=https://your-cluster.qdrant.io
# QDRANT_API_KEY=your-api-key
```

### Frontend `.env.local` (optional)

Create `frontend/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_GNOSIS_RPC=https://rpc.gnosischain.com
```

---

## Check Everything is Working

### 1. Backend Health Check

```bash
curl http://localhost:8000/health
```

Should return:
```json
{
  "status": "healthy",
  "qdrant": "connected",
  "collections": {...}
}
```

### 2. Frontend Check

Open: http://localhost:3000

Should show the landing page with:
- ✅ Hero section
- ✅ Wallet Analysis section
- ✅ Features
- ✅ How It Works
- ✅ Pricing
- ✅ CTA
- ✅ Footer

### 3. Test Wallet Analysis

1. Go to http://localhost:3000
2. Scroll to "On-Chain Wallet Analysis"
3. Enter: `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb`
4. Click "Analyze Wallet"
5. Should show results with risk score

---

## Quick Commands Summary

**Terminal 1 (Backend):**
```bash
cd backend
python -m uvicorn app_enhanced:app --reload --port 8000
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

**Browser:**
- Open: http://localhost:3000

---

## Next Steps (After Local Testing)

Once everything works locally:

1. **Commit to Git**
2. **Push to GitHub**
3. **Deploy to Vercel** (frontend)
4. **Deploy to Railway** (backend)

See `DEPLOY_NOW.md` for deployment steps!

