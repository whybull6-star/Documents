# 🔍 Proof: All Qdrant Usage for Risk Assessment

## Summary
This document shows **every single place** where Qdrant is used to assess risk factors in the codebase.

---

## 1. Transaction Pattern Analysis
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_analyze_transaction_patterns()`  
**Lines:** 125-131

### Code:
```python
# Search for similar patterns in Qdrant
similar_patterns = await self.qdrant.search_attack_patterns(
    signature,
    attack_types=["transaction_analysis", "wallet_stalking", "address_spoofing", "general_phishing"],
    limit=10,
    score_threshold=0.1
)
```

### What It Does:
- Creates behavioral signature from wallet characteristics
- Searches Qdrant `transaction_analysis` collection
- Returns pattern matches with similarity scores
- Used in risk calculation

### Risk Impact:
- Pattern matches contribute to risk score
- Higher similarity = higher risk
- Multiple matches = higher risk

---

## 2. Behavioral Cluster Detection
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_find_behavioral_cluster()`  
**Lines:** 160-170

### Code:
```python
results = await self.qdrant.search_attack_patterns(
    cluster_text,
    attack_types=["transaction_analysis"],
    limit=3,
    score_threshold=0.3
)
```

### What It Does:
- Searches Qdrant for similar wallet behaviors
- Groups wallets into behavioral clusters
- Returns cluster similarity score

### Risk Impact:
- If similarity > 0.3, adds to risk score
- Higher similarity = higher risk contribution

---

## 3. Anomaly Detection
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_detect_anomalies()`  
**Lines:** 224-229

### Code:
```python
results = await self.qdrant.search_attack_patterns(
    anomaly_text,
    attack_types=["transaction_analysis"],
    limit=5,
    score_threshold=0.3
)
```

### What It Does:
- Searches Qdrant for unusual activity patterns
- Detects anomalies in wallet behavior
- Returns anomalies with severity levels

### Risk Impact:
- Each anomaly adds to risk score based on severity:
  - Critical: +40 points
  - High: +30 points
  - Medium: +20 points

---

## 4. Risk Score Calculation (Primary)
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_calculate_risk()`  
**Lines:** 257-301

### Code:
```python
# PRIMARY: Pattern matches from Qdrant - THIS IS WHAT MATTERS
pattern_matches = tx_patterns.get("pattern_matches_count", 0)
similar_patterns = tx_patterns.get("similar_patterns", {})

for attack_type, patterns in similar_patterns.items():
    if patterns:
        for pattern in patterns:
            score = pattern.get("score", 0.0)  # Qdrant similarity score
            
            if score > 0.7:  # Very high similarity
                risk_score += score * 60
            elif score > 0.5:  # High similarity
                risk_score += score * 45
            elif score > 0.3:  # Moderate similarity
                risk_score += score * 30
            elif score > 0.1:  # Low but detected
                risk_score += score * 15
```

### What It Does:
- Takes Qdrant pattern matches from `_analyze_transaction_patterns()`
- Uses similarity scores (0-1) from Qdrant vector search
- Calculates risk based on:
  - Pattern similarity score
  - Number of matches
  - Severity from matched patterns

### Risk Impact:
- **Primary risk calculation method**
- Qdrant similarity scores directly determine risk
- Higher similarity = exponentially higher risk

---

## 5. Enhanced Analyzer (Text Analysis)
**File:** `backend/services/enhanced_analyzer.py`  
**Method:** `analyze_comprehensive()`  
**Uses:** `qdrant.search_attack_patterns()`

### What It Does:
- Analyzes text content (messages, communications)
- Searches Qdrant for similar attack patterns
- Detects SIM swapping, wallet stalking, address spoofing

### Risk Impact:
- Used for text-based threat detection
- Not used in wallet analysis (different use case)

---

## 6. Qdrant Service Implementation
**File:** `backend/services/enhanced_qdrant_service.py`  
**Method:** `search_attack_patterns()`  
**Lines:** 111-166

