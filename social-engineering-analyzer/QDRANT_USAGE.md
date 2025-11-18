# 🔍 How Qdrant is Used in This Project

## Overview
Qdrant is a vector database that stores high-dimensional vectors (embeddings) and enables fast similarity search. In this project, we use it to detect social engineering attacks and analyze wallet behavior patterns.

---

## 1. Vector Embeddings: Converting Text to Numbers

### What It Does
- Converts text (messages, wallet patterns, attack descriptions) into numerical vectors
- Uses **Sentence Transformers** model: `all-mpnet-base-v2` (768 dimensions)
- Each piece of text becomes a 768-dimensional vector

### Example:
```
Text: "Your wallet is compromised! Send funds immediately!"
↓ (Embedding)
Vector: [0.123, -0.456, 0.789, ..., 0.234] (768 numbers)
```

### Code Location:
- `backend/services/enhanced_qdrant_service.py`
- Method: `encode_text(text: str) -> List[float]`

---

## 2. Specialized Collections: Organizing Attack Types

### What It Does
We store different types of attack patterns in separate Qdrant collections:

1. **`sim_swapping_patterns`** - SIM swap attack indicators
2. **`wallet_stalking_patterns`** - Wallet tracking and stalking attempts
3. **`address_spoofing_patterns`** - Address spoofing and phishing
4. **`general_phishing_patterns`** - General social engineering patterns
5. **`transaction_analysis_patterns`** - On-chain transaction patterns

### Why Separate Collections?
- **Better organization** - Each attack type has its own space
- **Faster searches** - Only search relevant collections
- **Better accuracy** - Patterns are grouped by similarity
- **Easier updates** - Add new patterns to specific collections

### Code Location:
- `backend/services/enhanced_qdrant_service.py`
- Method: `_ensure_all_collections()`

---

## 3. Pattern Storage: Saving Known Attack Patterns

### What It Does
Stores real-world attack patterns as vectors in Qdrant:

```python
Pattern Example:
{
    "id": "sim_swap_001",
    "text": "We need to verify your identity. Please provide your phone number to port your SIM card.",
    "attack_type": "sim_swapping",
    "metadata": {
        "severity": "critical",
        "source": "real_world_case"
    }
}
```

### How It Works:
1. Convert pattern text to vector
2. Store in appropriate collection
3. Can search later for similar patterns

### Code Location:
- `backend/services/enhanced_qdrant_service.py`
- Method: `add_attack_pattern()`
- Seed script: `backend/scripts/seed_enhanced_patterns.py`

---

## 4. Similarity Search: Finding Matching Patterns

### What It Does
When analyzing new content, we:
1. Convert it to a vector
2. Search Qdrant for similar vectors
3. Return patterns with highest similarity scores

### Example:
```
User Input: "URGENT: Your wallet needs verification!"
↓ (Convert to vector)
↓ (Search Qdrant)
Found: "address_spoofing_003" (similarity: 0.87)
Found: "general_phishing_012" (similarity: 0.82)
```

### Code Location:
- `backend/services/enhanced_qdrant_service.py`
- Method: `search_attack_patterns()`

---

## 5. Multi-Collection Search: Searching Across Attack Types

### What It Does
Searches multiple collections simultaneously to find all relevant patterns:

```python
Search across:
- sim_swapping_patterns
- wallet_stalking_patterns
- address_spoofing_patterns
- general_phishing_patterns
```

### Why This Matters:
- A single message might match multiple attack types
- More comprehensive threat detection
- Better risk scoring

### Code Location:
- `backend/services/enhanced_qdrant_service.py`
- Method: `search_attack_patterns()` with multiple `attack_types`

---

## 6. Wallet Behavioral Clustering: Grouping Similar Wallets

### What It Does
1. Creates a "behavioral signature" for each wallet
2. Converts signature to vector
3. Searches Qdrant for wallets with similar behavior
4. Groups wallets into behavioral clusters

### Example:
```
Wallet A: "High transaction volume, many small transfers"
↓ (Vector)
↓ (Search Qdrant)
Found: "wallet_stalking_pattern_005" (similarity: 0.75)
→ This wallet behaves like known stalking wallets
```

