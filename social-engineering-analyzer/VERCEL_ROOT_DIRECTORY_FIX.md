# How to Set Root Directory in Vercel

## Quick Fix

**You CAN see the Root Directory option!** It's right there in your form.

---

## Step-by-Step:

### Step 1: Find "Root Directory" Section

**Look for this section in your Vercel form:**
- **"Root Directory"** ← This section exists!
- Current value: `social-engineering-analyzer`
- **"Edit" button** next to it

---

### Step 2: Click "Edit" Button

1. **Find the "Root Directory" field**
   - It shows: `social-engineering-analyzer`
   - **Click the "Edit" button** (to the right of the field)

---

### Step 3: Change Root Directory

**After clicking "Edit":**

1. **The field becomes editable**

2. **Change it FROM:**
   ```
   social-engineering-analyzer
   ```

3. **Change it TO:**
   ```
   social-engineering-analyzer/frontend
   ```

4. **OR try just:**
   ```
   frontend
   ```
   (Vercel might accept relative path)

5. **Click outside the field or press Enter** to save

---

### Step 4: Verify Framework Preset

**Also check "Framework Preset" section:**

1. **Current value:** `Other` (dropdown)

2. **Click the dropdown**

3. **Select:** `Next.js`

4. **This should auto-detect** your Next.js app

---

### Step 5: Update Project Name (Optional)

**Project Name field:**
- Currently shows: `documents`
- **Change to:** `lurantis` (or whatever you want)

---

### Step 6: Deploy

**Click the "Deploy" button** at the bottom

**Vercel will:**
1. Look in `social-engineering-analyzer/frontend/` folder
2. Detect Next.js
3. Install dependencies
4. Build and deploy

---

## What Your Form Should Look Like:

**Before:**
```
Root Directory: social-engineering-analyzer [Edit]
Framework Preset: Other ▼
```

**After:**
```
Root Directory: social-engineering-analyzer/frontend [Edit]
Framework Preset: Next.js ▼
```

---

## If "Edit" Button Doesn't Work:

**Alternative method:**

1. **Delete the text** in Root Directory field
2. **Type:** `social-engineering-analyzer/frontend`
3. **Click outside** to save

---

## If Root Directory Field is Grayed Out:

**This might happen if:**
- Vercel auto-detected the project structure

**Solution:**
1. **Click "Edit"** (if available)
2. **OR:** Close and re-import the repository
3. **OR:** Manually type the path

---

## Important Notes:

**Your repository structure:**
```
whybull6-star/Documents (GitHub repo)
  └── social-engineering-analyzer/
      ├── frontend/          ← Next.js app is here!
      │   ├── package.json
      │   ├── app/
      │   └── ...
      ├── backend/
      └── ...
```

**Vercel needs to know:**
- Root Directory = `social-engineering-analyzer/frontend`
- This tells Vercel where your `package.json` is

---

## After Setting Root Directory:

**Vercel should auto-detect:**
- ✅ Framework: Next.js
- ✅ Build Command: `npm run build`
- ✅ Output Directory: `.next`
- ✅ Install Command: `npm install`

**All should be correct!**

---

## Troubleshooting:

### Still Can't Edit Root Directory?

**Try this:**
1. **Cancel** this deployment
2. **Go back** to "Add New Project"
3. **Re-import** your repository
4. **This time**, click "Edit" on Root Directory immediately

---

### Root Directory Shows as Empty

**Manually type:**
```
social-engineering-analyzer/frontend
```

**Make sure there's no spaces!**

---

### "Build failed" After Deploy

**Check:**
1. Root Directory is `social-engineering-analyzer/frontend` ✅
2. Framework Preset is `Next.js` ✅
3. `frontend/package.json` exists ✅

**If still failing:**
- Check Vercel build logs
- Make sure `frontend/package.json` has correct dependencies

---

## Quick Summary:

1. ✅ **Find "Root Directory"** section (it's there!)
2. ✅ **Click "Edit"** button
3. ✅ **Change to:** `social-engineering-analyzer/frontend`
4. ✅ **Set Framework Preset:** `Next.js`
5. ✅ **Click "Deploy"**

**That's it!** ✅

