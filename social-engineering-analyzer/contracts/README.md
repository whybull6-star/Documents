# Smart Contracts

Smart contracts for Lurantis on Gnosis Chain.

## Contracts

### Subscription.sol

Monthly subscription contract that handles payments:
- **Price**: 8.99 xDAI per month (~$8.99 USD)
- **Payment address**: `0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`
- **Duration**: 30 days per subscription
- **Features**:
  - Users pay once, get 30 days of access
  - Payments go directly to owner wallet
  - Auto-extends subscription if already active
  - Tracks subscription end times on-chain

## Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment:**
   Create `.env` file with:
   ```
   PRIVATE_KEY=your_private_key_here
   GNOSIS_RPC=https://rpc.gnosischain.com
   GNOSISSCAN_API_KEY=your_api_key_here (optional, for verification)
   ```

## Deployment

### Deploy Subscription Contract

```bash
npm run deploy:mainnet
```

Or for testnet (Chiado):
```bash
npm run deploy:testnet
```

**After deployment:**
1. Save the contract address
2. Update `frontend/.env` with `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=<address>`
3. Verify contract on explorer (optional but recommended)

## Testing Locally

```bash
# Compile contracts
npm run compile

# Run tests (if you add tests)
npm test
```

## Contract Addresses

After deployment, update these:
- **Frontend**: `NEXT_PUBLIC_SUBSCRIPTION_CONTRACT`
- **Backend**: Add contract address to credit manager

## Owner Wallet

All subscription payments go to:
`0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079`

Make sure this wallet has sufficient balance to pay gas fees if you need to update the contract.

