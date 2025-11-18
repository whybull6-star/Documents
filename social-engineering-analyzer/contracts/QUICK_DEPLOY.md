# Quick Deploy Checklist

## ⚡ Fast Track Deployment (5 Minutes)

### Prerequisites
- [ ] MetaMask installed
- [ ] Node.js installed
- [ ] Have a wallet with some xDAI (even 0.01 is enough for testnet)

---

## Step 1: Get Testnet Tokens (2 minutes)

1. **Add Chiado Testnet to MetaMask:**
   - Go to https://chainlist.org
   - Search "Chiado"
   - Click "Connect Wallet" → "Add to MetaMask"
   - Switch to Chiado network in MetaMask

2. **Get free test tokens:**
   - Go to https://faucet.chiadochain.net or https://faucet.gnosischain.com
   - Connect wallet
   - Request testnet xDAI (it's free!)
   - Wait 1-2 minutes, check balance

---

## Step 2: Setup Deployment (1 minute)

1. **Open terminal in contracts folder:**
   ```bash
   cd social-engineering-analyzer/contracts
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create `.env` file:**
   - Create file: `contracts/.env`
   - Add this (replace YOUR_PRIVATE_KEY):
   ```
   PRIVATE_KEY=YOUR_PRIVATE_KEY_HERE
   GNOSIS_TESTNET_RPC=https://rpc.chiadochain.net
   GNOSIS_RPC=https://rpc.gnosischain.com
   ```

4. **Get your private key from MetaMask:**
   - MetaMask → Settings → Security & Privacy → Export Private Key
   - ⚠️ Enter password, copy the key
   - ⚠️ Remove `0x` prefix if it has one
   - Paste it in `.env` file

---

## Step 3: Deploy! (2 minutes)

```bash
npm run deploy:testnet
```

**What you'll see:**
```
Compiling...
Deploying Subscription contract...
✅ Subscription contract deployed to: 0x1234...abcd
   Network: gnosis-testnet
   Owner address: 0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079
   Monthly price: 8.99 xDAI
```

**Copy that contract address!** (It starts with `0x...`)

---

## Step 4: Connect to Frontend (1 minute)

1. **Create/update `frontend/.env.local`:**
   ```
   NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0xYOUR_CONTRACT_ADDRESS_HERE
   ```

2. **Restart frontend:**
   - Stop server (Ctrl+C)
   - Start again: `npm run dev` (in frontend folder)

3. **Test it:**
   - Refresh browser
   - Connect wallet
   - Click "Subscribe Now"
   - Should work! 🎉

---

## Troubleshooting

### "Insufficient funds"
→ Get more testnet xDAI from faucet

### "Invalid private key"
→ Make sure no `0x` prefix, no extra spaces

### "Cannot find module"
→ Run `npm install` in contracts folder

### "Contract not configured" error on site
→ Check `frontend/.env.local` has the right address
→ Restart frontend server

---

## Next: Deploy to Mainnet (Real Network)

When you're ready:
1. Buy real xDAI
2. Switch MetaMask to Gnosis Chain (network 100)
3. Run: `npm run deploy:mainnet`
4. Update frontend with mainnet address

That's it! 🚀

