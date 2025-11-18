# 🔍 Debug Qdrant - Why Patterns Aren't Matching

## Quick Test

**Run this to check if Qdrant is working:**

```cmd
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
venv\Scripts\activate
python test_qdrant_match.py
```

**This will show:**
- If collections exist
- If patterns are seeded
- If searches are working
- What similarity scores you're getting

---

## If Patterns Aren't Seeded

**Run the seed script:**

```cmd
python scripts/seed_enhanced_patterns.py
```

This adds all the patterns to Qdrant.

---

## Check Backend Logs

When you analyze a wallet, check the backend terminal for:

```
DEBUG: Searching Qdrant with signature: 'wallet with zero balance...'
DEBUG: Found X total matches
DEBUG RISK CALC: pattern_matches=X, similar_patterns keys=[...]
```

**If you see "Found 0 total matches"** - patterns aren't seeded or Qdrant isn't connected.

---

## What I Fixed

1. **Exact pattern matching** - Uses EXACT text from seeded patterns
2. **Lower threshold** - 0.1 instead of 0.2
3. **Better risk calculation** - Uses pattern scores properly
4. **Zero balance detection** - Adds risk even if Qdrant doesn't match (fallback)

---

## Test the Zero Wallet Again

After restarting backend, test:
```
0x0000000000000000000000000000000000000001
```

**It should:**
- Match pattern 5001 (zero balance pattern)
- Get similarity score > 0.7 (exact match)
- Show risk score 30-50+

---

## If Still Not Working

1. **Check if patterns are seeded:**
   ```cmd
   python test_qdrant_match.py
   ```

2. **Re-seed if needed:**
   ```cmd
   python scripts/seed_enhanced_patterns.py
   ```

3. **Check Qdrant connection:**
   - Verify `.env` has correct `QDRANT_URL` and `QDRANT_API_KEY`
   - Test connection: `curl http://localhost:6333/health` (if local)

4. **Check backend logs** - look for DEBUG messages

