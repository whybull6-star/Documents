# How to Add Files to GitHub Desktop

## Step-by-Step Guide

---

## STEP 1: Open GitHub Desktop

1. **Open GitHub Desktop** from Start Menu
   - Search for "GitHub Desktop" in Windows search
   - Click to open

2. **Make sure you're signed in:**
   - Top right should show your GitHub username
   - If not signed in, click "Sign in to GitHub.com"

---

## STEP 2: Add Your Project Folder

### Option A: Using "Add Local Repository" (Easiest)

1. **In GitHub Desktop:**
   - Click **"File"** (top left)
   - Click **"Add Local Repository"**

2. **Browse to your project:**
   - Click **"Choose..."** button
   - Navigate to: `C:\Users\valoo\Documents`
   - Find folder: `social-engineering-analyzer`
   - **Select the folder** (click once on `social-engineering-analyzer`)
   - Click **"Select Folder"** button

3. **If GitHub Desktop says "This directory does not appear to be a Git repository":**
   - Click **"create a repository"** link
   - OR check box: **"I understand this will create a new repository"**
   - Click **"Add Repository"**

✅ **Your project is now added!**

---

### Option B: Drag and Drop (Alternative)

1. **Open File Explorer**
   - Go to: `C:\Users\valoo\Documents\social-engineering-analyzer`

2. **In GitHub Desktop:**
   - Click **"File"** → **"Add Local Repository"**

3. **Drag your folder:**
   - **Drag** the `social-engineering-analyzer` folder
   - **Drop it** into the GitHub Desktop window

✅ **Folder added!**

---

## STEP 3: See Your Files

**After adding, you should see:**

1. **Left side of GitHub Desktop:**
   - **"Changes"** tab (selected)
   - **All your files listed** with checkboxes ☑️

2. **Right side:**
   - Shows file changes (if any)
   - Or preview of files

---

## STEP 4: Check All Files Are Selected

**In the "Changes" tab:**

1. **Look at the left side:**
   - Each file should have a **checkbox** ☑️
   - **Make sure all are checked** (selected)

2. **If files are NOT checked:**
   - **Click each checkbox** to check them
   - OR **Right-click** → **"Select All"** (if available)

3. **You should see:**
   - ✅ `frontend/` folder (with files inside)
   - ✅ `backend/` folder (with files inside)
   - ✅ `contracts/` folder
   - ✅ `README.md`
   - ✅ All documentation files (`.md` files)
   - ✅ All other project files

---

## STEP 5: Commit Files

**Bottom left of GitHub Desktop:**

1. **Summary (required):**
   ```
   Initial commit: Lurantis project with Qdrant integration
   ```

2. **Description (optional):**
   ```
   Complete social engineering detection platform
   - Frontend with Next.js and Tailwind CSS
   - Backend with FastAPI and Qdrant integration
   - 33 attack patterns across 5 collections
   - Real transaction analysis from Gnosis Chain
   ```

3. **Click "Commit to main"** button (bottom left)

4. **Wait for commit to complete:**
   - You'll see: "Committed to main"
   - ✅ **Files committed!**

---

## STEP 6: Publish to GitHub

**After committing:**

1. **Top center of GitHub Desktop:**
   - You should see button: **"Publish repository"**
   - OR **"Push origin"** (if repo already exists)

2. **Click "Publish repository"**

3. **If popup appears:**
   - **Name:** `lurantis` (or whatever you want)
   - **Description:** (optional) "Qdrant-leveraged social engineering detection platform"
   - **☑️ Keep this code private:** 
     - **Uncheck** if you want public (for judges)
     - **Check** if you want private
   - **Click "Publish Repository"**

4. **Wait for push:**
   - You'll see: "Pushing to origin/main..."
   - Then: "Successfully pushed to GitHub"
   - ✅ **Code is on GitHub!**

---

## What Your GitHub Desktop Should Look Like

### Before Publishing:
```
┌─────────────────────────────────────┐
│  GitHub Desktop                     │
├─────────────────────────────────────┤
│  File  Edit  View  Branch  Help     │
│                                     │
│  [Current repository: ]  [Publish]  │
│                                     │
│  ┌─────────┬──────────────────────┐ │
│  │ Changes │  File preview        │ │
│  │         │                      │ │
│  │ ☑ frontend/                   │ │
│  │ ☑ backend/                    │ │
│  │ ☑ contracts/                  │ │
│  │ ☑ README.md                   │ │
│  │ ☑ *.md files                  │ │
│  │                               │ │
│  │ [Commit message...]           │ │
│  │ [Commit to main]              │ │
│  └─────────┴──────────────────────┘ │
└─────────────────────────────────────┘
```

### After Publishing:
```
┌─────────────────────────────────────┐
│  GitHub Desktop                     │
├─────────────────────────────────────┤
│  [Current repository: lurantis]     │
│  [Fetch origin] [Pull] [Push]       │
│                                     │
│  ✅ Successfully pushed to GitHub   │
└─────────────────────────────────────┘
```

---

## Troubleshooting

### "This directory does not appear to be a Git repository"

**Solution:**
1. In the popup, click **"create a repository"** link
2. OR check box: **"I understand this will create a new repository"**
3. Click **"Add Repository"**

---

### "No changes to commit"

**Solution:**
1. Make sure files are checked (☑️) in "Changes" tab
2. If no files showing:
   - Try refreshing: **File** → **"Refresh"**
   - OR remove and re-add the repository

---

### Can't Find Your Folder

**Make sure you're navigating to:**
```
C:\Users\valoo\Documents\social-engineering-analyzer
```

**Steps:**
1. Open File Explorer
2. Go to: `C:\Users\valoo\Documents`
3. Look for: `social-engineering-analyzer` folder
4. If it doesn't exist, let me know!

---

### Files Not Showing Up

**Check:**
1. Make sure you selected the **`social-engineering-analyzer`** folder (not parent folder)
2. Check `.gitignore` file - it might be ignoring some files (this is OK)
3. Try refreshing: **View** → **"Refresh"** or press `F5`

---

## Quick Reference

**Your Project Path:**
```
C:\Users\valoo\Documents\social-engineering-analyzer
```

**GitHub Desktop Steps:**
1. File → Add Local Repository
2. Browse → Select `social-engineering-analyzer` folder
3. Check all files
4. Write commit message
5. Commit to main
6. Publish repository

---

## Next Steps

After publishing to GitHub:
1. ✅ Go to: https://github.com/YOUR_USERNAME/lurantis
2. ✅ Verify all files are there
3. ✅ Continue with Vercel deployment (see `COMPLETE_DEPLOYMENT_FROM_SCRATCH.md`)

---

**Need more help?** Tell me which step you're stuck on!

