# Social Engineering Attack Analyzer

A Web3 SaaS platform that uses vector search (Qdrant) to identify flaws in social engineering attack architectures, similar to @zachxbt's investigative work.

## ⚠️ Current Status: Problem Definition Phase

**Before building, we're refining the idea and defining the exact problem we're solving.**

See the `docs/` folder for:
- `PROBLEM_DEFINITION.md` - Framework to define the problem
- `RESEARCH_NOTES.md` - Competitive analysis and research
- `SOLUTION_FRAMING.md` - Solution design exercise

**Please complete these before proceeding with development!**

---

## 🎯 What This Will Do (Concept)

The concept is to create a tool that uses AI and vector search to:
1. **Detect patterns** in social engineering attacks
2. **Identify threats** in real-time
3. **Map connections** between scam operations
4. **Protect users** from crypto fraud

**But first, we need to:**
- Clearly define WHO has this problem
- Understand WHAT they need specifically  
- Determine HOW we uniquely solve it
- Validate WHY they would use this vs alternatives

---

## 📁 Project Structure

```
social-engineering-analyzer/
├── docs/              # ⭐ START HERE - Problem definition & research
│   ├── PROBLEM_DEFINITION.md
│   ├── RESEARCH_NOTES.md
│   └── SOLUTION_FRAMING.md
├── frontend/          # Landing page (Next.js) - Built but awaiting direction
├── backend/           # API server (Python/FastAPI) - Built but awaiting direction
├── contracts/         # Smart contracts (Solidity) - Built but awaiting direction
└── deploy/            # AWS deployment configs - TBD
```

---

## 🚀 Getting Started

### ⚡ Quick Start (Qdrant Integration)

**Want to get the threat detection system running immediately?**

👉 **[QDRANT_QUICKSTART.md](./QDRANT_QUICKSTART.md)** - Get up and running in 5 minutes!

This will:
- Start Qdrant vector database
- Seed attack patterns
- Run the backend API
- Test threat detection

---

### Step 1: Define the Problem (DO THIS FIRST!)

1. Open `docs/PROBLEM_DEFINITION.md`
2. Answer the questions about:
   - Target users
   - Specific pain points
   - Unique solution
3. Research competitors and @zachxbt's work
4. Fill in `docs/RESEARCH_NOTES.md`

### Step 2: Frame the Solution

1. Open `docs/SOLUTION_FRAMING.md`
2. Write your one-sentence pitch
3. Define user stories
4. Prioritize features for MVP

### Step 3: Once Direction is Clear

Then we can proceed with:
- Refining the tech stack
- Building the MVP
- Deploying to production

---

## 💡 Current Working Hypothesis

**Problem:** [TO BE DEFINED - Fill this in after research]  
**User:** [TO BE DEFINED - Fill this in after research]  
**Solution:** [TO BE DEFINED - Fill this in after research]  
**Differentiator:** [TO BE DEFINED - Fill this in after research]

---

## 📚 Resources

### Learning Resources
- **Python Basics**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **Solidity Basics**: [CryptoZombies](https://cryptozombies.io/)
- **Qdrant Docs**: [qdrant.tech/documentation](https://qdrant.tech/documentation/)
- **Gnosis Chain**: [docs.gnosischain.com](https://docs.gnosischain.com/)

### Research Targets
- @zachxbt on Twitter/X - Study his investigative threads
- Spoonos - Understand competitor
- Crypto security tools - Market analysis

---

## ⏭️ Next Steps

1. **Complete problem definition** (docs/PROBLEM_DEFINITION.md)
2. **Research competitors** (docs/RESEARCH_NOTES.md)
3. **Frame solution** (docs/SOLUTION_FRAMING.md)
4. **Decide on MVP scope**
5. **Then proceed with development**

**Don't skip the research phase! It will save time later.**
