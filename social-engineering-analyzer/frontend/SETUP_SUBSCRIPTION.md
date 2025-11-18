# Setting Up Subscriptions

## Quick Fix

You need to deploy the subscription contract first, then add its address to your environment variables.

## Step 1: Deploy the Contract

1. **Go to contracts folder:**
   ```bash
   cd ../contracts
   ```

2. **Install dependencies (if not done):**
   ```bash
   npm install
   ```

3. **Create `.env` file in contracts folder:**
   ```
   PRIVATE_KEY=your_wallet_private_key_here
   GNOSIS_RPC=https://rpc.gnosischain.com
   ```

4. **Deploy to Gnosis Mainnet:**
   ```bash
   npm run deploy:mainnet
   ```

   Or deploy to testnet first:
   ```bash
   npm run deploy:testnet
   ```

5. **Copy the contract address** from the deployment output (looks like: `0x...`)

## Step 2: Add Contract Address to Frontend

1. **Go back to frontend folder:**
   ```bash
   cd ../frontend
   ```

2. **Create `.env.local` file** (if it doesn't exist):
   ```
   NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=0xYOUR_CONTRACT_ADDRESS_HERE
   ```

3. **Replace `0xYOUR_CONTRACT_ADDRESS_HERE`** with the actual address from Step 1

4. **Restart the Next.js server:**
   - Stop it (Ctrl+C)
   - Start again: `npm run dev`

## Step 3: Test

1. Refresh your browser
2. Connect your wallet
3. Click "Subscribe Now"
4. It should now work!

## Troubleshooting

### "Contract not configured" error
- Make sure you created `.env.local` (not just `.env`)
- Make sure the variable name is exactly: `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`
- Restart the dev server after adding the variable

### Contract deployment fails
- Make sure your wallet has xDAI for gas fees
- Check your PRIVATE_KEY is correct
- Try testnet first to test

### Still not working?
- Check browser console (F12) for error messages
- Verify the contract address is correct (check on https://gnosisscan.io)