### Code:
```python
async def search_attack_patterns(
    self,
    query_text: str,
    attack_types: Optional[List[str]] = None,
    limit: int = 5,
    score_threshold: float = 0.5
) -> Dict[str, List[Dict]]:
    query_vector = self.encode_text(query_text)  # Convert to vector
    
    for collection_name in collections_to_search:
        search_results = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,  # Qdrant vector search
            limit=limit,
            score_threshold=score_threshold
        )
```

### What It Does:
- Converts text to 768-dimensional vector using Sentence Transformers
- Searches Qdrant collections using cosine similarity
- Returns patterns with similarity scores

### Risk Impact:
- **Core Qdrant functionality**
- All risk assessments depend on this
- Vector similarity determines pattern matches

---

## 7. Vector Encoding
**File:** `backend/services/enhanced_qdrant_service.py`  
**Method:** `encode_text()`  
**Lines:** 73-75

### Code:
```python
def encode_text(self, text: str) -> List[float]:
    vector = self.model.encode(text, normalize_embeddings=True).tolist()
    return vector
```

### What It Does:
- Uses `all-mpnet-base-v2` model (768 dimensions)
- Converts text to numerical vector
- Required for Qdrant similarity search

### Risk Impact:
- **Foundation of all Qdrant searches**
- Without this, no pattern matching works

---

## Summary: Qdrant Usage Flow

```
1. Wallet Analysis Request
   ↓
2. Create Behavioral Signature (onchain_analyzer.py:105-121)
   ↓
3. Search Qdrant for Patterns (onchain_analyzer.py:125-131)
   - Uses: enhanced_qdrant_service.search_attack_patterns()
   - Searches: transaction_analysis collection
   - Returns: Pattern matches with similarity scores
   ↓
4. Detect Behavioral Cluster (onchain_analyzer.py:160-170)
   - Uses: enhanced_qdrant_service.search_attack_patterns()
   - Returns: Cluster similarity
   ↓
5. Detect Anomalies (onchain_analyzer.py:224-229)
   - Uses: enhanced_qdrant_service.search_attack_patterns()
   - Returns: Anomalies with severity
   ↓
6. Calculate Risk Score (onchain_analyzer.py:257-301)
   - Uses: Pattern matches from step 3
   - Uses: Similarity scores from Qdrant
   - Calculates: Risk based on Qdrant results
   ↓
7. Return Risk Assessment
```

---

## Files Involved

1. **`backend/services/onchain_analyzer.py`**
   - `_analyze_transaction_patterns()` - Line 125
   - `_find_behavioral_cluster()` - Line 160
   - `_detect_anomalies()` - Line 224
   - `_calculate_risk()` - Line 257 (uses Qdrant results)

2. **`backend/services/enhanced_qdrant_service.py`**
   - `encode_text()` - Line 73
   - `search_attack_patterns()` - Line 111
   - `add_attack_pattern()` - Stores patterns in Qdrant

3. **`backend/services/enhanced_analyzer.py`**
   - Uses Qdrant for text analysis (different use case)

---

## Proof: Qdrant is Used for Risk Assessment

✅ **Pattern Matching** - Qdrant searches return patterns used in risk calculation  
✅ **Similarity Scores** - Qdrant similarity scores directly determine risk points  
✅ **Multiple Searches** - 3 separate Qdrant searches per wallet analysis  
✅ **Vector Encoding** - All text converted to vectors for Qdrant search  
✅ **Collections** - 5 specialized Qdrant collections for different attack types  

---

## Risk Calculation Formula

```
Risk Score = 
  (Qdrant Pattern Similarity × Multiplier) +
  (Number of Pattern Matches × Bonus) +
  (Anomaly Severity × Confidence) +
  (Cluster Similarity × Weight)
```

**All components come from Qdrant searches!**

