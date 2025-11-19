# Quick Fix: "Failed to Fetch" Error

## Common Causes

1. **Backend not running**
2. **Backend crashed** (RPC timeout or error)
3. **CORS issue** (though configured)
4. **Request timeout** (fetching too many blocks)
5. **RPC connection failing** (Gnosis Chain RPC down)

## Quick Fixes

### 1. Check if Backend is Running

```bash
# In backend directory
cd backend
python -m uvicorn app_enhanced:app --reload --host 0.0.0.0 --port 8000
```

Check if you see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 2. Test Backend Directly

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test analyze-wallet endpoint
curl -X POST "http://localhost:8000/analyze-wallet" \
  -H "Content-Type: application/json" \
  -d '{"wallet_address": "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"}'
```

### 3. Check Browser Console

Open browser DevTools (F12) → Console tab

Look for:
- CORS errors
- Network errors
- Connection refused errors

### 4. Check Backend Logs

Look for:
- RPC connection errors
- Timeout errors
- Exception stack traces

### 5. Verify Environment Variables

Make sure `.env` file has:
```
GNOSIS_RPC_URL=https://rpc.gnosischain.com
QDRANT_URL=http://localhost:6333
# OR for Qdrant Cloud:
# QDRANT_URL=https://your-cluster.qdrant.io
# QDRANT_API_KEY=your-api-key
```

## Updated Code

The code has been updated to:
- ✅ Use faster block sampling (every 10th block)
- ✅ Limit to 500 blocks max (instead of 5000)
- ✅ Add timeout protection (5 seconds per block)
- ✅ Better error handling and logging
- ✅ Return partial results if some blocks fail

## If Still Failing

### Option 1: Use Public RPC with Better Reliability

Update `.env`:
```
GNOSIS_RPC_URL=https://gnosis.blockpi.network/v1/rpc/public
```

### Option 2: Increase Timeout in Frontend

If the request is just slow, increase timeout in `WalletAnalysis.tsx`:

```typescript
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 60000); // 60 second timeout

const response = await fetch(`${API_URL}/analyze-wallet`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    wallet_address: walletAddress.trim(),
    user_address: address || undefined,
    include_transactions: true
  }),
  signal: controller.signal
});

clearTimeout(timeoutId);
```

### Option 3: Check Qdrant Connection

```bash
# Test Qdrant
curl http://localhost:6333/collections

# Or if using Qdrant Cloud, check your API key
```

## Debug Steps

1. **Check backend is running**: `curl http://localhost:8000/health`
2. **Check browser console**: Look for actual error message
3. **Check backend logs**: Look for exception stack traces
4. **Test endpoint directly**: Use curl or Postman
5. **Check network tab**: See what HTTP status code you're getting

## Most Likely Issue

**Backend not running** or **RPC timeout**.

The updated code now:
- Samples blocks (faster)
- Has timeouts (won't hang)
- Better error handling (returns partial results)

Try again - it should work now!

