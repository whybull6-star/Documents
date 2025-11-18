# 🚀 Final Deployment Guide - Push to Git & Deploy

Complete step-by-step guide to push your code to GitHub and deploy to Vercel + Railway.

---

## PART 1: Final Git Push

### Step 1: Open Command Prompt

1. Press `Windows Key`
2. Type `cmd`
3. Press `Enter`

### Step 2: Navigate to Project

```cmd
cd C:\Users\valoo\Documents\social-engineering-analyzer
```

### Step 3: Check Status

```cmd
git status
```

**You should see all your new files listed.**

### Step 4: Add All Changes

```cmd
git add .
```

### Step 5: Commit Changes

```cmd
git commit -m "Final updates: Enhanced UI with organic blobs, network overlays, high-level documentation language, sourced attack patterns, and polished design"
```

### Step 6: Push to GitHub

```cmd
git push origin main
```

**If asked for credentials:**
- Username: Your GitHub username
- Password: Use Personal Access Token (not password)

**✅ Code is now on GitHub!**

---

## PART 2: Deploy Frontend to Vercel

### Step 7: Go to Vercel

1. Open browser: https://vercel.com
2. Sign in with GitHub (if not already)

### Step 8: Import Repository

1. Click **"Add New Project"** (or "Import Project")
2. Find **`lurantis`** (or your repo name)
3. Click **"Import"**

### Step 9: Configure Project

**IMPORTANT SETTINGS:**

1. **Project Name**: `lurantis` (or keep default)

2. **Root Directory**: 
   - Click **"Edit"** next to Root Directory
   - Type: `frontend`
   - Click **"Continue"**

3. **Framework Preset**: Should auto-detect "Next.js"

4. **Build Command**: Leave default (`npm run build`)

5. **Output Directory**: Leave default (`.next`)

### Step 10: Add Environment Variables

**Before clicking "Deploy", add these:**

Click **"Environment Variables"** and add:

