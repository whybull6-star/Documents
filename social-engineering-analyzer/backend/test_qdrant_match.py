"""
Quick test to verify Qdrant is working and patterns are seeded
"""
import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.enhanced_qdrant_service import EnhancedQdrantService

async def test_qdrant():
    print("Testing Qdrant connection and pattern matching...")
    
    qdrant = EnhancedQdrantService()
    
    # Test 1: Check if collections exist
    print("\n1. Checking collections...")
    stats = await qdrant.get_collection_stats()
    for attack_type, stat in stats.items():
        if "error" not in stat:
            print(f"   ✓ {attack_type}: {stat['vectors_count']} patterns")
        else:
            print(f"   ✗ {attack_type}: Error - {stat['error']}")
    
    # Test 2: Search for zero balance pattern (exact match)
    print("\n2. Testing exact pattern match...")
    test_query = "wallet with zero balance and no transaction history suspicious empty wallet pattern"
    results = await qdrant.search_attack_patterns(
        test_query,
        attack_types=["transaction_analysis"],
        limit=5,
        score_threshold=0.1
    )
    
    if results.get("transaction_analysis"):
        print(f"   ✓ Found {len(results['transaction_analysis'])} matches")
        for i, match in enumerate(results['transaction_analysis'][:3]):
            print(f"      Match {i+1}: score={match['score']:.3f}, id={match['id']}")
            print(f"      Text: {match['payload'].get('text', '')[:80]}...")
    else:
        print("   ✗ NO MATCHES FOUND - Patterns might not be seeded!")
        print("   Run: python scripts/seed_enhanced_patterns.py")
    
    # Test 3: Test with different query
    print("\n3. Testing with different query...")
    test_query2 = "suspicious wallet behavior pattern unusual transaction flow"
    results2 = await qdrant.search_attack_patterns(
        test_query2,
        attack_types=["transaction_analysis"],
        limit=5,
        score_threshold=0.1
    )
    
    if results2.get("transaction_analysis"):
        print(f"   ✓ Found {len(results2['transaction_analysis'])} matches")
        for i, match in enumerate(results2['transaction_analysis'][:3]):
            print(f"      Match {i+1}: score={match['score']:.3f}")
    else:
        print("   ✗ NO MATCHES FOUND")

if __name__ == "__main__":
    asyncio.run(test_qdrant())

