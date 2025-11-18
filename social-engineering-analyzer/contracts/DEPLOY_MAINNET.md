# Deploy to Gnosis Mainnet - Step by Step

## Prerequisites Check ✅

Before starting, make sure you have:
- [ ] MetaMask installed and set up
- [ ] Some xDAI on Gnosis Chain (need ~0.1 xDAI for gas fees)
- [ ] Your wallet address: `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079` (for receiving payments)

---

## Step 1: Get xDAI on Gnosis Chain

If you don't have xDAI yet:

**Option A: Buy and Bridge**
1. Buy xDAI on an exchange (like Binance, Kraken, etc.)
2. Use a bridge like https://omni.xdaichain.com/ or https://bridge.gnosischain.com/
3. Bridge it to Gnosis Chain

**Option B: Swap ETH for xDAI**
1. If you have ETH, use a DEX like https://app.honeyswap.org/
2. Swap ETH → xDAI on Gnosis Chain

**You need at least 0.1 xDAI for deployment gas fees.**

---

## Step 2: Get Your Private Key from MetaMask

1. **Open MetaMask** (click the extension icon)
2. Click the **three dots (⋮)** at the top right
3. Click **Account details**
4. Click **Export Private Key**
5. **Enter your password**
6. **Copy the private key** (it looks like: `abc123def456...`)
7. **⚠️ Important:** Remove the `0x` at the start if it has one
   - If it shows: `0xabc123...`
   - Copy only: `abc123...` (without the `0x`)

**⚠️ NEVER share this key with anyone! Keep it secret!**

---

## Step 3: Navigate to Contracts Folder

**Where to open terminal:**
- **Windows:** Right-click in the folder → "Open in Terminal" or use PowerShell
- **Mac/Linux:** Right-click in the folder → "Open in Terminal"

**OR use Cursor/VS Code:**
- In Cursor, click "Terminal" at the top menu
- Or press `Ctrl + ` (backtick) or `Ctrl + J`

**Navigate to contracts folder:**

1. **Check where you are:**
   ```bash
   pwd
   ```
   (Windows PowerShell: `Get-Location`)

2. **You should be in:** `C:\Users\valoo\Documents\social-engineering-analyzer` (or similar)

3. **Go into contracts folder:**
   ```bash
   cd contracts
   ```

4. **Verify you're in the right place:**
   ```bash
   dir
   ```
   (Mac/Linux: `ls`)
   
   You should see files like:
   - `package.json`
   - `hardhat.config.js`
   - `contracts/` folder
   - `scripts/` folder

---

## Step 4: Install Dependencies

**In the terminal (still in `contracts` folder), run:**

```bash
npm install
```

**What this does:** Downloads all the code libraries needed (Hardhat, OpenZeppelin, etc.)

**Wait for it to finish** (takes 1-2 minutes). You'll see:
```
added 500 packages, and audited 501 packages in 45s
```

---

## Step 5: Create .env File

**In the same terminal/contracts folder:**

**Option A: Using Command Line**

**Windows PowerShell:**
```powershell
New-Item -ItemType File -Name ".env"
```

**Mac/Linux:**
```bash
touch .env
```

**Option B: Using File Explorer/Finder**
1. Open `contracts` folder in File Explorer
2. Right-click → New → Text Document
3. Name it exactly: `.env` (with the dot at the start!)
4. If Windows warns you about the name, click "Yes"

---

## Step 6: Add Your Private Key to .env

**Open the `.env` file** (double-click it in File Explorer or use any text editor)

**Paste this** (replace `YOUR_PRIVATE_KEY_HERE` with your actual key from Step 2):

```
PRIVATE_KEY=YOUR_PRIVATE_KEY_HERE
GNOSIS_RPC=https://rpc.gnosischain.com
GNOSIS_TESTNET_RPC=https://rpc.chiadochain.net
```

**Example:**
```
PRIVATE_KEY=abc123def4567890123456789012345678901234567890123456789012345678
GNOSIS_RPC=https://rpc.gnosischain.com
GNOSIS_TESTNET_RPC=https://rpc.chiadochain.net
```

**⚠️ Important:**
- No spaces around the `=` sign
- No quotes needed
- Remove `0x` if your key had it
- Save the file (Ctrl+S)

---

## Step 7: Switch MetaMask to Gnosis Chain

