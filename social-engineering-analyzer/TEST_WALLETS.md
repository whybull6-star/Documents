# 🧪 Test Wallets for Wallet Analysis

## Known Suspicious/Scam Wallets (For Testing)

### ⚠️ IMPORTANT: These are for testing only!
These addresses are known to be associated with scams, hacks, or suspicious activity. Use them to test your detection system.

---

## Gnosis Chain Test Wallets

### 1. High-Risk Wallet Pattern
```
0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
```
**Why suspicious:** Common pattern for address spoofing attempts

### 2. Test with Your Own Wallet
```
[Your MetaMask wallet address]
```
**Why test:** See how your own wallet is analyzed

### 3. Finding Real Suspicious Wallets

**To find actual Gnosis Chain hack/exploit addresses:**

1. **GnosisScan Block Explorer:**
   - Go to: https://gnosisscan.io/
   - Check "Internal Transactions" tab
   - Look for addresses with unusual activity
   - Check "Token Transfers" for suspicious patterns

2. **Security Reports:**
   - Check Rekt.news for Gnosis Chain exploits
   - Look at DeFi security databases
   - Check Twitter/X for reported scams

3. **Example Search Pattern:**
   - Look for addresses that received large amounts suddenly
   - Check addresses with many small outgoing transactions (dusting)
   - Find addresses that interact with known scam contracts

**Format:** Must be valid 42-character addresses starting with `0x`

**Note:** Always verify addresses are on Gnosis Chain (not Ethereum mainnet) before testing.

---

## How to Test

1. **Paste wallet address** in the analysis tool
2. **Click "Analyze Wallet"**
3. **Check results:**
   - Risk score
   - Behavioral cluster
   - Anomalies detected
   - Patterns matched

---

## What to Look For

### ✅ Good Detection:
- Risk score > 40 for suspicious wallets
- Anomalies detected
- Behavioral patterns identified
- Similar wallet patterns found

### ❌ Needs Improvement:
- All wallets show 0 risk
- No anomalies detected
- No patterns matched
- Generic results for all wallets

---

## Finding More Test Wallets

### GnosisScan (Block Explorer)
1. Go to: https://gnosisscan.io/
2. Look at recent transactions
3. Check flagged addresses
4. Copy wallet addresses to test

### Known Scam Databases
- Check Twitter/X for reported scams
- Look at @zachxbt's investigations
- Check DeFi security reports

---

## Expected Results

**For a normal wallet:**
- Risk: LOW (0-30)
- Anomalies: None or few
- Cluster: Normal activity

**For a suspicious wallet:**
- Risk: MEDIUM-HIGH (40-80+)
- Anomalies: Multiple detected
- Cluster: Suspicious pattern
- Patterns: Matches known attack vectors

