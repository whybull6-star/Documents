# 🔧 Fix "Failed to fetch" Error

## The Problem
Your frontend can't connect to the backend API. This usually means:
1. Backend server is not running
2. Backend has an error and crashed
3. Wrong API URL

## Quick Fix Steps

### Step 1: Check if Backend is Running

**Open PowerShell and check:**

```powershell
# Check if port 8000 is in use
netstat -ano | findstr :8000
```

**If you see output**, backend is running.  
**If no output**, backend is NOT running - go to Step 2.

---

### Step 2: Start Backend (If Not Running)

**Open PowerShell:**

```powershell
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
venv\Scripts\activate
python app_enhanced.py
```

**Watch for errors!** Common issues:

#### Error: "ModuleNotFoundError: No module named 'web3'"
**Fix:**
```powershell
pip install web3
```

#### Error: "ModuleNotFoundError: No module named 'services.onchain_analyzer'"
**Fix:** The file exists, but Python can't find it. Make sure you're in the `backend` folder.

#### Error: "Connection refused" or Qdrant errors
**Fix:** Check your `.env` file has correct Qdrant Cloud credentials.

---

### Step 3: Test Backend Directly

**Open a NEW PowerShell window and test:**

```powershell
curl http://localhost:8000/health
```

**Or use browser:** Go to http://localhost:8000/health

**You should see JSON response like:**
```json
{
  "status": "healthy",
  "qdrant": "connected",
  ...
}
```

**If this works**, backend is running correctly!

---

### Step 4: Test the Wallet Endpoint

**Test the analyze-wallet endpoint:**

```powershell
curl -X POST http://localhost:8000/analyze-wallet -H "Content-Type: application/json" -d "{\"wallet_address\": \"0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079\"}"
```

**If you get an error**, check the backend terminal for the full error message.

---

### Step 5: Check Frontend API URL

**Make sure frontend is using correct URL:**

1. Open browser console (F12)
2. Go to Network tab
3. Try analyzing a wallet
4. Look at the failed request
5. Check what URL it's trying to reach

**Should be:** `http://localhost:8000/analyze-wallet`

**If it's different**, check your `.env` file in frontend folder.

---

## Common Solutions

### Solution 1: Backend Not Running
**Fix:** Start backend (Step 2 above)

### Solution 2: Missing Dependencies
**Fix:** Install missing packages:
```powershell
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Solution 3: Port Already in Use
**Fix:** Kill the process using port 8000:
```powershell
# Find process ID
netstat -ano | findstr :8000
# Kill it (replace PID with actual number)
taskkill /PID <PID> /F
```

### Solution 4: CORS Error
**Fix:** Backend should already have CORS enabled. If not, check `app_enhanced.py` has:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    ...
)
```

---

## Still Not Working?

1. **Check backend terminal** - what error does it show?
2. **Check browser console** (F12) - what's the exact error?
3. **Check Network tab** - is the request even being sent?

**Share the error messages and I'll help fix it!**

