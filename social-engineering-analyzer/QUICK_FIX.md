# ⚡ Quick Fix: "Failed to fetch" Error

## The Problem
Your frontend can't connect to the backend API.

## Solution (3 Steps)

### Step 1: Check if Backend is Running

**Look at your backend terminal** - do you see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ If YES** → Go to Step 3  
**❌ If NO** → Go to Step 2

---

### Step 2: Start Backend

**In PowerShell:**

```powershell
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
venv\Scripts\activate
python app_enhanced.py
```

**Watch for errors!** Common ones:

**Error: "ModuleNotFoundError: No module named 'web3'"**
```powershell
pip install web3
```

**Error: "No module named 'services.onchain_analyzer'"**
- Make sure you're in the `backend` folder
- The file should exist at: `backend/services/onchain_analyzer.py`

**Any other error?** → Copy the full error message and share it!

---

### Step 3: Test Backend in Browser

**Open browser and go to:**
```
http://localhost:8000/health
```

**You should see JSON like:**
```json
{"status": "healthy", "qdrant": "connected", ...}
```

**✅ If you see this** → Backend is working!  
**❌ If you see "Can't reach this page"** → Backend is not running (go back to Step 2)

---

### Step 4: Try Frontend Again

1. **Refresh your browser** (F5)
2. **Try analyzing a wallet again**
3. **Check browser console** (F12) for errors

---

## Still Not Working?

**Check these:**

1. **Backend terminal** - Any error messages?
2. **Browser console** (F12) - What's the exact error?
3. **Network tab** (F12) - Is the request being sent?

**Most common issue:** Backend not running or crashed on startup.

**Share the error message from backend terminal and I'll help fix it!**