1. **`NEXT_PUBLIC_API_URL`**
   - Value: `http://localhost:8000` (we'll update after backend deploys)
   - Environments: ✅ Production, ✅ Preview, ✅ Development

2. **`NEXT_PUBLIC_CONTRACT_ADDRESS`**
   - Value: Your contract address (if you have one)
   - Environments: ✅ Production, ✅ Preview, ✅ Development

3. **`NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`**
   - Value: Your subscription contract address (if you have one)
   - Environments: ✅ Production, ✅ Preview, ✅ Development

4. **`NEXT_PUBLIC_GNOSIS_RPC`**
   - Value: `https://rpc.gnosischain.com`
   - Environments: ✅ Production, ✅ Preview, ✅ Development

**Click "Add" for each variable.**

### Step 11: Deploy Frontend

1. Click **"Deploy"** button
2. Wait 1-3 minutes for build
3. You'll see: ✅ **"Ready"**

**Your frontend URL:** `https://lurantis-xxxxx.vercel.app`

**✅ Frontend is LIVE!**

---

## PART 3: Deploy Backend to Railway

### Step 12: Go to Railway

1. Open browser: https://railway.app
2. Sign in with GitHub

### Step 13: Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Find and select **`lurantis`** repository
4. Click **"Deploy Now"**

### Step 14: Configure Backend

1. **Click on the service** (named after your repo)

2. **Go to "Settings" tab**

3. **Set Root Directory**:
   - Find "Root Directory"
   - Click **"Edit"**
   - Type: `backend`
   - Click **"Save"**

4. **Set Start Command**:
   - Find "Start Command"
   - Click **"Edit"**
   - Type:
     ```
     uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT
     ```
   - Click **"Save"**

### Step 15: Add Environment Variables (Backend)

**Go to "Variables" tab** and add:

1. **`QDRANT_URL`**
   - Value: Your Qdrant Cloud URL
     - Example: `https://xxxxx-xxxxx-xxxxx.qdrant.io`
   - Or: `http://localhost:6333` if using local Qdrant

2. **`QDRANT_API_KEY`** (if using Qdrant Cloud)
   - Value: Your Qdrant API key
   - Get from: https://cloud.qdrant.io

3. **`GNOSIS_RPC_URL`**
   - Value: `https://rpc.gnosischain.com`

**Click "Add" for each variable.**

### Step 16: Wait for Deployment

1. **Go to "Deployments" tab**
2. **Watch build logs**
3. **Wait for**: ✅ **"Deploy successful"**
4. **Takes 2-5 minutes**

### Step 17: Get Backend URL

1. **Go to "Settings" tab**
2. **Scroll to "Domains" section**
3. **You'll see**: `https://lurantis-production-xxxx.up.railway.app`
4. **Copy this URL!** This is your backend API URL.

**✅ Backend is LIVE!**

---

## PART 4: Connect Frontend to Backend

### Step 18: Update Frontend Environment Variable

1. **Go back to Vercel** (vercel.com)
2. **Select your `lurantis` project**
3. **Go to "Settings" → "Environment Variables"**
4. **Find `NEXT_PUBLIC_API_URL`**
5. **Click three dots** (⋮) → **"Edit"**
6. **Change value to**: Your Railway backend URL
   - Example: `https://lurantis-production-xxxx.up.railway.app`
7. **Click "Save"**

### Step 19: Redeploy Frontend

1. **Go to "Deployments" tab** in Vercel
2. **Click three dots** (⋮) on latest deployment
3. **Click "Redeploy"**
4. **Click "Redeploy" again** (confirm)
5. **Wait 1-2 minutes**

**✅ Frontend now connected to backend!**

---

## PART 5: Test Everything

### Step 20: Test Frontend

1. **Go to your Vercel URL**: `https://lurantis-xxxxx.vercel.app`
2. **Check if site loads**
3. **Try connecting wallet**
4. **Scroll through sections**
5. **Check if API Docs link works** (in footer)

### Step 21: Test Backend API

1. **Go to**: `https://your-railway-url.up.railway.app/docs`
2. **You should see FastAPI Swagger UI**
3. **Test `/health` endpoint**:
   - Click on `/health`
   - Click "Try it out"
   - Click "Execute"
   - Should return: `{"status": "healthy", ...}`

### Step 22: Test Wallet Analysis

1. **Go to your Vercel site**
2. **Scroll to "Wallet Analysis" section**
3. **Enter a wallet address**: `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`
4. **Click "Analyze Wallet"**
5. **Should show analysis results**

**✅ Everything working!**

---

## PART 6: Make Accessible to Judges

### Step 23: Get Your URLs

**After deployment, you'll have:**

- **Frontend**: `https://lurantis-xxxxx.vercel.app`
- **Backend API**: `https://lurantis-production-xxxx.up.railway.app`
- **API Docs**: `https://lurantis-production-xxxx.up.railway.app/docs`

### Step 24: Share with Judges

**Provide judges with:**

1. **Frontend URL** (main site)
2. **API Documentation URL** (for technical review)
3. **GitHub Repository** (for code review)

**Example submission:**
```
Frontend: https://lurantis-xxxxx.vercel.app
API Docs: https://lurantis-production-xxxx.up.railway.app/docs
GitHub: https://github.com/YOUR_USERNAME/lurantis
```

---

## Troubleshooting

### Git Push Fails

**Error: "Authentication failed"**
- Use Personal Access Token instead of password
- Create token: GitHub → Settings → Developer settings → Personal access tokens

**Error: "Repository not found"**
- Check repository name is correct
- Make sure you're using the right GitHub username

---

### Vercel Build Fails

**Error: "Module not found"**
- Make sure Root Directory is set to `frontend`
- Check `package.json` has all dependencies

**Error: "Build command failed"**
- Check build logs in Vercel
- Make sure all environment variables are set

---

### Railway Deployment Fails

**Error: "No module named 'xxx'"**
- Make sure Root Directory is set to `backend`
- Check `requirements.txt` has all dependencies

**Error: "Port already in use"**
- Make sure Start Command uses `$PORT` variable
- Railway assigns port automatically

---

### Frontend Can't Connect to Backend

**Error: "Failed to fetch"**
- Check `NEXT_PUBLIC_API_URL` is correct in Vercel
- Check backend is actually running (visit Railway URL)
- Check CORS settings in backend (should allow `*` for now)

**API Docs link doesn't work**
- Make sure backend is deployed
- Check backend URL is correct
- Visit backend URL directly: `https://your-backend-url/docs`

---

## Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Frontend deployed to Vercel (root: `frontend`)
- [ ] Backend deployed to Railway (root: `backend`)
- [ ] Environment variables set in both
- [ ] Frontend connected to backend
- [ ] Site tested and working
- [ ] API Docs accessible
- [ ] Wallet analysis working

---

## Final URLs Reference

After deployment, save these:

**Frontend:**
```
https://lurantis-xxxxx.vercel.app
```

**Backend API:**
```
https://lurantis-production-xxxx.up.railway.app
```

**API Documentation:**
```
https://lurantis-production-xxxx.up.railway.app/docs
```

**GitHub Repository:**
```
https://github.com/YOUR_USERNAME/lurantis
```

---

## For Judges Submission

**Provide this information:**

1. **Live Demo**: [Your Vercel URL]
2. **API Documentation**: [Your Railway /docs URL]
3. **Source Code**: [Your GitHub URL]
4. **Technical Stack**:
   - Frontend: Next.js 14, React, Tailwind CSS
   - Backend: FastAPI, Python
   - Database: Qdrant Vector Database
   - Blockchain: Gnosis Chain (EVM-compatible)
   - Vector Model: all-mpnet-base-v2 (768 dimensions)

---

## 🎉 Done!

**Your site is now:**
- ✅ Live on Vercel
- ✅ Backend on Railway
- ✅ Accessible to judges
- ✅ Fully functional

**Share the URLs and you're ready for judging!** 🚀
