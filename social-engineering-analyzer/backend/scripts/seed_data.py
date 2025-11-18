"""
Script to seed Qdrant with initial attack patterns
Run this after setting up Qdrant to populate the database
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.qdrant_service import QdrantService

# Sample attack patterns to seed the database
# These are real-world examples of social engineering attempts
ATTACK_PATTERNS = [
    {
        "id": 1,
        "text": "URGENT: Your account has been suspended. Click here immediately to verify your identity and restore access.",
        "type": "Account Suspension Scam",
        "source": "phishing_email"
    },
    {
        "id": 2,
        "text": "Congratulations! You've won $10,000. Click this link to claim your prize. Limited time offer - act now!",
        "type": "Fake Prize Scam",
        "source": "phishing_email"
    },
    {
        "id": 3,
        "text": "We detected unusual activity on your account. Please verify your login credentials immediately to secure your account.",
        "type": "Account Security Scam",
        "source": "phishing_email"
    },
    {
        "id": 4,
        "text": "Your payment method on file is expired. Update your billing information now to avoid service interruption.",
        "type": "Payment Scam",
        "source": "phishing_email"
    },
    {
        "id": 5,
        "text": "Hi, this is your bank. We need to verify some information for security purposes. Can you provide your social security number?",
        "type": "Impersonation Scam",
        "source": "phone_call"
    },
    {
        "id": 6,
        "text": "You have a package delivery pending. Click here to track and schedule delivery. (Link goes to fake site)",
        "type": "Fake Delivery Scam",
        "source": "smishing"
    },
    {
        "id": 7,
        "text": "Your crypto wallet needs verification. Send 0.1 ETH to this address to unlock your funds.",
        "type": "Crypto Scam",
        "source": "blockchain_scam"
    },
    {
        "id": 8,
        "text": "I'm a Nigerian prince with millions to share. Send me $5000 and I'll give you $1 million in return.",
        "type": "Advance Fee Fraud",
        "source": "email_scam"
    },
    {
        "id": 9,
        "text": "Your computer has been infected with a virus! Download this antivirus software immediately to protect your files.",
        "type": "Malware Scam",
        "source": "tech_support_scam"
    },
    {
        "id": 10,
        "text": "Your subscription is about to expire. Renew now with this special 90% discount offer - today only!",
        "type": "Urgency Scam",
        "source": "phishing_email"
    },
]

async def seed_database():
    """Add sample attack patterns to Qdrant"""
    print("Initializing Qdrant service...")
    qdrant = QdrantService()
    
    print(f"Seeding {len(ATTACK_PATTERNS)} attack patterns...")
    
    for pattern in ATTACK_PATTERNS:
        await qdrant.add_pattern(
            pattern_id=pattern["id"],
            text=pattern["text"],
            metadata={
                "type": pattern["type"],
                "source": pattern["source"]
            }
        )
        print(f"  ✓ Added: {pattern['type']}")
    
    print("\n✅ Database seeded successfully!")
    print(f"   Collection: {qdrant.collection_name}")
    
    # Verify
    info = await qdrant.get_collection_info()
    print(f"   Total patterns: {info['vectors_count']}")

if __name__ == "__main__":
    asyncio.run(seed_database())


