# 🚨 Emergency Fix - 404 Error

## Quick Fix (Most Common Issue)

### The Problem
404 NOT_FOUND usually means **Root Directory is wrong**.

---

## Fix in 2 Minutes

### Step 1: Fix Vercel (Frontend)

1. **Go to**: https://vercel.com
2. **Select your project**
3. **Settings** → **General**
4. **Root Directory**: Change to `frontend`
5. **Save**
6. **Redeploy** (Deployments → Three dots → Redeploy)

---

### Step 2: Fix Railway (Backend)

1. **Go to**: https://railway.app
2. **Select your service**
3. **Settings** tab
4. **Root Directory**: Change to `backend`
5. **Save**
6. **Wait for redeployment** (2-5 minutes)

---

## Test

**After redeploy:**

1. **Backend**: `https://your-railway-url/health`
2. **Frontend**: `https://your-vercel-url`

**Should work now!** ✅

---

## If Still 404

**Check:**
- Backend Start Command: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
- Environment variables are set
- Services are actually deployed (not just created)

**See**: `FIX_404_ERROR.md` for detailed troubleshooting.

