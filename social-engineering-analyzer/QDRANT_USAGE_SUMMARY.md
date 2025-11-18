# 🔍 Qdrant Usage in Lurantis - Summary

## Overview
Qdrant is a vector database that stores high-dimensional vectors (embeddings) and enables fast similarity search. In Lurantis, we use it to detect social engineering attacks and analyze wallet behavior patterns.

---

## 10 Ways Qdrant is Used

### 1. **Vector Embeddings**
- Converts text/patterns to 768-dimensional vectors
- Uses Sentence Transformers model: `all-mpnet-base-v2`
- Each piece of text becomes a numerical vector

### 2. **Specialized Collections**
- 5 separate collections for different attack types:
  - `sim_swapping_patterns`
  - `wallet_stalking_patterns`
  - `address_spoofing_patterns`
  - `general_phishing_patterns`
  - `transaction_analysis_patterns`

### 3. **Pattern Storage**
- Stores 28+ real-world attack patterns
- Each pattern has metadata (severity, source, tactic)
- Patterns are converted to vectors and stored in Qdrant

### 4. **Similarity Search**
- Finds similar patterns in milliseconds
- Returns patterns with similarity scores (0-1)
- Uses cosine similarity for matching

### 5. **Multi-Collection Search**
- Searches across multiple collections simultaneously
- More comprehensive threat detection
- Better risk scoring

### 6. **Wallet Behavioral Clustering**
- Creates behavioral signatures for wallets
- Converts signatures to vectors
- Groups wallets by similar behavior patterns

### 7. **Anomaly Detection**
- Detects unusual wallet behavior
- Flags suspicious patterns
- Uses similarity thresholds to identify anomalies

### 8. **Address Spoofing Detection**
- Compares addresses character-by-character
- Uses Qdrant to find known spoofing patterns
- Detects if an address is trying to mimic another

### 9. **Transaction Pattern Analysis**
- Analyzes transaction patterns
- Creates pattern signatures
- Searches Qdrant for similar transaction patterns

### 10. **Relationship Mapping**
- Finds connections between wallets
- Uses vector similarity to find related wallets
- Maps suspicious networks

---

## Technical Details

- **Model:** `all-mpnet-base-v2` (768 dimensions)
- **Distance Metric:** Cosine Similarity
- **Collections:** 5 specialized collections
- **Storage:** Qdrant Cloud
- **Search Speed:** Milliseconds
- **Scalability:** Millions of patterns

---

## Why Qdrant?

✅ **Fast** - Millisecond search times  
✅ **Scalable** - Handles millions of patterns  
✅ **Semantic** - Understands meaning, not just keywords  
✅ **Flexible** - Easy to add new patterns  
✅ **Multi-dimensional** - Captures complex relationships  

---

## Code Locations

- **Service:** `backend/services/enhanced_qdrant_service.py`
- **Analyzer:** `backend/services/onchain_analyzer.py`
- **Seed Script:** `backend/scripts/seed_enhanced_patterns.py`
- **API:** `backend/app_enhanced.py`

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

