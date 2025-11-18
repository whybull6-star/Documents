# 🔍 Complete Proof: All Qdrant Usage for Risk Assessment

## Overview
This document shows **every single instance** where Qdrant is used to assess risk factors, with exact file paths, line numbers, and code snippets.

---

## 1. Transaction Pattern Analysis (PRIMARY)
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
- Creates behavioral signature from wallet (balance, patterns)
- Searches 4 Qdrant collections simultaneously
- Returns pattern matches with similarity scores (0-1)
- **This is the PRIMARY source for risk calculation**

### Risk Impact:
- Pattern matches stored in `tx_patterns["similar_patterns"]`
- Used directly in `_calculate_risk()` method
- Similarity scores determine risk points

---

## 2. Behavioral Cluster Detection
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_find_behavioral_cluster()`  
**Lines:** 167-172

### Code:
```python
results = await self.qdrant.search_attack_patterns(
    cluster_text,
    attack_types=["transaction_analysis", "wallet_stalking"],
    limit=5,
    score_threshold=0.2
)
```

### What It Does:
- Searches Qdrant for similar wallet behaviors
- Groups wallets into behavioral clusters
- Returns cluster similarity score

### Risk Impact:
- Used in `_calculate_risk()` line 317-322
- If similarity > 0.3, adds `similarity * 25` to risk score
- Contributes to risk factors list

---

## 3. Wallet Relationship Identification
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_identify_wallet_relationships()`  
**Lines:** 196-201

### Code:
```python
results = await self.qdrant.search_attack_patterns(
    relationship_text,
    attack_types=["wallet_stalking"],
    limit=5,
    score_threshold=0.4
)
```

### What It Does:
- Searches Qdrant for wallet relationship patterns
- Identifies suspicious connections
- Returns relationship confidence scores

### Risk Impact:
- Relationships stored in analysis results
- Can be used for additional risk scoring
- Shows wallet connections in UI

---

## 4. Anomaly Detection
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_detect_anomalies()`  
**Lines:** 226-231

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
- Used in `_calculate_risk()` lines 304-314
- Each anomaly adds to risk:
  - Critical: `confidence * 40`
  - High: `confidence * 30`
  - Medium: `confidence * 20`

---

## 5. Risk Score Calculation (PRIMARY - Uses Qdrant Results)
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `_calculate_risk()`  
**Lines:** 257-301

### Code:
```python
# PRIMARY: Pattern matches from Qdrant - THIS IS WHAT MATTERS
pattern_matches = tx_patterns.get("pattern_matches_count", 0)
similar_patterns = tx_patterns.get("similar_patterns", {})  # From Qdrant search #1

for attack_type, patterns in similar_patterns.items():
    if patterns:
        for pattern in patterns:
            score = pattern.get("score", 0.0)  # Qdrant similarity score
            
            if score > 0.7:
                risk_score += score * 60  # Qdrant score directly determines risk
            elif score > 0.5:
                risk_score += score * 45
            elif score > 0.3:
                risk_score += score * 30
            elif score > 0.1:
                risk_score += score * 15
```

### What It Does:
- Takes Qdrant pattern matches from `_analyze_transaction_patterns()`
- Uses Qdrant similarity scores (0-1) to calculate risk
- Qdrant scores directly multiplied to get risk points

### Risk Impact:
- **PRIMARY risk calculation method**
- 100% dependent on Qdrant results
- No Qdrant matches = 0 risk (normal wallet)

---

## 6. Transaction Flow Tracing
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `trace_transaction_flow()`  
**Lines:** 406-410

### Code:
```python
results = await self.qdrant.search_attack_patterns(
    flow_text,
    attack_types=["transaction_analysis", "wallet_stalking"],
    limit=5,
    score_threshold=0.3
)
```

### What It Does:
- Searches Qdrant for transaction flow patterns
- Analyzes fund movements
- Detects suspicious transaction patterns

### Risk Impact:
- Used for transaction flow analysis
- Can identify money laundering patterns
- Contributes to overall risk assessment

---

## 7. Wallet Cluster Detection (Multiple Wallets)
**File:** `backend/services/onchain_analyzer.py`  
**Method:** `detect_wallet_cluster()`  
**Lines:** 438-439

### Code:
```python
vector = self.qdrant.encode_text(sig)  # Convert to vector for comparison
```

### What It Does:
- Encodes wallet signatures to vectors
- Compares multiple wallets using vector similarity
- Groups related wallets

### Risk Impact:
- Identifies wallet networks
- Can detect coordinated attacks
- Shows relationships between wallets

---

## 8. Enhanced Analyzer (Text Analysis)
**File:** `backend/services/enhanced_analyzer.py`  
**Method:** `analyze_comprehensive()`  
**Line:** 69

### Code:
```python
general_results = await self.qdrant.search_attack_patterns(
    content,
    attack_types=["sim_swapping", "wallet_stalking", "address_spoofing", "general_phishing"],
    limit=5,
    score_threshold=0.4
)
```

### What It Does:
- Analyzes text content (messages, emails)
- Searches all 4 Qdrant collections
- Detects social engineering patterns in text

### Risk Impact:
- Used for text-based threat detection
- Different use case (not wallet analysis)
- Still uses Qdrant for pattern matching

---

## 9. Qdrant Service - Core Implementation
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
    query_vector = self.encode_text(query_text)  # Convert to 768-dim vector
    
    for collection_name in collections_to_search:
        search_results = self.client.search(  # QDRANT SEARCH
            collection_name=collection_name,
            query_vector=query_vector,  # Vector from Sentence Transformers
            limit=limit,
            score_threshold=score_threshold
        )
```

