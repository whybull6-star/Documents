# Smart Contract Deployment Guide (ELI5)

## What Does "Deploy On-Chain" Mean?

**ELI5 Explanation:**
Think of it like this:
- **Your contract code** = A recipe (written in Solidity)
- **Deploying** = Actually cooking the recipe and putting it in a restaurant (the blockchain)
- **Once deployed** = Anyone can use your contract at that address (the restaurant location)

When you "deploy" a smart contract, you're:
1. Uploading your code to the blockchain
2. Getting a unique address (like `0x123...abc`)
3. Making it live and usable forever (well, until the blockchain ends)

---

## What You Need Before Deploying

### 1. A Wallet (MetaMask is fine)
- Already have this if you've connected to the site!

### 2. Some xDAI (for gas fees)
- **Testnet (Chiado)**: Free test tokens (for testing)
- **Mainnet (Gnosis)**: Real xDAI (costs real money, like $0.01-$0.10)

### 3. Your Wallet's Private Key
- **⚠️ NEVER SHARE THIS!**
- Export it from MetaMask (Settings → Security → Export Private Key)
- Keep it secret!

### 4. Node.js installed
- You probably have this already if the frontend runs

---

## Step-by-Step Deployment

### Step 1: Get Testnet xDAI (Recommended for First Time)

**Why testnet first?**
- It's free
- You can make mistakes without losing real money
- Perfect for learning

**How to get Chiado testnet xDAI:**

1. **Add Chiado Testnet to MetaMask:**
   - Go to [Chainlist.org](https://chainlist.org)
   - Search "Chiado"
   - Click "Connect Wallet"
   - Click "Add to MetaMask"

2. **Get free testnet tokens:**
   - Go to [Chiado Faucet](https://faucet.chiadochain.net/) or [Gnosis Faucet](https://faucet.gnosischain.com/)
   - Connect your wallet
   - Request testnet xDAI (it's free!)

3. **Switch to Chiado network in MetaMask**

### Step 2: Set Up Your Deployment Environment

1. **Navigate to contracts folder:**
   ```bash
   cd social-engineering-analyzer/contracts
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create `.env` file:**
   ```bash
   # Create the file (you can use any text editor)
   touch .env
   ```
   
   Or create it manually: `contracts/.env`

4. **Add your private key to `.env`:**
   ```
   PRIVATE_KEY=your_private_key_here_without_0x_prefix
   GNOSIS_TESTNET_RPC=https://rpc.chiadochain.net
   GNOSIS_RPC=https://rpc.gnosischain.com
   ```

   **⚠️ Important:**
   - Export your private key from MetaMask
   - Remove the `0x` prefix if it has one
   - **NEVER commit this file to GitHub!** (It's already in .gitignore)

### Step 3: Deploy to Testnet (Chiado)

1. **Make sure you have testnet xDAI:**
   - Check MetaMask balance on Chiado network
   - Should have at least 0.01 xDAI (request from faucet if needed)

2. **Deploy:**
   ```bash
   npm run deploy:testnet
   ```

3. **What happens:**
   - Hardhat compiles your contract
   - Sends it to Chiado testnet
   - Shows you the contract address
   - Wait for 5 confirmations

4. **Copy the contract address:**
   - It will look like: `0x1234567890abcdef1234567890abcdef12345678`
   - Save this somewhere!

### Step 4: Test It Works

1. **Go to Chiado Block Explorer:**
   - [Blockscout Chiado](https://blockscout.chiadochain.net/)

2. **Paste your contract address**
   - You should see your contract!

3. **Test on your website:**
   - Update `frontend/.env.local`:
     ```
     NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0xYOUR_CONTRACT_ADDRESS
     ```
   - Restart frontend: `npm run dev`
   - Try subscribing!

### Step 5: Deploy to Mainnet (Gnosis - Real Network)

**⚠️ Only do this when you're ready! This costs real money.**

1. **Make sure you have real xDAI on Gnosis:**
   - Buy xDAI on an exchange
   - Bridge it to Gnosis Chain
   - Need ~0.1 xDAI for gas

2. **Update your wallet to use Gnosis Mainnet:**
   - Switch MetaMask to Gnosis Chain (network 100)

3. **Deploy:**
   ```bash
   npm run deploy:mainnet
   ```

4. **Get the contract address** (same as testnet)

5. **Update frontend `.env.local`** with the mainnet address

6. **Verify on Gnosisscan:**
   - Go to [gnosisscan.io](https://gnosisscan.io)
   - Find your contract
   - (Optional) Verify the source code

---

## Troubleshooting

### "Insufficient funds for gas"
- **Solution:** Get more xDAI from faucet (testnet) or buy more (mainnet)

### "Private key is invalid"
- **Solution:** Make sure you copied it correctly, removed `0x` if it had one

### "Contract deployment failed"
- **Solution:** Check console for error, make sure network is correct

### "Cannot find module 'hardhat'"
- **Solution:** Run `npm install` in contracts folder

### Contract shows "0x0..." or blank
- **Solution:** Wait a bit longer, blockchain can be slow

---

## What Happens After Deployment?

1. **Your contract is live** at that address
2. **Users can interact with it** through your website
3. **Payments go to:** `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079` (your wallet)
4. **It's permanent** - can't be changed (unless you build upgrade functionality)

---

## Quick Reference

### Testnet (Chiado)
- **Network ID:** 10200
- **RPC:** https://rpc.chiadochain.net
- **Explorer:** https://blockscout.chiadochain.net
- **Faucet:** https://faucet.chiadochain.net

### Mainnet (Gnosis)
- **Network ID:** 100
- **RPC:** https://rpc.gnosischain.com
- **Explorer:** https://gnosisscan.io
- **Cost:** Real xDAI (~$0.01-0.10 for deployment)

---

## Next Steps

1. ✅ Deploy to testnet
2. ✅ Test it works
3. ✅ Update frontend with testnet address
4. ✅ Test subscription flow
5. ✅ When ready, deploy to mainnet
6. ✅ Update frontend with mainnet address
7. ✅ Launch! 🚀

---

## Need Help?

- **Hardhat Docs:** https://hardhat.org/docs
- **Gnosis Docs:** https://docs.gnosischain.com
- **OpenZeppelin (Smart Contract Security):** https://docs.openzeppelin.com

