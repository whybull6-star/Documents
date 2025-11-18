# ⚡ Qdrant Cloud - Quick Setup (5 Minutes)

## 🎯 What You Need

1. Web browser
2. Email address
3. 5 minutes

---

## Step 1: Sign Up (2 minutes)

1. Go to: **https://cloud.qdrant.io/**
2. Click **"Sign Up"**
3. Enter your email and password
4. Verify your email (check inbox)

---

## Step 2: Create Cluster (2 minutes)

1. Click **"Create Cluster"**
2. Fill in:
   - **Name**: `lurantis` (or any name)
   - **Region**: Choose closest to you
   - **Plan**: **Free** (for testing)
3. Click **"Create"**
4. Wait ~2 minutes for it to be ready

---

## Step 3: Get Credentials (1 minute)

1. Click on your cluster name
2. Find **"Connection"** or **"API"** section
3. Copy **two things**:

   **Cluster URL:**
   ```
   https://xxxxx.us-east-1-0.aws.cloud.qdrant.io
   ```

   **API Key:**
   ```
   QDRANT_API_KEY_abc123def456...
   ```
   (Click "Show API Key" to reveal it)

---

## Step 4: Create .env File

**In your `backend` folder**, create a file named `.env`:

```
QDRANT_URL=https://your-cluster-url-here
QDRANT_API_KEY=your-api-key-here
API_URL=http://localhost:8000
```

**Replace:**
- `https://your-cluster-url-here` → Your actual cluster URL
- `your-api-key-here` → Your actual API key

**Save the file!**

---

## Step 5: Test It

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
venv\Scripts\activate
python scripts/seed_enhanced_patterns.py
```

If you see "✅ Database seeded successfully!" - you're done! 🎉

---

## ✅ Done!

Now continue with:
```bash
python app_enhanced.py
```

---

## 🆘 Need Help?

- **Can't find API key?** → Look for "API" or "Connection" tab in cluster details
- **Connection error?** → Check your `.env` file has correct URL and API key
- **More details?** → See `QDRANT_CLOUD_SETUP.md` for full guide

