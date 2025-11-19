# Complete Deployment Guide - From Scratch

## Overview

This guide walks you through **everything from the beginning**:
1. ✅ Create GitHub account (if needed)
2. ✅ Create Vercel account (if needed)
3. ✅ Create Railway account (if needed)
4. ✅ Push your code to GitHub
5. ✅ Deploy frontend to Vercel
6. ✅ Deploy backend to Railway
7. ✅ Connect everything together

**No prior experience needed!** Follow step by step.

---

## PART 1: PREPARE YOUR PROJECT

### Step 1: Find Your Project Folder

**Your project is located at:**
```
C:\Users\valoo\Documents\social-engineering-analyzer
```

**Verify it exists:**
1. Open **File Explorer**
2. Go to: `C:\Users\valoo\Documents`
3. You should see folder: `social-engineering-analyzer`

✅ **If folder exists, continue!**

---

### Step 2: Check Important Files

**Make sure these exist:**

- ✅ `frontend/package.json` - Frontend dependencies
- ✅ `backend/requirements.txt` - Backend dependencies
- ✅ `backend/app_enhanced.py` - Main backend file
- ✅ `.gitignore` - Git ignore file (should exist)

**If any missing, ask me to help create them!**

---

## PART 2: CREATE GITHUB ACCOUNT

### Step 1: Go to GitHub

**Open:** https://github.com

---

### Step 2: Sign Up

1. **Click "Sign up"** (top right)

2. **Enter your information:**
   - **Username:** Choose a username (e.g., `yourname` or `lurantis-project`)
   - **Email:** Your email address
   - **Password:** Create a strong password
   - **Click "Continue"**

3. **Verify email:**
   - Check your email inbox
   - Click verification link
   - **✅ Account created!**

---

### Step 3: Remember Your Username

**Write down your username:** _________________

**You'll need this later!**

---

## PART 3: INSTALL GITHUB DESKTOP

### Step 1: Download GitHub Desktop

**Go to:** https://desktop.github.com

**Click "Download for Windows"**

---

### Step 2: Install

1. **Run the installer**
2. **Click "Install"**
3. **Wait for installation**
4. **Click "Finish"**

---

### Step 3: Sign In to GitHub Desktop

1. **Open GitHub Desktop** (from Start Menu)

2. **Click "Sign in to GitHub.com"**

3. **Enter your GitHub username and password**

4. **Authorize GitHub Desktop** (if asked)

5. **✅ You're signed in!**

---

## PART 4: PUSH CODE TO GITHUB

### Step 1: Add Your Project to GitHub Desktop

1. **In GitHub Desktop:**
   - Click **"File"** → **"Add Local Repository"**

2. **Browse to your project:**
   - Click **"Choose..."**
   - Navigate to: `C:\Users\valoo\Documents\social-engineering-analyzer`
   - Click **"Select Folder"**

3. **If asked "Create a repository?":**
   - Click **"Create a Repository"**
   - **Name:** `lurantis` (or whatever you want)
   - **Description:** (optional) "Qdrant-leveraged social engineering detection platform"
   - **✅ Repository added!**

---

### Step 2: Commit Your Files

1. **In GitHub Desktop, left side:**
   - You should see all your files listed
   - **All should be checked** (staged)

2. **If files not checked:**
   - **Check each file** manually
   - OR click **"Select all"** if available

3. **Bottom left - Write commit message:**
   ```
   Initial commit: Lurantis project with Qdrant integration
   ```

4. **Click "Commit to main"** button (bottom left)

5. **Wait for commit to complete**
   - ✅ **Files committed!**

---

### Step 3: Create GitHub Repository Online

