# ⚡ Quick Test - High Risk Wallet

## Test This Real Wallet Address

```
0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079
```

**This is your subscription wallet** - should show LOW risk (normal wallet)

**To find suspicious wallets:**
- Go to https://gnosisscan.io/
- Look at recent transactions
- Copy wallet addresses to test

---

## What You Should See

### For Normal Wallet (like your subscription wallet):
✅ **Risk Score:** 0-10 (LOW)  
✅ **Risk Level:** LOW  
✅ **Risk Factors:** 
   - "No suspicious patterns detected - wallet appears normal"

### For Suspicious Wallet (if you find one):
✅ **Risk Score:** 20-60+  
✅ **Risk Level:** MEDIUM or HIGH  
✅ **Risk Factors:** 
   - Pattern matches from Qdrant
   - Specific threat patterns detected

✅ **Pattern Matches:** Should show matches from Qdrant if suspicious  
✅ **Charts:** Should display risk score and pattern similarity

---

## Test Steps

1. **Start backend** (if not running):
   ```powershell
   cd backend
   venv\Scripts\activate
   python app_enhanced.py
   ```

2. **Start frontend** (if not running):
   ```powershell
   cd frontend
   npm run dev
   ```

3. **Open browser:** http://localhost:3000

4. **Go to Wallet Analysis section**

5. **Paste address:** `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079` (your subscription wallet)

6. **Click "Analyze Wallet"**

7. **Check results!**

---

## If It Shows Low Risk

I've lowered the similarity thresholds in the code, so it should match more patterns now. If it still shows low risk:

1. **Check backend terminal** - any errors?
2. **Check browser console** (F12) - any errors?
3. **Verify Qdrant is connected** - check `/health` endpoint
4. **Re-seed patterns** - run `python scripts/seed_enhanced_patterns.py`

---

## Expected Output

### Normal Wallet:
```
Risk Score: 0-10
Risk Level: LOW
Risk Factors:
  • No suspicious patterns detected - wallet appears normal
```

### Suspicious Wallet (if found):
```
Risk Score: 25-60+
Risk Level: MEDIUM/HIGH
Risk Factors:
  • Pattern match detected (X patterns)
  • [MEDIUM] Pattern match (transaction_analysis): ...
```

**Try it now!** 🚀

