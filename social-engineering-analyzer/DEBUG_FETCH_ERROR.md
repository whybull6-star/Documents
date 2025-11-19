# Debug "Failed to Fetch" Error - Step by Step

## Step 1: Check Backend is Running

**Open Terminal/CMD and run:**
```bash
curl http://localhost:8000/health
```

**OR in browser, go to:**
```
http://localhost:8000/health
```

**What you should see:**
```json
{
  "status": "healthy",
  "qdrant": "connected",
  "collections": {...}
}
```

**If you get an error:**
- ❌ "Connection refused" → Backend is NOT running
- ❌ "Failed to connect" → Backend is NOT running
- ✅ JSON response → Backend IS running (go to Step 2)

---

## Step 2: Check Frontend API URL

**Check `frontend/next.config.js` or `.env.local`:**

The frontend needs to know where the backend is.

**Should have:**
```javascript
// next.config.js
env: {
  NEXT_PUBLIC_API_URL: 'http://localhost:8000'
}
```

**OR create `frontend/.env.local`:**
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Step 3: Check Browser Console

**Open Browser DevTools:**
1. Press **F12** (or Right-click → Inspect)
2. Click **Console** tab
3. Try the wallet analysis again
4. **Look for red errors**

**Common errors you might see:**

1. **"Failed to fetch" or "Network Error"**
   - Backend is not running OR
   - CORS error OR
   - Wrong API URL

2. **"CORS policy blocked"**
   - Backend CORS not configured (but it should be)

3. **"ERR_CONNECTION_REFUSED"**
   - Backend is not running on port 8000

4. **"ERR_ABORTED" or timeout**
   - Backend is too slow or hanging

**Take a screenshot or copy the exact error message!**

---

## Step 4: Check Backend Logs

**Look at the terminal where backend is running:**

**You should see:**
```
INFO:     127.0.0.1:xxxxx - "POST /analyze-wallet HTTP/1.1" 200 OK
```

**If you see errors:**
- Copy the full error message
- Look for Python tracebacks
- Look for "ERROR:" or "Exception:"

**Common backend errors:**

1. **"Qdrant connection failed"**
   - Qdrant not running
   - Wrong Qdrant URL in `.env`

2. **"RPC connection failed" or "Gnosis RPC error"**
   - Gnosis RPC might be down
   - Wrong RPC URL in `.env`

3. **"Module not found"**
   - Missing Python dependencies
   - Run: `pip install -r requirements.txt`

4. **"Address validation error"**
   - Invalid wallet address format

---

## Step 5: Test Backend Directly

**Open new Terminal and run:**

```bash
curl -X POST "http://localhost:8000/analyze-wallet" \
  -H "Content-Type: application/json" \
  -d "{\"wallet_address\": \"0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb\"}"
```

**OR use PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/analyze-wallet" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"wallet_address": "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"}'
```

**What happens?**

1. **✅ Returns JSON with risk analysis** → Backend works! Problem is frontend connection
2. **❌ Connection refused** → Backend not running
3. **❌ Error message** → Backend error (check the error)

---

## Step 6: Check Network Tab

**In Browser DevTools:**
1. Click **Network** tab (next to Console)
2. Try wallet analysis again
3. **Look for the request** to `/analyze-wallet`
4. **Click on it** to see details

**Check:**
- **Status Code**: 
  - `200 OK` → Request worked (but frontend might have error handling issue)
  - `500` → Backend error (check backend logs)
  - `400` → Bad request (invalid wallet address?)
  - `404` → Endpoint not found
  - `CORS` → CORS error

- **Request URL**: Should be `http://localhost:8000/analyze-wallet`

- **Response**: Click "Response" tab to see what backend returned

---

## Step 7: Quick Fixes

### Fix 1: Backend Not Running

**Start backend:**
```bash
cd backend
python -m uvicorn app_enhanced:app --reload --port 8000
```

**Verify it's running:**
```bash
curl http://localhost:8000/health
```

### Fix 2: Wrong API URL

**Check `frontend/next.config.js`:**
```javascript
module.exports = {
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
    // ...
  }
}
```

**OR create `frontend/.env.local`:**
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**Restart frontend** after changing:
```bash
# Stop frontend (Ctrl+C)
npm run dev
```

### Fix 3: Port Already in Use

**Check what's using port 8000:**
```bash
# Windows:
netstat -ano | findstr :8000

# Mac/Linux:
lsof -i :8000
```

**Kill it if needed:**
```bash
# Windows (use PID from netstat):
taskkill /PID <PID> /F

# Mac/Linux:
kill -9 <PID>
```

### Fix 4: Qdrant Not Running

**If using Docker:**
```bash
docker ps | grep qdrant
# If not running:
docker-compose up -d
```

**If using Qdrant Cloud:**
- Check `.env` has correct `QDRANT_URL` and `QDRANT_API_KEY`

---

## Step 8: What to Tell Me

**When you report the error, tell me:**

1. **Backend running?** (Did `curl http://localhost:8000/health` work?)
2. **Browser Console error:** (Copy exact error from Console tab)
3. **Network tab status:** (What status code for `/analyze-wallet` request?)
4. **Backend terminal errors:** (Any red errors in backend terminal?)
5. **curl test result:** (What did curl to `/analyze-wallet` return?)

---

## Most Common Issue

**90% of the time:** Backend is not running!

**Quick check:**
1. Look at your backend terminal
2. Do you see: `INFO:     Uvicorn running on http://0.0.0.0:8000`?
3. If NO → Start backend!
4. If YES → Check browser console for actual error

---

## Still Not Working?

**Run these commands and share the output:**

```bash
# 1. Check backend health
curl http://localhost:8000/health

# 2. Test backend endpoint
curl -X POST "http://localhost:8000/analyze-wallet" \
  -H "Content-Type: application/json" \
  -d "{\"wallet_address\": \"0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb\"}"

# 3. Check ports
netstat -ano | findstr :8000
netstat -ano | findstr :3000
```

**Copy all outputs and share!**

