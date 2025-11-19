# Deploy Lurantis for Judges - Complete Guide

## Overview

This guide walks you through:
1. ✅ Gathering all Qdrant proof/data
2. ✅ Pushing to GitHub (for judges to access)
3. ✅ Deploying frontend to Vercel
4. ✅ Deploying backend to Railway
5. ✅ Making it accessible for judges

---

## PART 1: Gather Qdrant Proof for Pitch Deck

### Files to Include:

1. **Qdrant Proof Documents:**
   - `QDRANT_PITCH_DECK_PROOF.md` ← **Main proof document**
   - `QDRANT_PROOF.md` ← Complete technical proof
   - `QDRANT_USAGE.md` ← Usage documentation
   - `DATA_SOURCES_PROOF.md` ← Source verification

2. **Data Files:**
   - `backend/data/attack_patterns.json` ← JSON database
   - `backend/scripts/seed_enhanced_patterns.py` ← All 33 patterns
   - `PITCH_DECK_QDRANT_DATA.json` ← Formatted for pitch deck

3. **Code Files (for screenshots):**
   - `backend/services/enhanced_qdrant_service.py` ← Core Qdrant service
   - `backend/services/onchain_analyzer.py` ← Wallet analysis using Qdrant
   - `backend/app_enhanced.py` ← API endpoints

**These files are ready!** Just include them in your pitch deck.

---

## PART 2: Push to GitHub (For Judges)

### Step 1: Prepare for Push

**Make sure everything is ready:**

1. ✅ Code is working locally
2. ✅ All files committed
3. ✅ No sensitive data in code (API keys, etc.)
4. ✅ `.env` files in `.gitignore`

### Step 2: Check Git Status

**In Command Prompt:**

```cmd
cd Documents\social-engineering-analyzer
git status
```

**You should see list of files**

---

### Step 3: Stage All Files

**Using GitHub Desktop:**

1. **Open GitHub Desktop**
2. **Select repository**: `whybull6-star/lurantis` (if exists)
   - **OR** create new repository first (see below)

3. **In "Changes" tab:**
   - All files should show as "new" or "modified"
   - All should be checked (staged)

4. **If files not staged:**
   - Check all files manually
   - OR click "Select all" if available

---

### Step 4: Write Commit Message

**Bottom left of GitHub Desktop:**

**Summary (required):**
```
Final deployment: Qdrant integration, wallet analysis, enhanced UI, Gnosis Chain
```

**Description (optional):**
```
- Complete Qdrant vector search implementation (33 patterns, 5 collections)
- Real transaction history analysis from Gnosis Chain
- Enhanced UI with animations and organic blobs
- Wallet risk assessment using semantic similarity
- All attack patterns sourced from FBI IC3, CISA, Ethereum Foundation
```

---

### Step 5: Commit

**Click "Commit to main" button**

**Wait for commit to complete**

---

### Step 6: Push to GitHub

**Click "Publish branch" or "Push origin" button**

**Wait for push to complete**

**Verify:**
- Go to: https://github.com/whybull6-star/lurantis
- Should see all your files
- Should see latest commit

---

### Alternative: Create New Repository

**If repository doesn't exist:**

1. **Go to:** https://github.com/new
2. **Repository name:** `lurantis`
3. **Visibility:** Public (for judges to access)
4. **Description:** "Qdrant-leveraged, AI-powered social engineering detection platform"
5. **Click "Create repository"**

**Then in GitHub Desktop:**

1. **File → Add Local Repository**
2. **Browse to:** `C:\Users\valoo\Documents\social-engineering-analyzer`
3. **Click "Add repository"**
4. **Publish to GitHub**
5. **Select:** `whybull6-star/lurantis`
6. **Click "Publish Repository"**

---

## PART 3: Deploy Frontend to Vercel

### Step 1: Go to Vercel

**Open:** https://vercel.com

**Sign in with GitHub**

---

### Step 2: Import Project

