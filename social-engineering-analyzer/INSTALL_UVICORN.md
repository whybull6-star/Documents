# Install uvicorn - Quick Fix

## You Need to Install Dependencies First!

### Step 1: Make Sure You're in Backend Folder

**In Command Prompt, you should see:**
```
C:\Users\valoo\Documents\social-engineering-analyzer\backend>
```

**If not, run:**
```cmd
cd backend
```

---

### Step 2: Install All Dependencies

**Run this command:**

```cmd
pip install -r requirements.txt
```

**Press Enter and WAIT** (takes 2-3 minutes)

**You should see packages installing:**
```
Collecting fastapi>=0.104.0
Collecting uvicorn[standard]>=0.24.0
Collecting qdrant-client>=1.7.1
...
Successfully installed fastapi ... uvicorn ... etc.
```

---

### Step 3: Start Backend

**After installation finishes, run:**

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

**Should work now!**

---

## Alternative: Install Just uvicorn

**If you want to install just uvicorn first:**

```cmd
pip install uvicorn fastapi
```

**Then try:**
```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

---

## If Still Getting "No module named uvicorn"

### Check Python Version

```cmd
python --version
```

**Should be Python 3.8+**

### Check if pip is working

```cmd
pip --version
```

**If pip doesn't work, try:**

```cmd
python -m pip install -r requirements.txt
```

### Install uvicorn directly

```cmd
python -m pip install uvicorn[standard] fastapi
```

---

## Quick Commands (Copy-Paste)

**Copy and paste these one at a time:**

```cmd
cd backend
```

```cmd
pip install -r requirements.txt
```

**Wait for it to finish...**

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

---

## What Should Happen

1. ✅ `pip install` runs and installs packages
2. ✅ See "Successfully installed ..."
3. ✅ Run `python -m uvicorn ...`
4. ✅ See "INFO: Uvicorn running on http://0.0.0.0:8000"
5. ✅ Backend is running!

---

## Troubleshooting

**"pip is not recognized"**
- Try: `python -m pip install -r requirements.txt`

**"Permission denied"**
- Try: `pip install --user -r requirements.txt`

**"No module named pip"**
- Install pip first or use Python's built-in pip

**Still getting "no module uvicorn" after install**
- Make sure you're using the same Python that pip installed to
- Try: `python -m pip install uvicorn` then `python -m uvicorn ...`

