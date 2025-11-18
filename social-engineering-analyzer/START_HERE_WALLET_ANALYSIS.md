# 🎯 START HERE: Test Wallet Analysis (Step-by-Step)

## Quick Start (3 Steps)

### Step 1: Start Backend Server

**Open PowerShell or Command Prompt:**

```powershell
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
venv\Scripts\activate
python app_enhanced.py
```

**✅ You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**⏸️ Leave this terminal open!**

---

### Step 2: Start Frontend (New Terminal)

**Open a NEW PowerShell/Command Prompt window:**

```powershell
cd C:\Users\valoo\Documents\social-engineering-analyzer\frontend
npm run dev
```

**✅ You should see:**
```
✓ Ready in 2.5s
○ Local:        http://localhost:3000
```

**⏸️ Leave this terminal open too!**

---

### Step 3: Open Browser & Test

1. **Open your browser** (Chrome, Firefox, Edge)
2. **Go to:** http://localhost:3000
3. **Scroll down** or click **"Wallet Analysis"** in navbar
4. **Enter a wallet address:**
   ```
   0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079
   ```
5. **Click "🔍 Analyze Wallet"**
6. **Wait a few seconds** - see the results!

---

## What You'll See

- ✅ **Risk Score** (0-100)
- ✅ **Risk Level** (LOW/MEDIUM/HIGH/CRITICAL)
- ✅ **Wallet Balance** (xDAI)
- ✅ **Behavioral Cluster** (if detected)
- ✅ **Anomalies** (suspicious patterns)
- ✅ **Key Insights**

---

## Troubleshooting

**Backend won't start?**
- Make sure virtual environment is activated: `venv\Scripts\activate`
- Check Qdrant Cloud is connected (check `.env` file)

**Frontend won't start?**
- Run: `npm install` first
- Then: `npm run dev`

**No results showing?**
- Check browser console (Press F12)
- Check backend terminal for errors
- Make sure both servers are running!

---

## That's It! 🎉

You now have a **high-level on-chain wallet analysis system** running!

**Next:** Try different wallet addresses and see what patterns it detects!

