# Getting Started Guide (ELI5)

## What You're Building

You're creating a tool that helps people detect scams and social engineering attacks by:
1. Storing information about known scams in a special database (Qdrant)
2. When someone sends you a message/link, comparing it to known scams
3. Using blockchain (Gnosis) to handle payments for using the service

## Understanding the Pieces

### 1. Frontend (Landing Page)
**What it is**: The website people visit  
**Technology**: Next.js (like WordPress but for modern websites)  
**Purpose**: Beautiful page that explains your service and lets people sign up

### 2. Backend (API Server)
**What it is**: The brain that does the actual work  
**Technology**: Python with FastAPI (Python is like JavaScript but for servers)  
**Purpose**: 
- Takes requests from frontend
- Connects to Qdrant to search for scam patterns
- Manages user credits
- Calls AI services

### 3. Smart Contracts (Blockchain)
**What it is**: Code that runs on blockchain (can't be changed once deployed)  
**Technology**: Solidity (special language for blockchain)  
**Purpose**: 
- Handles payments
- Tracks user credits
- Stores transactions on Gnosis chain

### 4. Qdrant (Vector Database)
**What it is**: Special database that understands meaning, not just exact words  
**Purpose**: Stores scam patterns and helps find similar ones

## Setup Checklist

- [ ] Install Python 3.9+
- [ ] Install Node.js 18+
- [ ] Install Docker (for Qdrant)
- [ ] Get a wallet for Gnosis (MetaMask)
- [ ] Get AWS account (for hosting)
- [ ] Get a domain name (.com)

## Step-by-Step Development

1. **First**: Build the landing page (see frontend setup)
2. **Second**: Set up Qdrant and add some test scam data
3. **Third**: Build the backend API to connect everything
4. **Fourth**: Create smart contracts for payments
5. **Fifth**: Connect frontend to backend
6. **Sixth**: Deploy everything to AWS

Follow each folder's README for detailed steps!


