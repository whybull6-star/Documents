# 🚀 Step-by-Step: Deploy Lurantis to Vercel

Complete guide from zero to deployed site.

**For ULTRA detailed instructions (every single click explained), see: [ULTRA_DETAILED_DEPLOY.md](./ULTRA_DETAILED_DEPLOY.md)**

---

## Prerequisites Checklist

Before starting, make sure you have:
- [ ] GitHub account (free at github.com)
- [ ] Vercel account (free at vercel.com - sign in with GitHub)
- [ ] Railway account (free at railway.app - sign in with GitHub)
- [ ] Git installed on your computer
- [ ] Your backend API URL (if already deployed) or we'll deploy it

---

## PART 1: Git Setup & Push to GitHub

### Step 1: Check if Git is Installed

Open PowerShell (Windows) or Terminal (Mac/Linux) and run:

```bash
git --version
```

**If you see a version number** → Git is installed! Skip to Step 2.

**If you see an error** → Install Git:
- Windows: Download from https://git-scm.com/download/win
- Mac: `brew install git` or download from git-scm.com
- Linux: `sudo apt install git`

---

### Step 2: Navigate to Your Project

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer
```

Verify you're in the right place:
```bash
dir
```

You should see folders like `frontend`, `backend`, `contracts`, etc.

---

### Step 3: Initialize Git Repository

```bash
git init
```

You should see: `Initialized empty Git repository in ...`

---

### Step 4: Check What Files Will Be Added

```bash
git status
```

This shows all files. Make sure `.env` files are NOT listed (they should be in `.gitignore`).

---

### Step 5: Add All Files to Git

```bash
git add .
```

This stages all files for commit.

---

### Step 6: Create First Commit

```bash
git commit -m "Initial commit - Lurantis project ready for deployment"
```

You should see: `[main (root-commit) xxxxx] Initial commit...`

---

### Step 7: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Sign in** (or create account if needed)
3. **Click the "+" icon** (top right) → **"New repository"**
4. **Repository name**: `lurantis` (or any name you want)
5. **Description**: "Qdrant-leveraged, AI-powered platform for detecting social engineering attacks"
6. **Visibility**: 
   - ✅ **Public** (free, anyone can see code)
   - ⚠️ **Private** (requires paid plan, but code is hidden)
7. **DO NOT** check "Initialize with README" (you already have files)
8. **Click "Create repository"**

---

### Step 8: Connect Local Git to GitHub

GitHub will show you commands. Use these (replace `YOUR_USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/lurantis.git
```

**Example:**
```bash
git remote add origin https://github.com/valoo/lurantis.git
```

---

### Step 9: Rename Branch to Main (if needed)

```bash
git branch -M main
```

---

### Step 10: Push to GitHub

```bash
git push -u origin main
```

**First time?** GitHub will ask you to sign in:
- Username: Your GitHub username
- Password: **Use a Personal Access Token** (not your password)

**To create a Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name it: "Vercel Deployment"
4. Select scopes: ✅ `repo` (all)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)
7. Use this token as your password when pushing

**After pushing**, you should see:
```
Enumerating objects: X, done.
Writing objects: 100% (X/X), done.
To https://github.com/YOUR_USERNAME/lurantis.git
 * [new branch]      main -> main
```

**✅ Success!** Your code is now on GitHub!

---

## PART 2: Deploy Frontend to Vercel

### Step 11: Go to Vercel

1. **Go to**: https://vercel.com
2. **Click "Sign Up"** (or "Log In" if you have an account)
3. **Sign in with GitHub** (recommended - easier integration)

---

### Step 12: Import Your Repository

1. **Click "Add New Project"** (or "Import Project")
2. **You'll see your GitHub repositories**
3. **Find `lurantis`** (or whatever you named it)
4. **Click "Import"** next to it

---

### Step 13: Configure Project Settings

**IMPORTANT SETTINGS:**

1. **Project Name**: `lurantis` (or keep default)

2. **Root Directory**: 
   - Click "Edit" next to Root Directory
   - Type: `frontend`
   - Click "Continue"
   - **This tells Vercel to deploy the `frontend/` folder, not the root**

3. **Framework Preset**: 
   - Should auto-detect "Next.js"
   - If not, select "Next.js"

4. **Build Command**: 
   - Leave default: `npm run build`

5. **Output Directory**: 
   - Leave default: `.next`

6. **Install Command**: 
   - Leave default: `npm install`

---

### Step 14: Add Environment Variables

**Before clicking "Deploy", add these environment variables:**

Click **"Environment Variables"** section and add:

1. **`NEXT_PUBLIC_API_URL`**
   - Value: `http://localhost:8000` (for now, we'll update later)
   - Environment: ✅ Production, ✅ Preview, ✅ Development

2. **`NEXT_PUBLIC_CONTRACT_ADDRESS`**
   - Value: Your contract address (if you have one)
   - Environment: ✅ Production, ✅ Preview, ✅ Development

3. **`NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`**
   - Value: Your subscription contract address (if you have one)
   - Environment: ✅ Production, ✅ Preview, ✅ Development

4. **`NEXT_PUBLIC_GNOSIS_RPC`**
   - Value: `https://rpc.gnosischain.com`
   - Environment: ✅ Production, ✅ Preview, ✅ Development

**Click "Add" for each variable.**

