# ⚡ Quick Deploy - Final Push

## 1. Push to Git

```cmd
cd C:\Users\valoo\Documents\social-engineering-analyzer
git add .
git commit -m "Final deployment ready: Enhanced UI, sourced patterns, polished design"
git push origin main
```

---

## 2. Deploy Frontend (Vercel)

1. Go to: https://vercel.com
2. Import GitHub repo `lurantis`
3. **Set Root Directory**: `frontend`
4. Add env vars:
   - `NEXT_PUBLIC_API_URL` (update after backend deploys)
   - `NEXT_PUBLIC_GNOSIS_RPC` = `https://rpc.gnosischain.com`
5. Deploy!

**Frontend URL**: `https://lurantis-xxxxx.vercel.app`

---

## 3. Deploy Backend (Railway)

1. Go to: https://railway.app
2. New Project → Deploy from GitHub
3. Select `lurantis` repo
4. **Set Root Directory**: `backend`
5. **Set Start Command**: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
6. Add env vars:
   - `QDRANT_URL` (your Qdrant Cloud URL)
   - `QDRANT_API_KEY` (if using Cloud)
   - `GNOSIS_RPC_URL` = `https://rpc.gnosischain.com`
7. Deploy!

**Backend URL**: `https://lurantis-production-xxxx.up.railway.app`

---

## 4. Connect Frontend to Backend

1. In Vercel: Settings → Environment Variables
2. Update `NEXT_PUBLIC_API_URL` to your Railway backend URL
3. Redeploy frontend

---

## 5. Test

- Frontend: Visit your Vercel URL
- Backend: Visit `https://your-backend-url/docs`
- Wallet Analysis: Test with `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`

---

## For Judges

**Share these URLs:**
- Frontend: `https://lurantis-xxxxx.vercel.app`
- API Docs: `https://lurantis-production-xxxx.up.railway.app/docs`
- GitHub: `https://github.com/YOUR_USERNAME/lurantis`

**✅ Done!** 🚀
