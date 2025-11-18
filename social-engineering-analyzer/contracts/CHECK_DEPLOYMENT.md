# Check if Deployment Succeeded

## Step 1: Check Terminal Output

Look at your terminal where you ran `npm run deploy:mainnet`. 

**What to look for:**

✅ **Success looks like:**
```
Compiling 1 file with 0.8.20
Compilation finished successfully

Deploying Subscription contract...
✅ Subscription contract deployed to: 0x1234567890abcdef1234567890abcdef12345678
   Network: gnosis-mainnet
   Owner address: 0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079
   Monthly price: 8.99 xDAI

Waiting for block confirmations...
✅ Contract deployed successfully!
   Explorer: https://gnosisscan.io/address/0x1234567890abcdef1234567890abcdef12345678
```

❌ **If you see errors:**
- "insufficient funds" = Need more xDAI
- "nonce too high" = Try again
- "network error" = Check internet connection

---

## Step 2: Find Your Contract Address

**If deployment succeeded, you should see a line like:**
```
✅ Subscription contract deployed to: 0x...
```

**Copy that address!** (It starts with `0x` and is 42 characters long)

---

## Step 3: Check on Gnosisscan

1. **Go to:** https://gnosisscan.io

2. **Paste your contract address** in the search bar

3. **What you should see:**
   - Contract address page
   - Shows "Contract" (not just "Address")
   - Shows transaction history
   - Shows contract code (if verified)

---

## Step 4: Check Your Wallet Transaction

1. **Open MetaMask**
2. **Go to Activity tab**
3. **Look for the deployment transaction**
   - Should show "Contract Deployment"
   - Click it to see details
   - Copy the contract address from there

---

## Step 5: Check Transaction Hash

If you see a transaction hash in the terminal output:

1. **Copy the transaction hash** (looks like: `0xabc123...`)
2. **Go to:** https://gnosisscan.io
3. **Paste the transaction hash** in search
4. **Click on the transaction**
5. **Scroll down** to see "Contract Created" section
6. **Click the contract address** there

---

## Common Issues

### "I don't see any output"
- **Problem:** Deployment might have failed silently
- **Solution:** Check for error messages, try running again

### "I see the address but explorer shows nothing"
- **Problem:** Transaction might still be pending
- **Solution:** Wait 1-2 minutes, refresh the page

### "Explorer shows 'Address' not 'Contract'"
- **Problem:** Contract deployed but not verified
- **Solution:** This is fine! Contract still works, just not verified

### "I lost the contract address"
- **Solution:** Check MetaMask Activity → Find deployment transaction → Copy contract address

---

## Quick Check Commands

**If you want to verify the contract exists, you can check your wallet:**

1. **Go to:** https://gnosisscan.io
2. **Search your wallet address:** `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`
3. **Look at "Transactions" tab**
4. **Find the most recent "Contract Creation" transaction**
5. **Click it** → See contract address

---

## Still Can't Find It?

**Run deployment again and watch carefully:**

```bash
npm run deploy:mainnet
```

**This time:**
- Watch for any error messages
- Copy the contract address immediately when it appears
- Check if transaction hash is shown
- Note the explorer URL that's printed

**If it fails, share the error message!**

