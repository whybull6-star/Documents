# 🚀 Step-by-Step: Test Wallet Analysis

## What You Just Got

A **high-level on-chain wallet analysis system** that:
- Analyzes wallet behavior using Qdrant vector search
- Detects suspicious patterns and anomalies
- Shows risk scores and behavioral clusters
- Identifies wallet relationships

---

## Step 1: Check Your Backend is Running ✅

**Open a terminal/command prompt** and check if your backend is running:

```bash
# If you see "python app_enhanced.py" running, you're good!
# If not, start it:
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
python app_enhanced.py
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ If it's running, go to Step 2**

**❌ If you get an error**, make sure:
- Your virtual environment is activated (`venv\Scripts\activate`)
- Qdrant Cloud is connected (check your `.env` file has `QDRANT_URL` and `QDRANT_API_KEY`)

---

## Step 2: Start Your Frontend 🎨

**Open a NEW terminal/command prompt** (keep the backend running in the first one):

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer\frontend
npm run dev
```

**You should see:**
```
✓ Ready in 2.5s
○ Local:        http://localhost:3000
```

**✅ If it starts, go to Step 3**

**❌ If you get an error**, try:
```bash
npm install
npm run dev
```

---

## Step 3: Open Your Browser 🌐

1. Open your browser (Chrome, Firefox, Edge - any works)
2. Go to: **http://localhost:3000**
3. You should see your Lurantis landing page

---

## Step 4: Navigate to Wallet Analysis 🔍

**Option A: Click the navbar link**
- Look at the top navigation bar
- Click **"Wallet Analysis"**

**Option B: Scroll down**
- Scroll down past the Hero section
- You'll see the **"On-Chain Wallet Analysis"** section

---

## Step 5: Test with a Wallet Address 💼

**Enter a Gnosis Chain wallet address:**

1. **Find the input box** that says "Wallet Address"
2. **Paste a wallet address**, for example:
   ```
   0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079
   ```
   (This is your subscription wallet address - safe to test!)

3. **Click "🔍 Analyze Wallet"** button

4. **Wait a few seconds** - it's analyzing on-chain data!

---

## Step 6: See the Results 📊

**You should see:**

1. **Risk Assessment Card**
   - Risk score (0-100)
   - Risk level (LOW/MEDIUM/HIGH/CRITICAL)
   - Risk factors (if any)

2. **Wallet Info**
   - Balance in xDAI
   - Behavioral cluster (if detected)

3. **Anomalies** (if any detected)
   - List of suspicious patterns found

4. **Wallet Relationships** (if any)
   - Connections to other wallets

5. **Key Insights**
   - Summary of findings

---

## Step 7: Try Different Wallets 🔄

**Test with different addresses:**

1. **Your own wallet** (if you have MetaMask connected)
   - Click "Connect Wallet" in the navbar
   - Copy your address
   - Paste it in the analysis box

2. **Random Gnosis addresses** from:
   - GnosisScan: https://gnosisscan.io/
   - Look at recent transactions
   - Copy any wallet address

3. **Known scam wallets** (if you know any)
   - See if the system detects them!

---

## What's Happening Behind the Scenes? 🔬

1. **Frontend** sends wallet address to backend API
2. **Backend** connects to Gnosis Chain RPC
3. **Fetches** wallet balance and transaction data
4. **Creates** a behavioral signature vector
5. **Searches** Qdrant for similar wallet patterns
6. **Detects** anomalies using vector similarity
7. **Calculates** risk score based on findings
8. **Returns** comprehensive analysis to frontend

---

## Troubleshooting 🛠️

### Error: "Failed to analyze wallet"
- **Check:** Is backend running? (Step 1)
- **Check:** Is Qdrant Cloud connected?
- **Check:** Browser console for errors (F12)

### Error: "Insufficient credits"
- **Solution:** Connect your wallet and subscribe (or use free tier)
- **Or:** Test without `user_address` (remove subscription check temporarily)

### Error: "Invalid wallet address"
- **Check:** Address starts with `0x`
- **Check:** Address is 42 characters long
- **Check:** It's a Gnosis Chain address (not Ethereum mainnet)

### Nothing happens when clicking "Analyze"
- **Check:** Browser console (F12) for errors
- **Check:** Network tab to see if API call is made
- **Check:** Backend terminal for error messages

---

## Next Steps 🎯

**Once it's working, you can:**

1. **Integrate with GnosisScan API** for real transaction data
2. **Add transaction flow visualization**
3. **Build wallet comparison feature**
4. **Add more attack patterns to Qdrant**
5. **Create alerts for high-risk wallets**

---

## Quick Test Checklist ✅

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Browser open to localhost:3000
- [ ] Can see "Wallet Analysis" section
- [ ] Can enter wallet address
- [ ] Can click "Analyze Wallet"
- [ ] See results appear (even if empty)

---

**Need help?** Check the browser console (F12) and backend terminal for error messages!

