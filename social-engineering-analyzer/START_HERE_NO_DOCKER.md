# 🚀 START HERE - Without Docker (Using Qdrant Cloud)

## Quick Setup Without Docker

### Step 1: Get Free Qdrant Cloud Account

1. **Sign up:**
   - Go to: https://cloud.qdrant.io/
   - Click "Sign Up" (free tier available)
   - Verify your email

2. **Create a cluster:**
   - Click "Create Cluster"
   - Choose the free tier
   - Select a region close to you
   - Wait for cluster to be created (~2 minutes)

3. **Get your credentials:**
   - Click on your cluster
   - Copy the **Cluster URL** (looks like: `https://xxxxx.us-east-1-0.aws.cloud.qdrant.io`)
   - Copy the **API Key** (click "Show API Key")

---

### Step 2: Set Up Backend

**Open your terminal/command prompt** and run:

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
```

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

*(You should see `(venv)` appear in your terminal prompt)*

```bash
pip install -r requirements.txt
```

*(This will take a few minutes - downloads ~500MB)*

---

### Step 3: Create Environment File

**Create a `.env` file in the `backend` folder:**

**Option A: Using PowerShell:**
```powershell
echo "QDRANT_URL=https://your-cluster-url.qdrant.io" > .env
echo "QDRANT_API_KEY=your-api-key-here" >> .env
```

**Option B: Manually create it:**
1. In the `backend` folder, create a new file named `.env`
2. Add these lines (replace with your actual values):
   ```
   QDRANT_URL=https://your-cluster-url.qdrant.io
   QDRANT_API_KEY=your-api-key-here
   ```
3. Save the file

---

### Step 4: Seed the Database

**Still in the `backend` folder with venv activated:**

```bash
python scripts/seed_enhanced_patterns.py
```

**Expected output:**
```
🚀 Initializing Enhanced Qdrant Service...
📊 Seeding 20 attack patterns...
  ✓ [SIM_SWAPPING] Added pattern #1001
  ...
✅ Database seeded successfully!
```

---

### Step 5: Start the Backend Server

**Still in the `backend` folder with venv activated:**

```bash
python app_enhanced.py
```

**You should see:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal window open!**

---

### Step 6: Test It

**Open a NEW terminal window** and test:

```bash
curl http://localhost:8000/health
```

**Or test with a real threat:**
```bash
curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d "{\"content\": \"URGENT: Your wallet is compromised!\"}"
```

---

## ✅ Success Checklist

- [ ] Qdrant Cloud account created
- [ ] Cluster created and running
- [ ] `.env` file created with correct URL and API key
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Database seeded (20 patterns)
- [ ] Backend server running
- [ ] Health check works

---

## 🎯 All Commands in Order

```bash
# Navigate to backend
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (replace with your Qdrant Cloud URL and API key)
echo "QDRANT_URL=https://your-cluster-url.qdrant.io" > .env
echo "QDRANT_API_KEY=your-api-key-here" >> .env

# Seed database
python scripts/seed_enhanced_patterns.py

# Start server
python app_enhanced.py
```

---

## 💡 Benefits of Qdrant Cloud

- ✅ No Docker installation needed
- ✅ Free tier available
- ✅ Managed service (no maintenance)
- ✅ Works from anywhere
- ✅ Production-ready

---

**Need to install Docker instead?** See [INSTALL_DOCKER.md](./INSTALL_DOCKER.md)

