# Next Steps After Deployment ✅

## Step 1: Copy Your Contract Address

**In your terminal, you should see something like:**
```
✅ Subscription contract deployed to: 0x1234567890abcdef1234567890abcdef12345678
```

**📋 COPY THAT ADDRESS!** (The one starting with `0x...`)

**If you lost it:**
- Check your terminal output (scroll up)
- Or go to https://gnosisscan.io
- Search your wallet: `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`
- Look at "Transactions" → Find "Contract Creation" → Click it → See contract address

---

## Step 2: Add Contract Address to Frontend

### 2a. Navigate to Frontend Folder

**In terminal, run:**
```bash
cd ..\frontend
```

**Or open a new terminal and:**
```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer\frontend
```

### 2b. Create `.env.local` File

**Option A: Using Command Line**
```powershell
New-Item -ItemType File -Name ".env.local"
```

**Option B: Manually**
1. Open File Explorer
2. Go to: `C:\Users\valoo\Documents\social-engineering-analyzer\frontend`
3. Right-click → New → Text Document
4. Name it: `.env.local` (with the dot!)
5. If Windows warns about the name, click "Yes"

### 2c. Add Contract Address

**Open `.env.local`** and paste this (replace with YOUR contract address):

```
NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0xYOUR_CONTRACT_ADDRESS_HERE
```

**Example:**
```
NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0x1234567890abcdef1234567890abcdef12345678
```

**⚠️ Important:**
- No spaces around `=`
- No quotes
- Must be the exact address from Step 1

**Save the file** (Ctrl+S)

---

## Step 3: Restart Frontend Server

**If your frontend is running:**
1. Go to the terminal where `npm run dev` is running
2. Press **Ctrl + C** to stop it
3. Start it again:
   ```bash
   npm run dev
   ```

**If not running:**
```bash
npm run dev
```

**⚠️ CRITICAL:** You MUST restart the server after adding environment variables!

---

## Step 4: Test It Works! 🎉

1. **Open browser:** http://localhost:3000

2. **Connect your wallet:**
   - Click "Connect Wallet" in navbar
   - Approve in MetaMask
   - Make sure you're on **Gnosis Chain** (network 100)

3. **Scroll to Pricing section**

4. **Click "Subscribe Now"** on the Pro plan

5. **Approve transaction in MetaMask:**
   - It will ask you to pay 8.99 xDAI
   - Click "Confirm"
   - Wait for transaction to confirm (~30 seconds)

6. **Success!** ✅
   - You should see "Active (30 days left)" or similar
   - The error message should disappear
   - Your subscription is now active!

---

## Step 5: Verify on Blockchain

**Check your contract on explorer:**
1. Go to: https://gnosisscan.io
2. Paste your contract address
3. You should see:
   - Contract code
   - Recent transactions
   - Your subscription transaction

**Check your wallet received payment:**
1. Go to: https://gnosisscan.io
2. Search: `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`
3. Check "Transactions" tab
4. You should see the 8.99 xDAI payment!

---

## Troubleshooting

### "Contract not configured" error still shows
- ✅ Check `.env.local` has correct address
- ✅ **RESTART frontend server** (Ctrl+C, then `npm run dev`)
- ✅ Check no typos in address

### "MetaMask not connected"
- ✅ Make sure MetaMask is on Gnosis Chain (network 100)
- ✅ Refresh the page
- ✅ Try disconnecting and reconnecting

### Transaction fails
- ✅ Make sure you have enough xDAI (need 8.99 + gas fees)
- ✅ Check you're on Gnosis Chain
- ✅ Try again (sometimes network is busy)

### Can't find contract address
- ✅ Check terminal output (scroll up)
- ✅ Check MetaMask Activity → Find deployment transaction
- ✅ Check gnosisscan.io → Search your wallet → Find "Contract Creation"

---

## Summary Checklist

- [ ] Copied contract address from terminal
- [ ] Created `frontend/.env.local` file
- [ ] Added `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0x...` to `.env.local`
- [ ] Restarted frontend server (`npm run dev`)
- [ ] Opened http://localhost:3000
- [ ] Connected wallet (on Gnosis Chain)
- [ ] Clicked "Subscribe Now"
- [ ] Approved transaction in MetaMask
- [ ] ✅ Subscription active!

---

## What's Next?

Once subscriptions work:
1. **Test with different wallets** (if you have multiple)
2. **Check payments are going to your wallet** (`0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`)
3. **Build the rest of your app** (backend, Qdrant setup, etc.)
4. **Deploy frontend** to a real domain when ready

**You're almost there! 🚀**

