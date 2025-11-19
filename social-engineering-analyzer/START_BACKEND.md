# How to Start Backend - Windows CMD

## Step 1: Navigate to Backend Folder

**In Command Prompt, run:**

```cmd
cd Documents\social-engineering-analyzer\backend
```

**Verify you're in the right place:**
```cmd
dir
```

You should see files like:
- `app_enhanced.py`
- `requirements.txt`
- `services/` folder
- etc.

---

## Step 2: Install Dependencies (First Time Only)

**Run:**

```cmd
pip install -r requirements.txt
```

**Wait for it to install** (might take a few minutes)

You should see packages installing like:
- fastapi
- uvicorn
- qdrant-client
- sentence-transformers
- web3
- etc.

---

## Step 3: Start Backend

**Run:**

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

**You should see:**
```
INFO:     Will watch for changes in these directories: ['C:\\Users\\valoo\\Documents\\social-engineering-analyzer\\backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Backend is now running!**

**Keep this window open!**

---

## Step 4: Test Backend

**Open a NEW Command Prompt and run:**

```cmd
curl http://localhost:8000/health
```

**OR open browser and go to:**
```
http://localhost:8000/health
```

**You should see JSON response!**

---

## Troubleshooting

### "The system cannot find the path specified"

**Make sure you're in the right folder:**

```cmd
# Check current folder
cd

# Should show: C:\Users\valoo

# Navigate to project
cd Documents\social-engineering-analyzer\backend

# Check you're in right place
dir app_enhanced.py
```

**If `app_enhanced.py` doesn't exist:**
- You might not be in the right folder
- Check where your project actually is

---

### "No module named uvicorn"

**You need to install dependencies:**

```cmd
cd Documents\social-engineering-analyzer\backend
pip install -r requirements.txt
```

**Wait for installation to complete!**

**Then try again:**
```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

---

### "Port 8000 already in use"

**Something else is using port 8000.**

**Find and kill it:**
```cmd
netstat -ano | findstr :8000
```

**Note the PID (last number)**

**Kill it:**
```cmd
taskkill /PID <PID_NUMBER> /F
```

**Replace `<PID_NUMBER>` with the number from netstat**

---

### "Qdrant connection failed"

**Check if Qdrant is running:**

**If using Docker:**
```cmd
docker ps | findstr qdrant
```

**If not running:**
```cmd
cd Documents\social-engineering-analyzer
docker-compose up -d
```

**If using Qdrant Cloud:**
- Check `backend\.env` file has correct `QDRANT_URL` and `QDRANT_API_KEY`

---

## Quick Copy-Paste Commands

**Copy and paste these one at a time:**

```cmd
cd Documents\social-engineering-analyzer\backend
```

```cmd
pip install -r requirements.txt
```

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

---

## After Backend Starts

**Keep that Command Prompt window open!**

**Then open NEW Command Prompt for frontend:**

```cmd
cd Documents\social-engineering-analyzer\frontend
npm install
npm run dev
```

**Then open browser:**
```
http://localhost:3000
```

---

## Summary

1. ✅ Navigate: `cd Documents\social-engineering-analyzer\backend`
2. ✅ Install: `pip install -r requirements.txt`
3. ✅ Start: `python -m uvicorn app_enhanced:app --reload --port 8000`
4. ✅ Keep window open!
5. ✅ Test: `http://localhost:8000/health`