---

### Step 15: Deploy!

1. **Click "Deploy"** button (bottom right)
2. **Wait for build** (takes 1-3 minutes)
3. **You'll see build logs** in real-time
4. **When done**, you'll see: ✅ "Ready"

---

### Step 16: Get Your Vercel URL

After deployment:
- You'll see: **"Congratulations! Your project has been deployed"**
- Your site URL: `https://lurantis-xxxxx.vercel.app`
- **Copy this URL!** You'll need it later.

**✅ Frontend is now live!**

---

## PART 3: Deploy Backend to Railway

### Step 17: Go to Railway

1. **Go to**: https://railway.app
2. **Click "Start a New Project"**
3. **Sign in with GitHub** (recommended)

---

### Step 18: Create New Project

1. **Click "New Project"**
2. **Select "Deploy from GitHub repo"**
3. **Find and select `lurantis`** repository
4. **Click "Deploy Now"**

---

### Step 19: Configure Backend

1. **Railway will detect it's a Python project**
2. **Click on the service** (it will be named after your repo)
3. **Go to "Settings" tab**
4. **Set Root Directory**: 
   - Click "Edit"
   - Type: `backend`
   - Click "Save"
   - **This tells Railway to deploy the `backend/` folder**

---

### Step 20: Configure Start Command

1. **Still in Settings**, scroll to **"Start Command"**
2. **Click "Edit"**
3. **Enter**:
   ```
   uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT
   ```
4. **Click "Save"**

---

### Step 21: Add Environment Variables (Backend)

1. **Go to "Variables" tab** in Railway
2. **Add these variables:**

   **`QDRANT_URL`**
   - Value: Your Qdrant Cloud URL (e.g., `https://xxxxx.qdrant.io`)
   - Or: `http://localhost:6333` if using local Qdrant

   **`QDRANT_API_KEY`** (if using Qdrant Cloud)
   - Value: Your Qdrant API key

   **`GNOSIS_RPC_URL`**
   - Value: `https://rpc.gnosischain.com`

3. **Click "Add" for each variable**

---

### Step 22: Wait for Deployment

1. **Go to "Deployments" tab**
2. **Watch the build logs**
3. **Wait for**: ✅ "Deploy successful"
4. **This takes 2-5 minutes**

---

### Step 23: Get Your Backend URL

1. **Go to "Settings" tab**
2. **Scroll to "Domains"**
3. **You'll see**: `https://lurantis-production-xxxx.up.railway.app`
4. **Copy this URL!** This is your backend API URL.

**✅ Backend is now live!**

---

## PART 4: Connect Frontend to Backend

### Step 24: Update Frontend Environment Variable

1. **Go back to Vercel** (vercel.com)
2. **Select your `lurantis` project**
3. **Go to "Settings" → "Environment Variables"**
4. **Find `NEXT_PUBLIC_API_URL`**
5. **Click the three dots** → **"Edit"**
6. **Change value to**: Your Railway backend URL
   - Example: `https://lurantis-production-xxxx.up.railway.app`
7. **Click "Save"**

---

### Step 25: Redeploy Frontend

1. **Go to "Deployments" tab** in Vercel
2. **Click the three dots** on the latest deployment
3. **Click "Redeploy"**
4. **Wait for deployment** (1-2 minutes)

**✅ Frontend now connected to backend!**

---

## PART 5: Test Everything

### Step 26: Test Frontend

1. **Go to your Vercel URL**: `https://lurantis-xxxxx.vercel.app`
2. **Check if site loads**
3. **Try connecting wallet**
4. **Check if API Docs link works** (in footer)

---

### Step 27: Test Backend API

1. **Go to**: `https://your-railway-url.up.railway.app/docs`
2. **You should see FastAPI Swagger UI**
3. **Test the `/health` endpoint**:
   - Click on `/health`
   - Click "Try it out"
   - Click "Execute"
   - Should return: `{"status": "healthy", ...}`

---

### Step 28: Test API Docs Link

1. **Go to your Vercel site**
2. **Scroll to footer**
3. **Click "API Docs"**
4. **Should open**: Your Railway backend `/docs` page in new tab

**✅ Everything working!**

---

## Troubleshooting

### Git Push Fails

**Error: "Authentication failed"**
- Use Personal Access Token instead of password
- See Step 10 for how to create one

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

## Quick Reference: URLs

After deployment, you'll have:

- **Frontend**: `https://lurantis-xxxxx.vercel.app`
- **Backend API**: `https://lurantis-production-xxxx.up.railway.app`
- **API Docs**: `https://lurantis-production-xxxx.up.railway.app/docs`

---

## Next Steps

1. **Custom Domain** (optional):
   - In Vercel: Settings → Domains → Add your domain
   - Follow DNS instructions

2. **Update CORS** (production):
   - In backend, update CORS to only allow your Vercel domain
   - More secure than allowing `*`

3. **Monitor**:
   - Vercel: Check deployment logs
   - Railway: Check service logs

---

## Summary Checklist

- [ ] Git initialized
- [ ] Code pushed to GitHub
- [ ] Frontend deployed to Vercel
- [ ] Backend deployed to Railway
- [ ] Environment variables set
- [ ] Frontend connected to backend
- [ ] Site tested and working
- [ ] API Docs link working

**🎉 You're done! Your site is live!**