1. **Open MetaMask**
2. Click the network dropdown (top of MetaMask, shows "Ethereum Mainnet" or similar)
3. If you see "Gnosis Chain" - click it
4. If you DON'T see it:
   - Scroll down → "Add Network"
   - Or go to: https://chainlist.org
   - Search "Gnosis Chain"
   - Click "Connect Wallet"
   - Click "Add to MetaMask"

5. **Verify you're on Gnosis Chain:**
   - Network should show "Gnosis Chain"
   - Network ID: 100
   - You should see your xDAI balance

---

## Step 8: Deploy to Mainnet!

**Back in terminal (still in `contracts` folder), run:**

```bash
npm run deploy:mainnet
```

**What happens:**
1. It compiles your contract (10-20 seconds)
2. Sends transaction to Gnosis Chain (30-60 seconds)
3. Shows you the contract address

**You'll see output like:**
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

⚠️  Remember to:
   1. Save the contract address: 0x1234567890abcdef1234567890abcdef12345678
   2. Update frontend .env with NEXT_PUBLIC_SUBSCRIPTION_CONTRACT= 0x1234567890abcdef1234567890abcdef12345678
   3. Verify contract on explorer
```

**📋 COPY THAT CONTRACT ADDRESS!** (The one starting with `0x...`)

---

## Step 9: Add Contract Address to Frontend

1. **Navigate to frontend folder:**
   
   **In terminal, go back up one folder:**
   ```bash
   cd ..
   cd frontend
   ```

   **Or open a new terminal** and navigate there:
   ```bash
   cd C:\Users\valoo\Documents\social-engineering-analyzer\frontend
   ```

2. **Create `.env.local` file:**

   **Windows PowerShell:**
   ```powershell
   New-Item -ItemType File -Name ".env.local"
   ```

   **Mac/Linux:**
   ```bash
   touch .env.local
   ```

   **Or manually:** Create a new text file named `.env.local` in the `frontend` folder

3. **Open `.env.local`** and add:
   ```
   NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0xYOUR_CONTRACT_ADDRESS_HERE
   ```
   
   Replace `0xYOUR_CONTRACT_ADDRESS_HERE` with the address from Step 8

   **Example:**
   ```
   NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0x1234567890abcdef1234567890abcdef12345678
   ```

4. **Save the file**

---

## Step 10: Restart Frontend Server

**If your frontend server is running:**
1. Go to the terminal where `npm run dev` is running
2. Press `Ctrl + C` to stop it
3. Start it again:
   ```bash
   npm run dev
   ```

**If not running:**
```bash
npm run dev
```

**⚠️ Important:** You MUST restart the server after adding environment variables!

---

## Step 11: Test It!

1. **Open your browser:** http://localhost:3000
2. **Connect your wallet** (MetaMask)
3. **Make sure you're on Gnosis Chain** in MetaMask
4. **Scroll to Pricing section**
5. **Click "Subscribe Now"**
6. **Approve in MetaMask** (it will ask you to pay 8.99 xDAI)
7. **Wait for transaction** to confirm
8. **Success!** ✅

---

## Troubleshooting

### "Insufficient funds for gas"
- **Problem:** Not enough xDAI
- **Solution:** Get more xDAI on Gnosis Chain (need at least 0.1 for deployment)

### "Cannot find module 'hardhat'"
- **Problem:** Dependencies not installed
- **Solution:** Run `npm install` in contracts folder (Step 4)

### "Private key is invalid"
- **Problem:** Wrong format
- **Solution:** Make sure no `0x` prefix, no quotes, no spaces

### "Contract not configured" on website
- **Problem:** Environment variable not loaded
- **Solution:** 
  - Check `.env.local` has correct address
  - **RESTART the frontend server** (Ctrl+C, then `npm run dev` again)

### "MetaMask not connected"
- **Problem:** Wrong network
- **Solution:** Switch MetaMask to Gnosis Chain (network 100)

---

## Summary

1. ✅ Get xDAI on Gnosis Chain
2. ✅ Export private key from MetaMask
3. ✅ `cd contracts` (in terminal)
4. ✅ `npm install`
5. ✅ Create `.env` file with private key
6. ✅ Switch MetaMask to Gnosis Chain
7. ✅ `npm run deploy:mainnet`
8. ✅ Copy contract address
9. ✅ Add to `frontend/.env.local`
10. ✅ Restart frontend server (`npm run dev`)
11. ✅ Test it works!

**Questions? Check the error messages in terminal - they usually tell you what's wrong!**

