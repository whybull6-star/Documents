# 🚀 Deploy to Vercel - Complete Guide

## Overview

This guide will help you deploy the **frontend** to Vercel. The backend (FastAPI) needs to be hosted separately (see options below).

---

## Step 1: Push to GitHub

1. **Initialize Git** (if not already done):
   ```bash
   cd social-engineering-analyzer
   git init
   git add .
   git commit -m "Initial commit - Lurantis project"
   ```

2. **Create GitHub Repository**:
   - Go to https://github.com/new
   - Create a new repository (e.g., `lurantis`)
   - **Don't** initialize with README (you already have one)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/lurantis.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Deploy Frontend to Vercel

1. **Go to Vercel**: https://vercel.com
2. **Sign in** with GitHub
3. **Click "Add New Project"**
4. **Import your repository** (`lurantis`)
5. **Configure Project**:
   - **Framework Preset**: Next.js (auto-detected)
   - **Root Directory**: `frontend` (IMPORTANT!)
   - **Build Command**: `npm run build` (default)
   - **Output Directory**: `.next` (default)

6. **Environment Variables** (Add these):
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.com
   NEXT_PUBLIC_CONTRACT_ADDRESS=0x...
   NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0x...
   NEXT_PUBLIC_GNOSIS_RPC=https://rpc.gnosischain.com
   ```

7. **Click "Deploy"**

---

## Step 3: Deploy Backend (FastAPI)

Vercel doesn't support long-running Python servers well. You have these options:

### Option A: Railway (Recommended - Easiest)
1. Go to https://railway.app
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Set root directory to `backend`
6. Add environment variables:
   ```
   QDRANT_URL=your-qdrant-url
   QDRANT_API_KEY=your-api-key
   GNOSIS_RPC_URL=https://rpc.gnosischain.com
   ```
7. Railway auto-detects Python and deploys!

### Option B: Render
1. Go to https://render.com
2. Sign in with GitHub
3. Click "New" → "Web Service"
4. Connect your repository
5. Set:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app_enhanced:app --host 0.0.0.0 --port $PORT`
6. Add environment variables
7. Deploy!

### Option C: Fly.io
1. Install Fly CLI: https://fly.io/docs/getting-started/installing-flyctl/
2. In `backend/` directory:
   ```bash
   fly launch
   ```
3. Follow prompts
4. Deploy!

---

## Step 4: Update Frontend Environment Variables

After backend is deployed:

1. **Go to Vercel Dashboard**
2. **Select your project**
3. **Go to Settings → Environment Variables**
4. **Update** `NEXT_PUBLIC_API_URL` to your backend URL:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.railway.app
   ```
5. **Redeploy** (Vercel will auto-redeploy)

---

## Step 5: API Docs Link

The API docs link in the footer will automatically point to:
```
https://your-backend-url.com/docs
```

This is FastAPI's auto-generated Swagger UI documentation.

---

## File Structure for Vercel

```
social-engineering-analyzer/
├── frontend/          ← Deploy this to Vercel
│   ├── app/
│   ├── components/
│   ├── vercel.json    ← Vercel config
│   └── package.json
├── backend/           ← Deploy separately (Railway/Render/Fly.io)
│   ├── app_enhanced.py
│   └── requirements.txt
└── .gitignore         ← Git ignore file
```

---

## Quick Checklist

- [ ] Push code to GitHub
- [ ] Deploy frontend to Vercel (root: `frontend`)
- [ ] Deploy backend to Railway/Render/Fly.io
- [ ] Set environment variables in both
- [ ] Update `NEXT_PUBLIC_API_URL` in Vercel
- [ ] Test API docs link (should work automatically)

---

## Custom Domain (Optional)

1. **In Vercel Dashboard**:
   - Go to Settings → Domains
   - Add your domain (e.g., `lurantis.com`)
   - Follow DNS instructions

2. **Update Environment Variables**:
   - Update `NEXT_PUBLIC_API_URL` if needed
   - Redeploy

---

## Troubleshooting

### Frontend can't connect to backend
- Check `NEXT_PUBLIC_API_URL` is correct
- Check backend CORS settings allow your Vercel domain
- Check backend is actually running

### API Docs not loading
- Make sure backend is deployed and accessible
- Check URL: `https://your-backend-url.com/docs`
- FastAPI auto-generates docs at `/docs` endpoint

### Build fails on Vercel
- Check root directory is set to `frontend`
- Check all dependencies in `package.json`
- Check build logs in Vercel dashboard

---

## What Gets Deployed Where

| Component | Platform | Root Directory |
|-----------|----------|----------------|
| Frontend (Next.js) | Vercel | `frontend/` |
| Backend (FastAPI) | Railway/Render/Fly.io | `backend/` |
| Smart Contracts | Gnosis Chain | Already deployed |
| Qdrant | Qdrant Cloud | Already set up |

---

## Environment Variables Reference

### Frontend (Vercel)
```
NEXT_PUBLIC_API_URL=https://your-backend.railway.app
NEXT_PUBLIC_CONTRACT_ADDRESS=0x...
NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0x...
NEXT_PUBLIC_GNOSIS_RPC=https://rpc.gnosischain.com
```

### Backend (Railway/Render/Fly.io)
```
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-api-key
GNOSIS_RPC_URL=https://rpc.gnosischain.com
```

---

## Done! 🎉

Your site should now be live at:
- **Frontend**: `https://your-project.vercel.app`
- **Backend API**: `https://your-backend.railway.app`
- **API Docs**: `https://your-backend.railway.app/docs`