1. **Click "Add New Project"** (or "Import Project")

2. **Select Repository:**
   - Find `whybull6-star/lurantis`
   - Click "Import"

---

### Step 3: Configure Project

**Project Settings:**

1. **Project Name:** `lurantis` (or whatever you want)

2. **Root Directory:** 
   - Click "Edit"
   - Set to: `frontend`
   - Click "Continue"

3. **Framework Preset:** 
   - Should auto-detect: "Next.js"
   - Leave as is

4. **Build Command:**
   - Should be: `npm run build`
   - Leave as is

5. **Output Directory:**
   - Should be: `.next`
   - Leave as is

6. **Install Command:**
   - Should be: `npm install`
   - Leave as is

**Click "Continue"**

---

### Step 4: Add Environment Variables

**Add these variables:**

1. **`NEXT_PUBLIC_API_URL`**
   - Value: `https://your-backend-url.up.railway.app` (update after backend deploys)
   - **For now:** `http://localhost:8000` (we'll update later)

2. **`NEXT_PUBLIC_GNOSIS_RPC`**
   - Value: `https://rpc.gnosischain.com`

3. **`NEXT_PUBLIC_CONTRACT_ADDRESS`** (if you have one)
   - Value: Your deployed contract address

4. **`NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`** (if you have one)
   - Value: Your subscription contract address

**Click "Deploy"**

---

### Step 5: Wait for Deployment

**Vercel will:**
1. Clone your repo
2. Install dependencies
3. Build the project
4. Deploy

**Wait 2-3 minutes**

**You should see:**
- ✅ "Building..."
- ✅ "Deployed"

**Copy your Vercel URL:**
- `https://lurantis-xxxxx.vercel.app`

---

### Step 6: Update Environment Variables (After Backend)

**After backend is deployed (Part 4):**

1. **Go to:** Vercel Dashboard → Your Project → Settings → Environment Variables
2. **Edit** `NEXT_PUBLIC_API_URL`
3. **Change to:** Your Railway backend URL
4. **Save**
5. **Go to:** Deployments tab → Click "..." → "Redeploy"

---

## PART 4: Deploy Backend to Railway

### Step 1: Go to Railway

**Open:** https://railway.app

**Sign in with GitHub**

---

### Step 2: Create New Project

1. **Click "New Project"**

2. **Select "Deploy from GitHub repo"**

3. **Select:** `whybull6-star/lurantis`

4. **Click "Deploy"**

---

### Step 3: Configure Project

1. **Click on your project**

2. **Set Root Directory:**
   - Click "Settings" tab
   - **Root Directory:** Set to `backend`
   - Save

3. **Set Start Command:**
   - Click "Settings" tab
   - **Start Command:** `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
   - Save

---

### Step 4: Add Environment Variables

**Click "Variables" tab**

**Add these:**

1. **`QDRANT_URL`**
   - Value: Your Qdrant Cloud URL
   - Example: `https://your-cluster.qdrant.io`

2. **`QDRANT_API_KEY`**
   - Value: Your Qdrant API key

3. **`GNOSIS_RPC_URL`**
   - Value: `https://rpc.gnosischain.com`

4. **`PYTHON_VERSION`**
   - Value: `3.11` (or your Python version)

---

### Step 5: Wait for Deployment

**Railway will:**
1. Clone repo
2. Install Python dependencies
3. Start the server

**Wait 2-3 minutes**

**Check "Logs" tab** for errors

**Copy your Railway URL:**
- `https://lurantis-production-xxxx.up.railway.app`

---

### Step 6: Test Backend

**Open:** `https://your-railway-url.up.railway.app/health`

**Should see JSON response!**

---

## PART 5: Connect Frontend to Backend

### Step 1: Update Vercel Environment Variable

1. **Go to Vercel Dashboard**
2. **Your Project → Settings → Environment Variables**
3. **Edit** `NEXT_PUBLIC_API_URL`
4. **Change to:** Your Railway backend URL
5. **Save**

---

### Step 2: Redeploy Frontend

1. **Go to:** Deployments tab
2. **Click "..." on latest deployment**
3. **Click "Redeploy"**

**Wait for redeploy**

---

### Step 3: Test Everything

**Open your Vercel URL:** `https://lurantis-xxxxx.vercel.app`

**Test:**
1. ✅ Site loads
2. ✅ Wallet connection works
3. ✅ Wallet analysis works
4. ✅ API calls go to Railway backend

---

## PART 6: Make Accessible for Judges

### Step 1: Make GitHub Repository Public (if not already)

1. **Go to:** https://github.com/whybull6-star/lurantis/settings
2. **Scroll down to "Danger Zone"**
3. **Click "Change visibility"**
4. **Select "Make public"**
5. **Confirm**

---

### Step 2: Update README

**Make sure `README.md` has:**
- Project description
- Live demo link (Vercel URL)
- API docs link (Railway `/docs`)
- Qdrant usage summary
- Key features

---

### Step 3: Create Judges Access Document

**Create:** `JUDGES_ACCESS.md`

```markdown
# Lurantis - Judges Access

## Live Demo
**Frontend:** https://lurantis-xxxxx.vercel.app
**Backend API:** https://lurantis-production-xxxx.up.railway.app
**API Docs:** https://lurantis-production-xxxx.up.railway.app/docs

## GitHub Repository
https://github.com/whybull6-star/lurantis

## Qdrant Integration Proof
See `QDRANT_PITCH_DECK_PROOF.md` for complete documentation

## Key Features
- Vector search using Qdrant (33 patterns, 5 collections)
- Real transaction analysis from Gnosis Chain
- Semantic similarity detection
- Risk assessment based on Qdrant matches
```

---

## Quick Reference URLs

**After deployment, you'll have:**

- **Frontend:** `https://lurantis-xxxxx.vercel.app`
- **Backend:** `https://lurantis-production-xxxx.up.railway.app`
- **API Docs:** `https://lurantis-production-xxxx.up.railway.app/docs`
- **GitHub:** `https://github.com/whybull6-star/lurantis`

**Share these with judges!**

---

## Troubleshooting

### GitHub Push Issues

**"git not recognized"**
- Use GitHub Desktop instead
- Or install Git: https://git-scm.com/download/win

**"Repository not found"**
- Make sure you're logged into GitHub
- Check repository name is correct

### Vercel Deployment Issues

**"Build failed"**
- Check build logs in Vercel
- Make sure `frontend/package.json` exists
- Check Node.js version (should be 18+)

**"Environment variables not working"**
- Make sure they start with `NEXT_PUBLIC_`
- Redeploy after adding variables

### Railway Deployment Issues

**"Deployment failed"**
- Check logs in Railway
- Make sure `backend/requirements.txt` exists
- Check Python version matches

**"Port binding error"**
- Make sure start command uses `$PORT`
- Should be: `--port $PORT`

**"Qdrant connection failed"**
- Check `QDRANT_URL` and `QDRANT_API_KEY` are set
- Make sure Qdrant Cloud is accessible

---

## Checklist Before Judging

- [ ] ✅ All code pushed to GitHub
- [ ] ✅ Repository is public
- [ ] ✅ Frontend deployed to Vercel
- [ ] ✅ Backend deployed to Railway
- [ ] ✅ Frontend connected to backend
- [ ] ✅ Test wallet analysis works
- [ ] ✅ API docs accessible
- [ ] ✅ Qdrant proof documents in repo
- [ ] ✅ README updated with links
- [ ] ✅ JUDGES_ACCESS.md created

---

## Next Steps

1. ✅ Push to GitHub
2. ✅ Deploy to Vercel
3. ✅ Deploy to Railway
4. ✅ Test everything works
5. ✅ Share URLs with judges
6. ✅ Include Qdrant proof in pitch deck

**Good luck! 🚀**

