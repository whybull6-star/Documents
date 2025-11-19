# Start Backend - Copy These Commands

## Step 1: Navigate to Backend Folder

**In Command Prompt, type:**

```cmd
cd social-engineering-analyzer\backend
```

**Press Enter**

**Verify (optional):**
```cmd
dir app_enhanced.py
```

**Should show:** `app_enhanced.py`

---

## Step 2: Activate Virtual Environment (Optional but Recommended)

**If you have a venv folder:**

```cmd
venv\Scripts\activate
```

**You should see:** `(venv)` at the start of your prompt

**If no venv, skip to Step 3**

---

## Step 3: Install Dependencies (If Not Already Done)

```cmd
pip install -r requirements.txt
```

**Wait for it to finish** (might take 2-3 minutes)

**You should see:** `Successfully installed ...` at the end

---

## Step 4: Start Backend

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**✅ Backend is now running!**

**KEEP THIS WINDOW OPEN!**

---

## Step 5: Test It

**Open a NEW Command Prompt and run:**

```cmd
curl http://localhost:8000/health
```

**OR open your browser and go to:**
```
http://localhost:8000/health
```

**You should see JSON response!**

---

## Full Command Sequence (Copy-Paste)

**Copy and paste these one at a time:**

```cmd
cd social-engineering-analyzer\backend
```

```cmd
pip install -r requirements.txt
```

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

---

## If "No module named uvicorn" Error

**Run this first:**
```cmd
pip install uvicorn fastapi qdrant-client sentence-transformers web3 python-dotenv
```

**Then try again:**
```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

---

## After Backend Starts

**Keep that Command Prompt window running!**

**Then open NEW Command Prompt for frontend:**

```cmd
cd Documents\social-engineering-analyzer\frontend
npm run dev
```

**Then open browser:**
```
http://localhost:3000
```

---

## Troubleshooting

**"The system cannot find the path specified"**
- Make sure you're in `C:\Users\valoo\Documents` first
- Then: `cd social-engineering-analyzer\backend`

**"No module named uvicorn"**
- Run: `pip install -r requirements.txt`
- Or: `pip install uvicorn fastapi`

**"Port 8000 already in use"**
- Something else is using port 8000
- Kill it: `netstat -ano | findstr :8000` then `taskkill /PID <PID> /F`

**Backend starts but shows errors**
- Check if Qdrant is running
- Check `backend\.env` file exists
- Look at the error message in the terminal

