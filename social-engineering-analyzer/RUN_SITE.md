# 🚀 How to Run the Site

## Step 1: Backend is Running ✅
You already have this running! Keep that terminal open.

---

## Step 2: Start Frontend (New Terminal)

**Open a NEW Command Prompt or PowerShell window** (keep backend running in the first one)

### Navigate to frontend folder:
```cmd
cd C:\Users\valoo\Documents\social-engineering-analyzer\frontend
```

### Install dependencies (if you haven't already):
```cmd
npm install
```

### Start the frontend:
```cmd
npm run dev
```

**You should see:**
```
✓ Ready in X.Xs
○ Local:        http://localhost:3000
```

---

## Step 3: Open Browser

1. Open your browser (Chrome, Firefox, Edge)
2. Go to: **http://localhost:3000**
3. You should see your Lurantis landing page!

---

## Step 4: Test Wallet Analysis

1. Scroll down to "Wallet Analysis" section
2. Paste a wallet address (e.g., `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`)
3. Click "Analyze Wallet"
4. See the results!

---

## You Should Have 2 Terminals Running:

**Terminal 1 (Backend):**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 (Frontend):**
```
✓ Ready in X.Xs
○ Local:        http://localhost:3000
```

---

## Troubleshooting

**Frontend won't start?**
- Make sure you're in the `frontend` folder
- Run `npm install` first
- Check if port 3000 is already in use

**Can't connect to backend?**
- Make sure backend is running on port 8000
- Check backend terminal for errors

**Site loads but analysis doesn't work?**
- Check browser console (F12) for errors
- Check backend terminal for errors
- Make sure both are running!

---

## That's It! 🎉

Your site should now be running at **http://localhost:3000**

