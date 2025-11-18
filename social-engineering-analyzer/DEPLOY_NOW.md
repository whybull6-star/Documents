# 🚀 DEPLOY NOW - Step by Step

## ⚠️ FIRST: Create GitHub Repository

**If you don't have a repository yet:**

1. **Go to**: https://github.com/new
2. **Name**: `lurantis`
3. **DO NOT** check "Initialize with README"
4. **Click "Create repository"**

**OR use GitHub Desktop** (easier - see `CREATE_GITHUB_REPO.md`)

---

## ⚡ Quick Commands (Copy-Paste)

### 1. Push to Git

**If Git is NOT installed:**
- Use **GitHub Desktop** instead (see `CREATE_GITHUB_REPO.md`)
- Or install Git from: https://git-scm.com/download/win

**Open Command Prompt:**
```cmd
cd C:\Users\valoo\Documents\social-engineering-analyzer
git add .
git commit -m "Final deployment: Enhanced UI, organic blobs, network overlays, high-level docs, sourced patterns"
git push origin main
```

**If asked for password:** Use Personal Access Token (not password)

---

## 2. Deploy Frontend (Vercel)

1. **Go to**: https://vercel.com
2. **Sign in** with GitHub
3. **Click "Add New Project"**
4. **Import** `lurantis` repository
5. **IMPORTANT**: Set **Root Directory** to `frontend`
6. **Add Environment Variables**:
   - `NEXT_PUBLIC_API_URL` = `http://localhost:8000` (update later)
   - `NEXT_PUBLIC_GNOSIS_RPC` = `https://rpc.gnosischain.com`
   - `NEXT_PUBLIC_CONTRACT_ADDRESS` = (your contract if you have it)
   - `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT` = (your contract if you have it)
7. **Click "Deploy"**

**Wait 1-3 minutes** → Get URL: `https://lurantis-xxxxx.vercel.app`

---

## 3. Deploy Backend (Railway)

1. **Go to**: https://railway.app
2. **Sign in** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Select** `lurantis` repository
6. **Go to Settings**:
   - **Root Directory**: `backend`
   - **Start Command**: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
7. **Go to Variables** tab, add:
   - `QDRANT_URL` = Your Qdrant Cloud URL (or `http://localhost:6333`)
   - `QDRANT_API_KEY` = Your Qdrant API key (if using Cloud)
   - `GNOSIS_RPC_URL` = `https://rpc.gnosischain.com`
8. **Wait 2-5 minutes** for deployment

**Get Backend URL**: `https://lurantis-production-xxxx.up.railway.app`

---

## 4. Connect Frontend to Backend

1. **Go back to Vercel**
2. **Settings** → **Environment Variables**
3. **Edit** `NEXT_PUBLIC_API_URL`
4. **Change to**: Your Railway backend URL
5. **Save**
6. **Redeploy** (Deployments → Three dots → Redeploy)

---

## 5. Test & Share

**Test:**
- Frontend: Visit your Vercel URL
- Backend: Visit `https://your-backend-url/docs`
- Wallet Analysis: Test with any wallet address

**For Judges:**
- Frontend URL: `https://lurantis-xxxxx.vercel.app`
- API Docs: `https://lurantis-production-xxxx.up.railway.app/docs`
- GitHub: `https://github.com/YOUR_USERNAME/lurantis`

---

## ✅ Done!

**Your site is live and ready for judges!** 🎉

