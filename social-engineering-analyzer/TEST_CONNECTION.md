# Test Connection - Find the Error

## Quick Test Steps

### 1. Test if Backend is Running

**Open Browser and go to:**
```
http://localhost:8000/health
```

**OR use PowerShell:**
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing
```

**What do you see?**

- ✅ **JSON response** with "status": "healthy" → Backend is working!
- ❌ **Can't connect / Failed to fetch** → Backend is NOT running
- ❌ **404 Not Found** → Wrong URL
- ❌ **Other error** → Copy the error message

---

### 2. Test Wallet Analysis Endpoint Directly

**Open PowerShell and run:**
```powershell
$body = @{
    wallet_address = "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/analyze-wallet" -Method POST -ContentType "application/json" -Body $body
```

**What happens?**

- ✅ **Returns JSON** → Backend endpoint works!
- ❌ **Connection refused** → Backend not running
- ❌ **Error message** → Copy the full error
- ❌ **Timeout** → Backend is too slow (RPC issue)

---

### 3. Check Browser Console

**Steps:**
1. Open your site: http://localhost:3000
2. Press **F12** (opens DevTools)
3. Click **Console** tab (at top)
4. Click **Network** tab (next to Console)
5. Try wallet analysis again
6. Look at **Console** tab for red errors
7. Look at **Network** tab for failed requests

**In Network tab:**
- Find request to `analyze-wallet`
- Click on it
- Check **Status** column
- Click **Response** tab to see what backend returned
- Click **Headers** tab to see request URL

**What's the status code?**
- `200` = Success (but frontend might have error)
- `400` = Bad request (wrong data)
- `500` = Server error (backend crashed)
- `CORS` = CORS error
- `Failed` = Can't connect

---

### 4. Check Backend Terminal

**Look at the terminal where you ran:**
```
python -m uvicorn app_enhanced:app --reload --port 8000
```

**When you click "Analyze Wallet", do you see:**

✅ **Good:**
```
INFO:     127.0.0.1:xxxxx - "POST /analyze-wallet HTTP/1.1" 200 OK
DEBUG: Fetching transactions from block...
```

❌ **Bad (errors):**
```
ERROR: Exception in analyze-wallet: ...
Traceback (most recent call last):
  ...
```

**Copy the full error if you see one!**

---

## Most Common Issues

### Issue 1: Backend Not Running

**Fix:**
```bash
cd backend
python -m uvicorn app_enhanced:app --reload --port 8000
```

**Verify:**
Open: http://localhost:8000/health

---

### Issue 2: Wrong Port

**Check:**
- Frontend is using `http://localhost:8000`?
- Backend is running on port `8000`?

**Check `frontend/next.config.js`:**
```javascript
NEXT_PUBLIC_API_URL: 'http://localhost:8000'
```

---

### Issue 3: CORS Error

**Should be fixed already, but check `backend/app_enhanced.py`:**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Should allow all
    ...
)
```

---

### Issue 4: Backend Error (500)

**Check backend terminal for:**
- Python errors
- Qdrant connection errors
- RPC connection errors

**Common fixes:**
- Qdrant not running: `docker ps | grep qdrant`
- Missing dependencies: `pip install -r requirements.txt`
- Wrong `.env` file: Check `backend/.env`

---

## Tell Me What You See

**Answer these:**

1. **Backend health check** (`http://localhost:8000/health`):
   - ✅ Works → Got JSON response
   - ❌ Fails → Error: [copy error here]

2. **Browser Console** (F12 → Console tab):
   - Error message: [copy exact message]

3. **Network tab** (F12 → Network):
   - Status code: [what number?]
   - Response: [what does it say?]

4. **Backend terminal:**
   - ✅ Shows request → `POST /analyze-wallet HTTP/1.1" 200 OK`
   - ❌ Shows error → [copy full error]

5. **PowerShell test** (step 2 above):
   - ✅ Works → Got response
   - ❌ Fails → Error: [copy error]

---

## Quick Diagnostic Commands

**Run these and share output:**

```powershell
# 1. Check if port 8000 is in use
netstat -ano | findstr :8000

# 2. Check if port 3000 is in use  
netstat -ano | findstr :3000

# 3. Test backend health
Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing

# 4. Check if backend folder exists
Test-Path backend
Test-Path frontend
```

**Copy all outputs and share!**

