# 🔧 Fix 404 NOT_FOUND Error - Quick Guide

## Common Causes & Fixes

### Issue 1: Vercel 404 - Root Directory Wrong

**Problem:** Vercel is looking in the wrong folder.

**Fix:**
1. Go to Vercel dashboard
2. Select your project
3. Go to **Settings** → **General**
4. Find **Root Directory**
5. Change to: `frontend`
6. **Save**
7. **Redeploy** (Deployments → Three dots → Redeploy)

---

### Issue 2: Railway 404 - Root Directory Wrong

**Problem:** Railway is looking in the wrong folder.

**Fix:**
1. Go to Railway dashboard
2. Select your service
3. Go to **Settings** tab
4. Find **Root Directory**
5. Change to: `backend`
6. **Save**
7. Wait for redeployment

---

### Issue 3: Backend Not Running

**Problem:** Backend service crashed or didn't start.

**Fix:**
1. Go to Railway dashboard
2. Select your service
3. Go to **Deployments** tab
4. Check **logs** for errors
5. Common issues:
   - Missing environment variables
   - Wrong start command
   - Port not set correctly

**Check Start Command:**
- Should be: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`

---

### Issue 4: Missing Environment Variables

**Problem:** Backend can't connect to Qdrant or missing config.

**Fix:**
1. Go to Railway → **Variables** tab
2. Make sure you have:
   - `QDRANT_URL`
   - `QDRANT_API_KEY` (if using Cloud)
   - `GNOSIS_RPC_URL`
3. **Redeploy** after adding variables

---

### Issue 5: Frontend Can't Find Backend

**Problem:** Frontend API URL is wrong.

**Fix:**
1. Go to Vercel dashboard
2. **Settings** → **Environment Variables**
3. Check `NEXT_PUBLIC_API_URL`
4. Should be: `https://your-railway-url.up.railway.app`
5. **Redeploy** frontend

---

## Quick Diagnostic Steps

### Step 1: Check Backend is Running

**Visit:** `https://your-railway-url.up.railway.app/health`

**Should see:**
```json
{
  "status": "healthy",
  "qdrant": "connected"
}
```

**If 404:**
- Backend not deployed correctly
- Check Railway logs
- Verify Root Directory is `backend`

---

### Step 2: Check Frontend Build

**In Vercel:**
1. Go to **Deployments** tab
2. Click on latest deployment
3. Check **Build Logs**
4. Look for errors

**Common errors:**
- `Module not found` → Missing dependencies
- `Build failed` → Check `package.json`

---

### Step 3: Check API Docs

**Visit:** `https://your-railway-url.up.railway.app/docs`

**Should see:**
- FastAPI Swagger UI
- List of endpoints

**If 404:**
- Backend not running
- Check Railway deployment

---

## Emergency Fix: Redeploy Everything

### Backend (Railway):
1. Go to Railway
2. **Deployments** → **Three dots** → **Redeploy**
3. Wait 2-5 minutes

### Frontend (Vercel):
1. Go to Vercel
2. **Deployments** → **Three dots** → **Redeploy**
3. Wait 1-2 minutes

---

## Still Not Working?

**Check these:**

1. **Backend URL correct?**
   - Get from Railway → Settings → Domains
   - Should be: `https://xxxxx.up.railway.app`

2. **Frontend URL correct?**
   - Get from Vercel dashboard
   - Should be: `https://xxxxx.vercel.app`

3. **Environment variables set?**
   - Vercel: `NEXT_PUBLIC_API_URL`
   - Railway: `QDRANT_URL`, `GNOSIS_RPC_URL`

4. **Root directories correct?**
   - Vercel: `frontend`
   - Railway: `backend`

---

## Quick Test URLs

**Test these in order:**

1. **Backend Health**: `https://your-railway-url/health`
2. **Backend Docs**: `https://your-railway-url/docs`
3. **Frontend**: `https://your-vercel-url`

**If all return 404:**
- Services not deployed
- Need to deploy first

**If backend works but frontend 404:**
- Frontend build issue
- Check Vercel build logs

---

## Most Common Fix

**90% of 404 errors = Wrong Root Directory**

**Vercel:** Must be `frontend`  
**Railway:** Must be `backend`

**Fix it and redeploy!** ✅