### Code Location:
- `backend/services/onchain_analyzer.py`
- Method: `_find_behavioral_cluster()`

---

## 7. Anomaly Detection: Finding Unusual Patterns

### What It Does
1. Analyzes wallet behavior
2. Searches Qdrant for known suspicious patterns
3. If similarity is high → anomaly detected
4. Flags unusual transaction patterns

### Example:
```
Normal wallet: Low similarity to suspicious patterns (0.2)
Suspicious wallet: High similarity to known scams (0.85)
→ Anomaly detected!
```

### Code Location:
- `backend/services/onchain_analyzer.py`
- Method: `_detect_anomalies()`

---

## 8. Address Spoofing Detection: Finding Similar-Looking Addresses

### What It Does
1. Compares wallet addresses character-by-character
2. Uses Qdrant to find known spoofing patterns
3. Detects if an address is trying to mimic another

### Example:
```
Your address: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEa
Suspicious:   0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
→ Only last character differs → Likely spoofing attempt
```

### Code Location:
- `backend/services/enhanced_qdrant_service.py`
- Method: `check_address_spoofing()`

---

## 9. Transaction Pattern Analysis: Detecting Suspicious On-Chain Activity

### What It Does
1. Analyzes transaction patterns (volume, frequency, recipients)
2. Creates pattern signature
3. Searches Qdrant for similar transaction patterns
4. Identifies known scam transaction flows

### Example:
```
Pattern: "Many small transactions to different addresses"
↓ (Search Qdrant)
Found: "dusting_attack_pattern" (similarity: 0.78)
→ Likely dusting attack
```

### Code Location:
- `backend/services/onchain_analyzer.py`
- Method: `_analyze_transaction_patterns()`

---

## 10. Relationship Mapping: Finding Connected Wallets

### What It Does
1. Analyzes wallet interactions
2. Uses vector similarity to find related wallets
3. Maps connections between suspicious addresses

### Example:
```
Wallet A interacts with Wallet B
↓ (Both have similar behavioral vectors)
↓ (Search Qdrant)
Found: Both match "scam_network_pattern_003"
→ Likely part of same scam operation
```

### Code Location:
- `backend/services/onchain_analyzer.py`
- Method: `_identify_wallet_relationships()`

---

## Technical Details

### Vector Model
- **Model:** `all-mpnet-base-v2` (Sentence Transformers)
- **Dimensions:** 768
- **Distance Metric:** Cosine Similarity
- **Why this model:** Better semantic understanding than smaller models

### Qdrant Configuration
- **Collections:** 5 specialized collections
- **Vector Size:** 768 dimensions
- **Distance:** Cosine
- **Storage:** Qdrant Cloud (or local Docker)

### Search Parameters
- **Limit:** 5-10 results per search
- **Score Threshold:** 0.3-0.5 (adjustable)
- **Multiple Collections:** Searched in parallel

---

## Why Qdrant is Perfect for This

### ✅ Advantages:
1. **Fast Similarity Search** - Finds similar patterns in milliseconds
2. **Semantic Understanding** - Understands meaning, not just keywords
3. **Scalable** - Can handle millions of patterns
4. **Flexible** - Easy to add new patterns
5. **Multi-dimensional** - Captures complex relationships

### 🎯 Use Cases Enabled:
- Real-time threat detection
- Pattern matching across different attack types
- Behavioral analysis
- Anomaly detection
- Relationship mapping

---

## Current Limitations & Future Improvements

### Current:
- Basic pattern matching
- Limited transaction data
- Simple behavioral signatures

### Future:
- Real transaction history analysis
- More sophisticated behavioral vectors
- Temporal pattern analysis (how patterns change over time)
- Cross-chain analysis
- Machine learning model training on Qdrant data

---

## Summary

**Qdrant is the core intelligence engine** that:
1. Stores known attack patterns as vectors
2. Searches for similar patterns in real-time
3. Groups wallets by behavior
4. Detects anomalies
5. Maps relationships

**Without Qdrant**, we'd only have keyword matching (slow, inaccurate).  
**With Qdrant**, we have semantic understanding and fast similarity search (fast, accurate, scalable).

