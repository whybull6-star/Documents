# Correct Commands - You're Already in the Right Place!

## You're Currently Here:
```
C:\Users\valoo\Documents\social-engineering-analyzer>
```

## Just Run These:

### Step 1: Go into Backend Folder

```cmd
cd backend
```

**Press Enter**

**You should now see:**
```
C:\Users\valoo\Documents\social-engineering-analyzer\backend>
```

---

### Step 2: Install Dependencies (If Needed)

```cmd
pip install -r requirements.txt
```

**Press Enter and wait**

**Skip this if you already installed before**

---

### Step 3: Start Backend

```cmd
python -m uvicorn app_enhanced:app --reload --port 8000
```

**Press Enter**

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**✅ Backend is now running!**

**KEEP THIS WINDOW OPEN!**

---

## Test Backend

**Open browser:**
```
http://localhost:8000/health
```

**Should see JSON response!**

---

## Then Start Frontend

**Open NEW Command Prompt:**

```cmd
cd Documents\social-engineering-analyzer\frontend
npm run dev
```

**Then open:**
```
http://localhost:3000
```

---

## Summary

**From where you are now (`social-engineering-analyzer`):**

1. `cd backend`
2. `python -m uvicorn app_enhanced:app --reload --port 8000`
3. Keep window open!
4. Test: `http://localhost:8000/health`
5. Open NEW terminal for frontend

