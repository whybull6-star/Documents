# 🚀 START HERE - Copy-Paste Commands

## Where to Run These Commands

**Open your terminal/command prompt:**
- **Windows**: Press `Win + R`, type `cmd` or `powershell`, press Enter
- **Mac**: Press `Cmd + Space`, type `Terminal`, press Enter
- **Linux**: Press `Ctrl + Alt + T`

---

## Step-by-Step Commands

### Step 1: Navigate to Your Project

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer
```

*(Adjust the path if your project is in a different location)*

---

### Step 2: Start Qdrant (Docker)

**Open a NEW terminal window** and run:

```bash
docker run -d -p 6333:6333 --name qdrant qdrant/qdrant
```

**Wait for it to download and start** (first time only, ~100MB download)

**Verify it's running:**
```bash
curl http://localhost:6333/health
```

You should see: `{"status":"ok"}`

---

### Step 3: Set Up Backend

**In your original terminal**, run these commands one by one:

```bash
cd backend
```

```bash
python -m venv venv
```

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

*(You should see `(venv)` appear in your terminal prompt)*

```bash
pip install -r requirements.txt
```

*(This will take a few minutes - downloads ~500MB of dependencies)*

---

### Step 4: Create Environment File

**Still in the `backend` folder**, create a `.env` file:

**Windows (PowerShell):**
```powershell
echo "QDRANT_URL=http://localhost:6333" > .env
```

**Windows (Command Prompt):**
```cmd
echo QDRANT_URL=http://localhost:6333 > .env
```

**Mac/Linux:**
```bash
echo "QDRANT_URL=http://localhost:6333" > .env
```

**OR manually create it:**
1. Create a new file named `.env` in the `backend` folder
2. Add this line: `QDRANT_URL=http://localhost:6333`
3. Save it

---

### Step 5: Seed the Database

**Still in the `backend` folder with venv activated**, run:

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

### Step 6: Start the Backend Server

**Still in the `backend` folder with venv activated**, run:

```bash
python app_enhanced.py
```

**You should see:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal window open!** The server needs to keep running.

---

### Step 7: Test It (New Terminal)

**Open a NEW terminal window** and test:

```bash
curl http://localhost:8000/health
```

**Or test with a real threat:**
```bash
curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d "{\"content\": \"URGENT: Your wallet is compromised!\"}"
```

---

## 🎯 Quick Reference - All Commands in Order

**Terminal 1 (Qdrant):**
```bash
docker run -d -p 6333:6333 --name qdrant qdrant/qdrant
```

**Terminal 2 (Backend Setup):**
```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
echo "QDRANT_URL=http://localhost:6333" > .env
python scripts/seed_enhanced_patterns.py
python app_enhanced.py
```

**Terminal 3 (Testing):**
```bash
curl http://localhost:8000/health
```

---

## ✅ Success Checklist

- [ ] Qdrant is running (check with `curl http://localhost:6333/health`)
- [ ] Virtual environment created and activated (see `(venv)` in prompt)
- [ ] Dependencies installed (no errors)
- [ ] `.env` file created in `backend/` folder
- [ ] Database seeded (20 patterns added)
- [ ] Backend server running (see "Uvicorn running on http://0.0.0.0:8000")
- [ ] Health check works (`curl http://localhost:8000/health`)

---

## 🐛 Common Issues

### "docker: command not found"
- Install Docker Desktop: https://www.docker.com/products/docker-desktop
- Restart your computer after installing

### "python: command not found"
- Install Python 3.8+: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### "pip: command not found"
- Python might not be in your PATH
- Try: `python -m pip install -r requirements.txt`

### Port 6333 or 8000 already in use
- Stop other services using those ports
- Or change ports in `.env` and `app_enhanced.py`

---

## 📚 Next Steps

Once everything is running:
1. Read the full guide: [QDRANT_QUICKSTART.md](./QDRANT_QUICKSTART.md)
2. Test the API: [QDRANT_QUICKSTART.md#step-5-test-the-api](./QDRANT_QUICKSTART.md#step-5-test-the-api)
3. Integrate with frontend

---

**Need help?** Check the troubleshooting section in [QDRANT_QUICKSTART.md](./QDRANT_QUICKSTART.md)