1. **Go to:** https://github.com/new
   - (Make sure you're signed in)

2. **Fill in:**
   - **Repository name:** `lurantis`
   - **Description:** "Qdrant-leveraged, AI-powered social engineering detection platform"
   - **Visibility:** 
     - ✅ **Public** (so judges can see it)
     - OR **Private** (if you prefer)

3. **DO NOT check these:**
   - ❌ "Add a README file" (you already have one)
   - ❌ "Add .gitignore" (you already have one)
   - ❌ "Choose a license" (optional, skip for now)

4. **Click "Create repository"**

5. **✅ Repository created!**

---

### Step 4: Push to GitHub

1. **Back in GitHub Desktop:**
   - You should see button: **"Publish repository"** (top center)
   - OR **"Push origin"** button

2. **Click "Publish repository"**

3. **If asked about name:**
   - **Name:** `lurantis` (or same as your online repo)
   - **Uncheck "Keep this code private"** if you want public

4. **Click "Publish repository"**

5. **Wait for push to complete**
   - You'll see: "Successfully pushed to GitHub"
   - ✅ **Code is on GitHub!**

---

### Step 5: Verify on GitHub

1. **Go to:** https://github.com/YOUR_USERNAME/lurantis
   - Replace `YOUR_USERNAME` with your actual username

2. **You should see:**
   - ✅ All your files
   - ✅ `frontend/` folder
   - ✅ `backend/` folder
   - ✅ All documentation files

**✅ GitHub is set up!**

---

## PART 5: CREATE VERCEL ACCOUNT

### Step 1: Go to Vercel

**Open:** https://vercel.com

---

### Step 2: Sign Up with GitHub

1. **Click "Sign Up"** (top right)

2. **Select "Continue with GitHub"**
   - This uses your GitHub account
   - **Easiest option!**

3. **Authorize Vercel:**
   - Click "Authorize Vercel" if asked
   - This connects Vercel to your GitHub

4. **Complete setup:**
   - Choose your team name (optional)
   - Click "Continue"

5. **✅ Vercel account created!**

---

## PART 6: DEPLOY FRONTEND TO VERCEL

### Step 1: Import Your Project

1. **In Vercel Dashboard:**
   - Click **"Add New Project"** (or "Import Project")

2. **You should see your GitHub repositories:**
   - Find: `YOUR_USERNAME/lurantis`
   - Click **"Import"**

---

### Step 2: Configure Project

**IMPORTANT: Set Root Directory!**

1. **Project Settings:**
   - **Project Name:** `lurantis` (or whatever you want)
   - **Framework Preset:** Should auto-detect "Next.js" ✅
   - **Root Directory:** 
     - **Click "Edit"**
     - **Change from:** `.` (current folder)
     - **Change to:** `frontend`
     - **Click "Continue"**

2. **Build Settings (should be auto-detected):**
   - **Build Command:** `npm run build` ✅
   - **Output Directory:** `.next` ✅
   - **Install Command:** `npm install` ✅

3. **Environment Variables:**
   - **Click "Environment Variables"** section
   - **Add these variables one by one:**

   **Variable 1:**
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `http://localhost:8000` (we'll update this later)
   - **Click "Add"**

   **Variable 2:**
   - **Name:** `NEXT_PUBLIC_GNOSIS_RPC`
   - **Value:** `https://rpc.gnosischain.com`
   - **Click "Add"**

   **Variable 3:**
   - **Name:** `NEXT_PUBLIC_CONTRACT_ADDRESS`
   - **Value:** (leave empty for now, or add if you have contract address)
   - **Click "Add"**

4. **Click "Deploy"** button (bottom right)

---

### Step 3: Wait for Deployment

**Vercel will now:**
1. Clone your repository
2. Install dependencies (`npm install`)
3. Build the project (`npm run build`)
4. Deploy to Vercel

**This takes 2-3 minutes**

**You'll see:**
- ✅ "Building..."
- ✅ "Deployed" (green checkmark)

---

### Step 4: Get Your Vercel URL

**After deployment:**

1. **You'll see:** "Congratulations! Your project has been deployed"

2. **Copy your URL:**
   - Example: `https://lurantis-abc123.vercel.app`
   - **Write it down:** _________________

3. **Click the URL to test:**
   - Site should load!
   - (API might not work yet, that's OK)

**✅ Frontend deployed!**

---

## PART 7: CREATE RAILWAY ACCOUNT

### Step 1: Go to Railway

**Open:** https://railway.app

---

### Step 2: Sign Up

1. **Click "Start a New Project"** or **"Sign Up"**

2. **Select "Login with GitHub"**
   - Uses your GitHub account
   - **Easiest option!**

3. **Authorize Railway:**
   - Click "Authorize Railway" if asked

4. **Complete setup:**
   - Choose plan (free tier is fine)
   - Click "Continue"

5. **✅ Railway account created!**

---

## PART 8: DEPLOY BACKEND TO RAILWAY

### Step 1: Create New Project

1. **In Railway Dashboard:**
   - Click **"New Project"**

2. **Select "Deploy from GitHub repo"**

3. **Find your repository:**
   - Search for: `lurantis`
   - OR scroll to find: `YOUR_USERNAME/lurantis`
   - **Click on it**

4. **Railway will start deploying automatically!**
   - Wait a moment...

---

### Step 2: Configure Backend

1. **Click on your project** (in Railway)

2. **Click on the service** (should show "GitHub Repo")

3. **Settings Tab:**
   - **Root Directory:**
     - Click **"Edit"**
     - Change to: `backend`
     - **Click "Save"**

4. **Settings Tab - Start Command:**
   - **Start Command:**
     - Click **"Edit"**
     - Enter: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
     - **Click "Save"**

---

### Step 3: Add Environment Variables

1. **Click "Variables" tab** (top of Railway)

2. **Add these variables:**

   **Variable 1:**
   - **Name:** `QDRANT_URL`
   - **Value:** Your Qdrant Cloud URL
     - Example: `https://your-cluster-xxxxx.qdrant.io`
     - **Get from:** Qdrant Cloud dashboard
   - **Click "Add"**

   **Variable 2:**
   - **Name:** `QDRANT_API_KEY`
   - **Value:** Your Qdrant API key
     - **Get from:** Qdrant Cloud dashboard
   - **Click "Add"**

   **Variable 3:**
   - **Name:** `GNOSIS_RPC_URL`
   - **Value:** `https://rpc.gnosischain.com`
   - **Click "Add"**

   **Variable 4:**
   - **Name:** `PYTHON_VERSION`
   - **Value:** `3.11` (or `3.10`)
   - **Click "Add"**

3. **Save all variables**

---

### Step 4: Wait for Deployment

**Railway will:**
1. Clone your repository
2. Install Python dependencies (`pip install -r requirements.txt`)
3. Start the server (`uvicorn app_enhanced:app`)

**This takes 2-3 minutes**

**Check "Deployments" tab:**
- ✅ Should show "Active" (green)
- ❌ If "Failed", check "Logs" tab for errors

---

### Step 5: Get Your Railway URL

**After deployment:**

1. **Click "Settings" tab**

2. **Scroll to "Networking"**

3. **Click "Generate Domain"** (if not already done)

4. **Copy your URL:**
   - Example: `https://lurantis-production-xxxx.up.railway.app`
   - **Write it down:** _________________

5. **Test your backend:**
   - Open: `YOUR_RAILWAY_URL/health`
   - Should see JSON response: `{"status": "healthy", ...}`

**✅ Backend deployed!**

---

## PART 9: CONNECT FRONTEND TO BACKEND

### Step 1: Update Vercel Environment Variable

1. **Go back to Vercel Dashboard**

2. **Click on your project** (`lurantis`)

3. **Go to "Settings" tab** (top)

4. **Click "Environment Variables"** (left menu)

5. **Find:** `NEXT_PUBLIC_API_URL`

6. **Click the pencil icon** (edit)

7. **Change value from:**
   ```
   http://localhost:8000
   ```
   **To:**
   ```
   https://YOUR_RAILWAY_URL.up.railway.app
   ```
   (Replace `YOUR_RAILWAY_URL` with your actual Railway URL)

8. **Click "Save"**

---

### Step 2: Redeploy Frontend

1. **Still in Vercel:**

2. **Go to "Deployments" tab** (top)

3. **Find latest deployment**

4. **Click the three dots** `...` (right side)

5. **Click "Redeploy"**

6. **Click "Redeploy"** again to confirm

7. **Wait 1-2 minutes** for redeploy

---

### Step 3: Test Everything

**Open your Vercel URL:** `https://lurantis-xxxxx.vercel.app`

**Test:**
1. ✅ Site loads
2. ✅ Wallet connection works (if you have MetaMask)
3. ✅ Wallet analysis works (enters wallet address)
4. ✅ API calls work (check browser console: F12)

**✅ Everything connected!**

---

## PART 10: FINAL STEPS

### Step 1: Make GitHub Repository Public (Optional)

**If you want judges to see your code:**

1. **Go to:** https://github.com/YOUR_USERNAME/lurantis/settings

2. **Scroll down to "Danger Zone"**

3. **Click "Change visibility"**

4. **Select "Make public"**

5. **Type:** `YOUR_USERNAME/lurantis` to confirm

6. **Click "Change visibility"**

**✅ Repository is now public!**

---

### Step 2: Update README (Optional)

**Make your README look professional:**

1. **Go to:** https://github.com/YOUR_USERNAME/lurantis

2. **Click on `README.md`**

3. **Click "Edit" (pencil icon)**

4. **Add at the top:**
   ```markdown
   # Lurantis - Social Engineering Detection Platform

   ## Live Demo
   - **Frontend:** https://lurantis-xxxxx.vercel.app
   - **Backend API:** https://lurantis-production-xxxx.up.railway.app
   - **API Docs:** https://lurantis-production-xxxx.up.railway.app/docs

   ## Features
   - Qdrant vector search (33 patterns, 5 collections)
   - Real transaction analysis from Gnosis Chain
   - Wallet risk assessment
   - Semantic similarity detection

   ## Qdrant Integration
   See `QDRANT_PITCH_DECK_PROOF.md` for complete documentation.
   ```

5. **Click "Commit changes"** (bottom)

**✅ README updated!**

---

## YOUR FINAL URLs

**Write these down:**

- **GitHub:** `https://github.com/YOUR_USERNAME/lurantis`
- **Frontend:** `https://lurantis-xxxxx.vercel.app`
- **Backend:** `https://lurantis-production-xxxx.up.railway.app`
- **API Docs:** `https://lurantis-production-xxxx.up.railway.app/docs`

**Share these with judges!**

---

## TROUBLESHOOTING

### GitHub Desktop Issues

**"git not recognized"**
- You need GitHub Desktop (we installed it)
- Make sure it's running

**"Repository not found"**
- Make sure you created the repo on GitHub.com first
- Then publish from GitHub Desktop

### Vercel Deployment Issues

**"Build failed"**
- Check build logs in Vercel
- Make sure Root Directory is set to `frontend`
- Check `frontend/package.json` exists

**"Environment variables not working"**
- Make sure they start with `NEXT_PUBLIC_`
- Redeploy after adding variables

### Railway Deployment Issues

**"Deployment failed"**
- Check "Logs" tab in Railway
- Make sure Root Directory is set to `backend`
- Check `backend/requirements.txt` exists

**"Qdrant connection failed"**
- Check `QDRANT_URL` and `QDRANT_API_KEY` are set correctly
- Make sure Qdrant Cloud is accessible
- Check Railway logs for connection errors

**"Port binding error"**
- Make sure Start Command uses `$PORT`
- Should be: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`

---

## QUICK REFERENCE

### GitHub
- **URL:** https://github.com
- **Desktop:** https://desktop.github.com
- **Repository:** `https://github.com/YOUR_USERNAME/lurantis`

### Vercel
- **URL:** https://vercel.com
- **Root Directory:** `frontend`
- **Environment:** `NEXT_PUBLIC_API_URL` = Railway URL

### Railway
- **URL:** https://railway.app
- **Root Directory:** `backend`
- **Start Command:** `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`

---

## CHECKLIST

**Before Judging:**

- [ ] ✅ GitHub account created
- [ ] ✅ Code pushed to GitHub
- [ ] ✅ Vercel account created
- [ ] ✅ Frontend deployed to Vercel
- [ ] ✅ Railway account created
- [ ] ✅ Backend deployed to Railway
- [ ] ✅ Frontend connected to backend
- [ ] ✅ Test wallet analysis works
- [ ] ✅ API docs accessible
- [ ] ✅ Repository is public (optional)
- [ ] ✅ README updated with links (optional)

---

## DONE! 🎉

**Your project is now live!**

**Next steps:**
1. ✅ Share URLs with judges
2. ✅ Include Qdrant proof in pitch deck
3. ✅ Prepare presentation

**Good luck! 🚀**

