# 🧪 High-Risk Test Wallet

## Test Wallet Address (High Risk)

Use this address to test high-risk detection:

```
0x0000000000000000000000000000000000000000
```

**Wait!** That's the zero address - it's invalid. Let me give you a better one:

## Better Test Address (Suspicious Characteristics)

```
0x0000000000000000000000000000000000000001
```

**Why this triggers high risk:**
- Has 39 zeros (our code flags >15 zeros as suspicious)
- Will match "high_zero_count" indicator
- Will match transaction analysis patterns about suspicious addresses

---

## Even Better: Use This Pattern

For maximum risk detection, use an address with many zeros:

```
0x0000000000000000000000000000000000000002
```

Or create your own with many zeros:
```
0x000000000000000000000000000000000000ABCD
```

---

## What Should Happen

When you analyze these addresses, you should see:

1. **Risk Score:** 15-40+ (from suspicious indicators)
2. **Risk Factors:** 
   - "Suspicious address characteristics: high_zero_count"
   - "Zero balance with suspicious patterns" (if balance is 0)
3. **Pattern Matches:** Should match transaction_analysis patterns
4. **Anomalies:** May detect suspicious patterns

---

## Quick Test Steps

1. Go to Wallet Analysis section
2. Paste: `0x0000000000000000000000000000000000000001`
3. Click "Analyze Wallet"
4. Check results:
   - Risk score should be > 0
   - Should see "high_zero_count" in risk factors
   - Should see pattern matches

---

## If It Still Shows Low Risk

The patterns might not be matching well. In that case, we can:
1. Lower the similarity threshold
2. Add more generic patterns
3. Make the address analysis more sensitive

Let me know what you see!

