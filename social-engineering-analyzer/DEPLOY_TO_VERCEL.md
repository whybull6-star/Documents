# ⚡ Quick Deploy to Vercel

**For detailed step-by-step guide, see: [STEP_BY_STEP_DEPLOY.md](./STEP_BY_STEP_DEPLOY.md)**

## 1. Push to GitHub

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/lurantis.git
git branch -M main
git push -u origin main
```

**Note**: If asked for password, use a Personal Access Token (see GIT_SETUP.md)

## 2. Deploy Frontend to Vercel

1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New Project"
4. Import your repo
5. **IMPORTANT**: Set **Root Directory** to `frontend`
6. Add environment variables:
   - `NEXT_PUBLIC_API_URL` (your backend URL)
   - `NEXT_PUBLIC_CONTRACT_ADDRESS`
   - `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`
   - `NEXT_PUBLIC_GNOSIS_RPC`
7. Deploy!

## 3. Deploy Backend (Railway - Easiest)

1. Go to https://railway.app
2. Sign in with GitHub
3. New Project → Deploy from GitHub
4. Select repo, set root to `backend`
5. Add env vars (QDRANT_URL, QDRANT_API_KEY, etc.)
6. Deploy!

## 4. Update API URL

In Vercel dashboard, update `NEXT_PUBLIC_API_URL` to your Railway backend URL.

## API Docs

The footer "API Docs" link automatically points to:
```
https://your-backend-url.com/docs
```

FastAPI auto-generates Swagger UI docs at `/docs`!

---

**That's it!** Your site will be live on Vercel! 🚀