### What It Does:
- **Core Qdrant search function**
- Converts text to vector using Sentence Transformers
- Searches Qdrant collections using cosine similarity
- Returns patterns with similarity scores

### Risk Impact:
- **ALL risk assessments depend on this**
- Every Qdrant search goes through here
- Vector similarity determines all pattern matches

---

## 10. Vector Encoding (Foundation)
**File:** `backend/services/enhanced_qdrant_service.py`  
**Method:** `encode_text()`  
**Lines:** 73-75

### Code:
```python
def encode_text(self, text: str) -> List[float]:
    vector = self.model.encode(text, normalize_embeddings=True).tolist()
    return vector  # 768-dimensional vector
```

### What It Does:
- Uses `all-mpnet-base-v2` model
- Converts text to 768-dimensional vector
- Required for all Qdrant searches

### Risk Impact:
- **Foundation of all Qdrant operations**
- Without this, no vector search works
- All risk assessments depend on this

---

## 11. Address Spoofing Detection
**File:** `backend/services/enhanced_qdrant_service.py`  
**Method:** `detect_address_spoofing()`  
**Lines:** 250-260

### Code:
```python
results = await self.search_attack_patterns(
    f"address spoofing {suspicious_address} similar to {known_address}",
    attack_types=["address_spoofing"],
    limit=3,
    score_threshold=0.3
)
```

### What It Does:
- Searches Qdrant for address spoofing patterns
- Uses vector similarity to detect spoofing
- Returns spoofing confidence scores

### Risk Impact:
- Used in enhanced analyzer
- Detects address spoofing attacks
- Contributes to threat detection

---

## 12. SIM Swapping Detection
**File:** `backend/services/enhanced_qdrant_service.py`  
**Method:** `detect_sim_swapping()`  
**Lines:** 306-315

### Code:
```python
results = await self.search_attack_patterns(
    content,
    attack_types=["sim_swapping"],
    limit=5,
    score_threshold=0.4
)
```

### What It Does:
- Searches Qdrant `sim_swapping_patterns` collection
- Detects SIM swap attack indicators
- Returns pattern matches

### Risk Impact:
- Used in enhanced analyzer
- Detects SIM swapping attempts
- Contributes to threat score

---

## 13. Wallet Stalking Detection
**File:** `backend/services/enhanced_qdrant_service.py`  
**Method:** `detect_wallet_stalking()`  
**Lines:** 360-370

### Code:
```python
results = await self.search_attack_patterns(
    content,
    attack_types=["wallet_stalking"],
    limit=5,
    score_threshold=0.4
)
```

### What It Does:
- Searches Qdrant `wallet_stalking_patterns` collection
- Detects wallet tracking/stalking patterns
- Returns stalking indicators

### Risk Impact:
- Used in enhanced analyzer
- Detects wallet stalking attempts
- Contributes to threat score

---

## Complete Flow: Wallet Analysis → Risk Assessment

```
1. analyze_wallet_activity() called
   ↓
2. _analyze_transaction_patterns() [QDRANT SEARCH #1]
   - Creates signature: "wallet with zero balance..."
   - Searches: transaction_analysis, wallet_stalking, address_spoofing, general_phishing
   - Returns: pattern matches with similarity scores
   ↓
3. _find_behavioral_cluster() [QDRANT SEARCH #2]
   - Searches: transaction_analysis, wallet_stalking
   - Returns: cluster similarity
   ↓
4. _identify_wallet_relationships() [QDRANT SEARCH #3]
   - Searches: wallet_stalking
   - Returns: relationship patterns
   ↓
5. _detect_anomalies() [QDRANT SEARCH #4]
   - Searches: transaction_analysis
   - Returns: anomalies with severity
   ↓
6. _calculate_risk() [USES QDRANT RESULTS]
   - Takes pattern matches from step 2
   - Uses similarity scores: score * 60/45/30/15
   - Uses anomalies from step 5: severity * confidence
   - Uses cluster from step 3: similarity * 25
   - Calculates final risk score
   ↓
7. Returns risk assessment
```

---

## Risk Calculation Formula (All from Qdrant)

```
Risk Score = 
  Σ(Qdrant Pattern Similarity × Multiplier) +      [From search #1]
  (Number of Pattern Matches × Bonus) +            [From search #1]
  Σ(Anomaly Severity × Qdrant Confidence) +        [From search #4]
  (Cluster Similarity × 25) +                      [From search #2]
  (Relationship Confidence)                        [From search #3]
```

**Every component comes from Qdrant!**

---

## Files Summary

### Primary Risk Assessment:
1. **`backend/services/onchain_analyzer.py`**
   - Line 125: Transaction pattern search
   - Line 167: Behavioral cluster search
   - Line 196: Relationship search
   - Line 226: Anomaly detection search
   - Line 257-301: Risk calculation (uses all Qdrant results)
   - Line 406: Transaction flow search

### Core Qdrant Service:
2. **`backend/services/enhanced_qdrant_service.py`**
   - Line 73: Vector encoding
   - Line 111: Core search function
   - Line 250: Address spoofing search
   - Line 306: SIM swapping search
   - Line 360: Wallet stalking search

### Text Analysis:
3. **`backend/services/enhanced_analyzer.py`**
   - Line 69: General pattern search

---

## Proof Summary

✅ **4 Qdrant searches per wallet analysis**  
✅ **All risk scores calculated from Qdrant similarity scores**  
✅ **5 specialized Qdrant collections used**  
✅ **768-dimensional vector embeddings**  
✅ **Cosine similarity for pattern matching**  
✅ **Every risk factor comes from Qdrant results**  

**Qdrant is the ONLY source of risk assessment data!**

