# Final Deploy Checklist - Step by Step

## ✅ PRE-DEPLOYMENT CHECKLIST

- [ ] Backend works locally (`http://localhost:8000/health` returns JSON)
- [ ] Frontend works locally (`http://localhost:3000` loads)
- [ ] Wallet analysis works locally
- [ ] Qdrant is connected and working
- [ ] All sensitive data removed from code (API keys, etc.)
- [ ] `.env` files in `.gitignore`

---

## STEP 1: GATHER QDRANT PROOF

### Files to Include in Pitch Deck:

1. ✅ `QDRANT_PITCH_DECK_PROOF.md` - Main proof document
2. ✅ `PITCH_DECK_QDRANT_DATA.json` - Formatted data
3. ✅ `backend/data/attack_patterns.json` - JSON database
4. ✅ `DATA_SOURCES_PROOF.md` - Source verification
5. ✅ Screenshots of code files:
   - `backend/services/enhanced_qdrant_service.py`
   - `backend/services/onchain_analyzer.py`

**All files are ready!** ✅

---

## STEP 2: PUSH TO GITHUB

### Option A: Using GitHub Desktop

1. **Open GitHub Desktop**

2. **Make sure repository is selected:**
   - Should show: `whybull6-star/lurantis`
   - If not, add repository: File → Add Local Repository

3. **Check Changes:**
   - Should see all your files
   - All should be checked (staged)

4. **Write Commit Message:**
   ```
   Final deployment: Qdrant integration, wallet analysis, enhanced UI
   ```

5. **Click "Commit to main"**

6. **Click "Push origin"** (or "Publish branch")

7. **Verify:**
   - Go to: https://github.com/whybull6-star/lurantis
   - Should see all files

### Option B: Create New Repository

**If repo doesn't exist:**

1. **Go to:** https://github.com/new
2. **Name:** `lurantis`
3. **Public:** Yes (for judges)
4. **Create repository**

**Then in GitHub Desktop:**

1. **File → Add Local Repository**
2. **Browse to:** `C:\Users\valoo\Documents\social-engineering-analyzer`
3. **Publish to GitHub**

---

## STEP 3: DEPLOY FRONTEND TO VERCEL

1. **Go to:** https://vercel.com
2. **Sign in with GitHub**
3. **Click "Add New Project"**
4. **Import:** `whybull6-star/lurantis`
5. **Root Directory:** `frontend` ← **IMPORTANT!**
6. **Framework:** Next.js (auto-detected)
7. **Environment Variables:**
   - `NEXT_PUBLIC_API_URL` = `http://localhost:8000` (update later)
   - `NEXT_PUBLIC_GNOSIS_RPC` = `https://rpc.gnosischain.com`
8. **Click "Deploy"**
9. **Wait 2-3 minutes**
10. **Copy URL:** `https://lurantis-xxxxx.vercel.app`

**✅ Frontend deployed!**

---

## STEP 4: DEPLOY BACKEND TO RAILWAY

1. **Go to:** https://railway.app
2. **Sign in with GitHub**
3. **Click "New Project"**
4. **Deploy from GitHub repo:** `whybull6-star/lurantis`
5. **Settings:**
   - **Root Directory:** `backend`
   - **Start Command:** `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
6. **Variables:**
   - `QDRANT_URL` = Your Qdrant Cloud URL
   - `QDRANT_API_KEY` = Your Qdrant API key
   - `GNOSIS_RPC_URL` = `https://rpc.gnosischain.com`
7. **Click "Deploy"**
8. **Wait 2-3 minutes**
9. **Copy URL:** `https://lurantis-production-xxxx.up.railway.app`

**✅ Backend deployed!**

---

## STEP 5: CONNECT FRONTEND TO BACKEND

1. **Go to Vercel Dashboard**
2. **Your Project → Settings → Environment Variables**
3. **Edit** `NEXT_PUBLIC_API_URL`
4. **Change to:** Your Railway backend URL
5. **Save**
6. **Deployments → Redeploy**

**✅ Connected!**

---

## STEP 6: TEST EVERYTHING

**Test Frontend:**
- [ ] Open Vercel URL
- [ ] Site loads correctly
- [ ] Wallet connection works
- [ ] Wallet analysis works

**Test Backend:**
- [ ] Open Railway URL/health
- [ ] Returns JSON
- [ ] API docs work: `/docs`

**Test Integration:**
- [ ] Wallet analysis calls backend
- [ ] Risk scores appear
- [ ] Charts display correctly

---

## STEP 7: PREPARE FOR JUDGES

### Make Repository Public:

1. **Go to:** https://github.com/whybull6-star/lurantis/settings
2. **Danger Zone → Change visibility**
3. **Make public**

### Update README:

**Add to `README.md`:**

```markdown
## Live Demo
- **Frontend:** https://lurantis-xxxxx.vercel.app
- **Backend API:** https://lurantis-production-xxxx.up.railway.app
- **API Docs:** https://lurantis-production-xxxx.up.railway.app/docs

## Qdrant Integration
See `QDRANT_PITCH_DECK_PROOF.md` for complete documentation.

33 attack patterns across 5 specialized collections using 768-dimensional vector search.
```

---

## QUICK COMMAND REFERENCE

### GitHub Desktop:
1. Open GitHub Desktop
2. Select repository
3. Check all files
4. Commit: "Final deployment: Qdrant integration, wallet analysis"
5. Push origin

### Vercel:
1. https://vercel.com → Add Project
2. Import `whybull6-star/lurantis`
3. Root: `frontend`
4. Deploy

### Railway:
1. https://railway.app → New Project
2. Import `whybull6-star/lurantis`
3. Root: `backend`
4. Start: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
5. Add environment variables
6. Deploy

---

## YOUR FINAL URLs

**After deployment:**

- **Frontend:** `https://lurantis-xxxxx.vercel.app`
- **Backend:** `https://lurantis-production-xxxx.up.railway.app`
- **API Docs:** `https://lurantis-production-xxxx.up.railway.app/docs`
- **GitHub:** `https://github.com/whybull6-star/lurantis`

**Share these with judges!**

---

## PITCH DECK MATERIALS READY

✅ `QDRANT_PITCH_DECK_PROOF.md` - Complete Qdrant documentation  
✅ `PITCH_DECK_QDRANT_DATA.json` - Formatted data  
✅ `QDRANT_PROOF.md` - Technical proof  
✅ `DATA_SOURCES_PROOF.md` - Source verification  
✅ `backend/data/attack_patterns.json` - JSON database  

**All ready for your pitch deck!** 🎯

