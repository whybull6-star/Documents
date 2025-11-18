# 🚀 Ultra Detailed: Deploy Lurantis - Every Single Step

This guide assumes you know NOTHING. Every click, every command explained.

**For quick deployment, see: [FINAL_DEPLOYMENT.md](./FINAL_DEPLOYMENT.md)**

---

## BEFORE YOU START: What You Need

- [ ] Windows computer
- [ ] Internet connection
- [ ] GitHub account (we'll create if needed)
- [ ] Your project folder: `C:\Users\valoo\Documents\social-engineering-analyzer`

---

## PART 0: Opening Command Prompt

### Step 0.1: Open Command Prompt

**Method 1: Search**
1. Press `Windows Key` (bottom left of keyboard)
2. Type: `cmd`
3. You'll see "Command Prompt" appear
4. Click on it (or press Enter)

**Method 2: Run Dialog**
1. Press `Windows Key + R`
2. Type: `cmd`
3. Press Enter

**You should see a black window with text like:**
```
Microsoft Windows [Version 10.0.xxxxx]
(c) Microsoft Corporation. All rights reserved.

C:\Users\valoo>
```

---

### Step 0.2: Clear the Screen (Optional but Recommended)

**Why?** Makes it easier to see what you're doing.

**How:**
1. Type: `cls`
2. Press `Enter`

**You'll see:** Screen clears, cursor goes to top

**Now you have a clean screen!**

---

### Step 0.3: Check You're in the Right Place

**Current location shows at the prompt:**
```
C:\Users\valoo>
```

**This means you're in your user folder.**

**Good!** This is where we start.

---

## PART 1: Navigate to Your Project

### Step 1.1: Go to Documents Folder

**Type this command:**
```cmd
cd Documents
```

**Press Enter**

**You should see:**
```
C:\Users\valoo\Documents>
```

**What happened?** You moved into the Documents folder.

---

### Step 1.2: Go to Your Project Folder

**Type this command:**
```cmd
cd social-engineering-analyzer
```

**Press Enter**

**You should see:**
```
C:\Users\valoo\Documents\social-engineering-analyzer>
```

**What happened?** You're now in your project folder!

---

### Step 1.3: Verify You're in the Right Place

**Type this command:**
```cmd
dir
```

**Press Enter**

**You should see a list of folders:**
```
 Directory of C:\Users\valoo\Documents\social-engineering-analyzer

[folder]  backend
[folder]  frontend
[folder]  contracts
[file]    README.md
... (more files)
```

**✅ Perfect!** You're in the right place if you see `frontend`, `backend`, `contracts` folders.

**❌ If you see "The system cannot find the path specified":**
- Check the folder name is exactly: `social-engineering-analyzer`
- Check you're in `Documents` folder first
- Try: `cd C:\Users\valoo\Documents\social-engineering-analyzer` (full path)

---

## PART 2: Git Setup

### Step 2.1: Check if Git is Installed

**Type this command:**
```cmd
git --version
```

**Press Enter**

**✅ If you see something like:**
```
git version 2.xx.x.windows.x
```

**Great! Git is installed. Skip to Step 2.3.**

**❌ If you see:**
```
'git' is not recognized as an internal or external command...
```

**Git is NOT installed. Install it:**
1. Go to: https://git-scm.com/download/win
2. Download the installer (it will auto-detect 64-bit)
3. Run the installer
4. **IMPORTANT:** During installation:
   - Click "Next" through all screens
   - **When you see "Choosing the default editor"**: Select "Use Visual Studio Code" or "Nano" (not Vim)
   - **When you see "Adjusting your PATH environment"**: Select "Git from the command line and also from 3rd-party software"
   - Click "Next" through rest
   - Click "Install"
5. **After installation**: Close Command Prompt and open a NEW one
6. Go back to Step 2.1 and check again

---

### Step 2.2: Configure Git (First Time Only)

**Only do this if you've NEVER used Git before on this computer.**

**Type this command (replace with YOUR name):**
```cmd
git config --global user.name "Your Name"
```

**Press Enter**

**Example:**
```cmd
git config --global user.name "Valoo"
```

**Then type:**
```cmd
git config --global user.email "your.email@example.com"
```

**Press Enter**

**Example:**
```cmd
git config --global user.email "valoo@example.com"
```

**You won't see any output - that's normal!**

**What happened?** Git now knows who you are.

---

### Step 2.3: Initialize Git Repository

**Type this command:**
```cmd
git init
```

**Press Enter**

**You should see:**
```
Initialized empty Git repository in C:/Users/valoo/Documents/social-engineering-analyzer/.git/
```

**✅ Success!** Git repository created.

**What happened?** Git created a hidden `.git` folder to track your files.

---

### Step 2.4: Check What Files Will Be Added

**Type this command:**
```cmd
git status
```

**Press Enter**

**You'll see a list of files:**
```
On branch main

No commits yet

Untracked files:
  (use "git add ." to include in what will be committed)
        backend/
        frontend/
        contracts/
        README.md
        ... (many more files)
```

**✅ Good!** All your project files are listed.

**⚠️ IMPORTANT:** Make sure you DON'T see `.env` files listed. If you do:
- They should be in `.gitignore` (we'll check this)
- If they're not ignored, we need to fix `.gitignore` first

**Check if `.gitignore` exists:**
```cmd
type .gitignore
```

**Press Enter**

**If you see content**, good! If you see "The system cannot find the file", we need to create one (but we already have one, so this shouldn't happen).

---

### Step 2.5: Add All Files to Git

**Type this command:**
```cmd
git add .
```

**Press Enter**

**You won't see any output - that's normal!**

**What happened?** All files are now "staged" (ready to be saved).

**Verify files were added:**
```cmd
git status
```

**Press Enter**

**You should see:**
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   backend/app_enhanced.py
        new file:   frontend/package.json
        ... (many files listed in green)
```

**✅ Perfect!** Files are staged.

---

### Step 2.6: Create First Commit

**Type this command:**
```cmd
git commit -m "Initial commit - Lurantis project ready for deployment"
```

**Press Enter**

**You should see:**
```
[main (root-commit) xxxxxxx] Initial commit - Lurantis project ready for deployment
 X files changed, X insertions(+)
 create mode 100644 backend/app_enhanced.py
 ... (many files listed)
```

**✅ Success!** Your code is now saved in Git!

**What happened?** Git took a "snapshot" of all your files.

---

## PART 3: Create GitHub Repository

### Step 3.1: Open Web Browser

**Open your web browser** (Chrome, Edge, Firefox, etc.)

---

### Step 3.2: Go to GitHub

**Type in address bar:**
```
https://github.com
```

**Press Enter**

---

### Step 3.3: Sign In (or Sign Up)

**If you have a GitHub account:**
1. Click "Sign in" (top right)
2. Enter username/email and password
3. Click "Sign in"

**If you DON'T have a GitHub account:**
1. Click "Sign up" (top right)
2. Enter:
   - Username (e.g., `valoo`)
   - Email address
   - Password
3. Click "Create account"
4. Verify your email (check inbox)
5. Complete setup steps

---

### Step 3.4: Create New Repository

**After signing in:**

1. **Look for a "+" icon** (top right, next to your profile picture)
2. **Click the "+" icon**
3. **Click "New repository"** from dropdown

**You'll see a form:**

---

### Step 3.5: Fill Repository Details

**Repository name:**
- Type: `lurantis`
- (Or any name you want, but `lurantis` is recommended)

**Description (optional):**
- Type: `Qdrant-leveraged, AI-powered platform for detecting social engineering attacks`

**Visibility:**
- ✅ **Public** (recommended - free, anyone can see code)
- ⚠️ **Private** (requires paid plan, but code is hidden)

**IMPORTANT - DO NOT CHECK THESE:**
- ❌ **DO NOT** check "Add a README file" (you already have one)
- ❌ **DO NOT** check "Add .gitignore" (you already have one)
- ❌ **DO NOT** check "Choose a license" (optional, can add later)

**Leave everything else as default.**

---

### Step 3.6: Create Repository

**Click the green "Create repository" button** (bottom of page)

**You'll see a page with instructions - DON'T follow them yet!**

**You should see something like:**
```
Quick setup — if you've done this kind of thing before
https://github.com/YOUR_USERNAME/lurantis.git
```

**✅ Repository created!**

**Copy the URL** (you'll need it in a moment):
- It looks like: `https://github.com/YOUR_USERNAME/lurantis.git`
- **Replace `YOUR_USERNAME` with your actual GitHub username**

---

## PART 4: Connect Local Git to GitHub

### Step 4.1: Go Back to Command Prompt

**Switch back to your Command Prompt window**

**Make sure you're still in the project folder:**
```cmd
cd C:\Users\valoo\Documents\social-engineering-analyzer
```

**Press Enter**

---

### Step 4.2: Add GitHub as Remote

**Type this command (replace `YOUR_USERNAME` with your GitHub username):**
```cmd
git remote add origin https://github.com/YOUR_USERNAME/lurantis.git
```

**Press Enter**

**Example (if your username is `valoo`):**
```cmd
git remote add origin https://github.com/valoo/lurantis.git
```

**You won't see any output - that's normal!**

**What happened?** Git now knows where to send your code.

---

### Step 4.3: Verify Remote Was Added

**Type this command:**
```cmd
git remote -v
```

**Press Enter**

**You should see:**
```
origin  https://github.com/YOUR_USERNAME/lurantis.git (fetch)
origin  https://github.com/YOUR_USERNAME/lurantis.git (push)
```

**✅ Perfect!** Remote is connected.

---

### Step 4.4: Rename Branch to Main

**Type this command:**
```cmd
git branch -M main
```

**Press Enter**

**You won't see any output - that's normal!**

**What happened?** Git renamed your branch to `main` (GitHub's default).

---

## PART 5: Push to GitHub

### Step 5.1: Push Your Code

**Type this command:**
```cmd
git push -u origin main
```

**Press Enter**

---

### Step 5.2: Authentication

**You'll see one of these:**

**Option A: Browser Opens**
- GitHub login page opens in browser
- Sign in
- Authorize Git
- Go back to Command Prompt

**Option B: Username/Password Prompt**
```
Username for 'https://github.com':
```

**Type your GitHub username, press Enter**

**Then you'll see:**
```
Password for 'https://github.com/YOUR_USERNAME':
```

**⚠️ IMPORTANT:** GitHub doesn't accept passwords anymore!

**You need a Personal Access Token instead.**

---

### Step 5.3: Create Personal Access Token

**If you need a token (you'll know if password doesn't work):**

1. **Go to GitHub in browser**
2. **Click your profile picture** (top right)
3. **Click "Settings"**
4. **Scroll down, click "Developer settings"** (left sidebar, at bottom)
5. **Click "Personal access tokens"**
6. **Click "Tokens (classic)"**
7. **Click "Generate new token"**
8. **Click "Generate new token (classic)"**
9. **Fill in:**
   - **Note**: `Vercel Deployment` (or any name)
   - **Expiration**: `90 days` (or `No expiration` if you want)
   - **Select scopes**: ✅ Check `repo` (this checks all repo permissions)
10. **Scroll down, click "Generate token"** (green button)
11. **⚠️ IMPORTANT:** Copy the token NOW (you won't see it again!)
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - **Copy the entire thing**

---

### Step 5.4: Use Token as Password

**Go back to Command Prompt**

**If it's still asking for password:**
- **Paste the token** (right-click to paste in CMD, or `Shift + Insert`)
- **Press Enter**

**You should see:**
```
Enumerating objects: X, done.
Counting objects: 100% (X/X), done.
Delta compression using up to X threads
Compressing objects: 100% (X/X), done.
Writing objects: 100% (X/X), X.XX MiB | X.XX MiB/s, done.
Total X (delta X), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (X/X), done.
To https://github.com/YOUR_USERNAME/lurantis.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

**✅ SUCCESS!** Your code is now on GitHub!

---

### Step 5.5: Verify on GitHub

**Go back to your browser**

**Go to:** `https://github.com/YOUR_USERNAME/lurantis`

**You should see:**
- All your files
- Folders: `backend/`, `frontend/`, `contracts/`
- README.md
- Everything from your project

**✅ Perfect!** Code is on GitHub!

---

## PART 6: Deploy Frontend to Vercel

### Step 6.1: Go to Vercel

**In your browser, go to:**
```
https://vercel.com
```

---

### Step 6.2: Sign In

**Click "Sign Up" or "Log In"**

**Click "Continue with GitHub"** (recommended - easier)

**Authorize Vercel** (click "Authorize vercel")

**You'll be redirected to Vercel dashboard**

---

### Step 6.3: Create New Project

**Click "Add New Project"** (big button, or top right)

**You'll see a list of your GitHub repositories**

---

### Step 6.4: Import Repository

**Find `lurantis` in the list**

**Click "Import"** next to it

---

### Step 6.5: Configure Project

**You'll see a configuration page:**

**Project Name:**
- Leave as `lurantis` (or change if you want)

**Framework Preset:**
- Should auto-detect "Next.js"
- If not, select "Next.js" from dropdown

**Root Directory:**
- **⚠️ CRITICAL:** Click "Edit" next to "Root Directory"
- **Type:** `frontend`
- **Click "Continue"**
- **This tells Vercel to deploy the `frontend/` folder, not the root!**

**Build Command:**
- Leave as: `npm run build` (default)

**Output Directory:**
- Leave as: `.next` (default)

**Install Command:**
- Leave as: `npm install` (default)

---

### Step 6.6: Add Environment Variables

**Before clicking "Deploy", scroll down to "Environment Variables"**

**Click "Add" for each variable:**

**1. Add `NEXT_PUBLIC_API_URL`:**
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `http://localhost:8000` (we'll update this later)
   - **Environments:** ✅ Check all (Production, Preview, Development)
   - **Click "Add"**

**2. Add `NEXT_PUBLIC_CONTRACT_ADDRESS`:**
   - **Name:** `NEXT_PUBLIC_CONTRACT_ADDRESS`
   - **Value:** (leave empty for now, or add if you have it)
   - **Environments:** ✅ Check all
   - **Click "Add"**

**3. Add `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`:**
   - **Name:** `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`
   - **Value:** (leave empty for now, or add if you have it)
   - **Environments:** ✅ Check all
   - **Click "Add"**

**4. Add `NEXT_PUBLIC_GNOSIS_RPC`:**
   - **Name:** `NEXT_PUBLIC_GNOSIS_RPC`
   - **Value:** `https://rpc.gnosischain.com`
   - **Environments:** ✅ Check all
   - **Click "Add"**

---

### Step 6.7: Deploy!

**Scroll to bottom of page**

**Click the blue "Deploy" button**

**You'll see build logs in real-time:**
```
Cloning repository...
Installing dependencies...
Building...
```

**Wait 1-3 minutes** (coffee break time!)

---

### Step 6.8: Deployment Complete!

**When done, you'll see:**
```
✅ Ready
```

**And a URL like:**
```
https://lurantis-xxxxx.vercel.app
```

**✅ Your frontend is LIVE!**

**Click the URL to see your site!**

---

## PART 7: Deploy Backend to Railway

### Step 7.1: Go to Railway

**In your browser, go to:**
```
https://railway.app
```

---

### Step 7.2: Sign In

**Click "Start a New Project"**

**Click "Login with GitHub"**

**Authorize Railway**

---

### Step 7.3: Create New Project

**Click "New Project"**

**Click "Deploy from GitHub repo"**

**Find `lurantis` in the list**

**Click it**

**Railway will start deploying automatically**

---

### Step 7.4: Configure Backend

**Wait for initial deployment to start (30 seconds)**

**Click on the service** (it will be named `lurantis` or similar)

**Go to "Settings" tab**

**Find "Root Directory":**
- **Click "Edit"**
- **Type:** `backend`
- **Click "Save"**

---

### Step 7.5: Set Start Command

**Still in Settings, find "Start Command":**

**Click "Edit"**

**Type:**
```
uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT
```

**Click "Save"**

---

### Step 7.6: Add Environment Variables

**Go to "Variables" tab**

**Click "New Variable" for each:**

**1. `QDRANT_URL`:**
   - **Name:** `QDRANT_URL`
   - **Value:** Your Qdrant Cloud URL (e.g., `https://xxxxx.qdrant.io`)
   - **Click "Add"**

**2. `QDRANT_API_KEY`** (if using Qdrant Cloud):
   - **Name:** `QDRANT_API_KEY`
   - **Value:** Your Qdrant API key
   - **Click "Add"**

**3. `GNOSIS_RPC_URL`:**
   - **Name:** `GNOSIS_RPC_URL`
   - **Value:** `https://rpc.gnosischain.com`
   - **Click "Add"**

---

### Step 7.7: Wait for Deployment

**Go to "Deployments" tab**

**Watch the logs** (it will show build progress)

**Wait 2-5 minutes**

**When you see:** ✅ "Deploy successful"

**✅ Backend is LIVE!**

---

### Step 7.8: Get Backend URL

**Go to "Settings" tab**

**Scroll to "Domains" section**

**You'll see:** `https://lurantis-production-xxxx.up.railway.app`

**Copy this URL!** This is your backend API URL.

---

## PART 8: Connect Frontend to Backend

### Step 8.1: Update Frontend Environment Variable

**Go back to Vercel** (vercel.com)

**Click on your `lurantis` project**

**Go to "Settings" → "Environment Variables"**

**Find `NEXT_PUBLIC_API_URL`**

**Click the three dots** (⋮) → **"Edit"**

**Change value to:** Your Railway backend URL
- Example: `https://lurantis-production-xxxx.up.railway.app`

**Click "Save"**

---

### Step 8.2: Redeploy Frontend

**Go to "Deployments" tab**

**Click the three dots** (⋮) on the latest deployment

**Click "Redeploy"**

**Click "Redeploy" again** (confirm)

**Wait 1-2 minutes**

**✅ Frontend now connected to backend!**

---

## PART 9: Test Everything

### Step 9.1: Test Frontend

**Go to your Vercel URL:**
```
https://lurantis-xxxxx.vercel.app
```

**You should see:**
- Your landing page
- All sections loading
- No errors

**✅ Frontend works!**

---

### Step 9.2: Test Backend API

**Go to your Railway backend URL + `/docs`:**
```
https://lurantis-production-xxxx.up.railway.app/docs
```

**You should see:**
- FastAPI Swagger UI documentation
- List of API endpoints

**✅ Backend works!**

---

### Step 9.3: Test API Docs Link

**Go back to your Vercel site**

**Scroll to footer**

**Click "API Docs"**

**Should open:** Your Railway backend `/docs` page in new tab

**✅ API Docs link works!**

---

## 🎉 DONE!

**Your site is now live!**

**Frontend:** `https://lurantis-xxxxx.vercel.app`  
**Backend:** `https://lurantis-production-xxxx.up.railway.app`  
**API Docs:** `https://lurantis-production-xxxx.up.railway.app/docs`

---

## Troubleshooting

### Command Prompt Issues

**"The system cannot find the path specified"**
- Check you typed the path correctly
- Use: `cd C:\Users\valoo\Documents\social-engineering-analyzer` (full path)

**"git is not recognized"**
- Git is not installed
- Install from: https://git-scm.com/download/win
- Restart Command Prompt after installation

**Can't paste in Command Prompt**
- Right-click in the window
- Or: `Shift + Insert`

---

### Git Issues

**"Authentication failed"**
- Use Personal Access Token, not password
- See Step 5.3 for how to create one

**"Repository not found"**
- Check repository name is correct
- Check GitHub username is correct
- Make sure repository exists on GitHub

---

### Vercel Issues

**Build fails**
- Check Root Directory is set to `frontend`
- Check all environment variables are set
- Check build logs for specific errors

**Site shows errors**
- Check browser console (F12)
- Check environment variables are correct
- Make sure backend is deployed and running

---

### Railway Issues

**Deployment fails**
- Check Root Directory is set to `backend`
- Check Start Command is correct
- Check environment variables are set
- Check logs for specific errors

**Backend not accessible**
- Check deployment is successful
- Check URL is correct
- Check environment variables

---

## Quick Command Reference

```cmd
# Clear screen
cls

# Navigate to project
cd C:\Users\valoo\Documents\social-engineering-analyzer

# Check location
cd

# List files
dir

# Git commands
git --version
git init
git status
git add .
git commit -m "message"
git remote add origin https://github.com/USERNAME/repo.git
git push -u origin main
```

---

**That's it! Follow these steps exactly and you'll have a live site!** 🚀

