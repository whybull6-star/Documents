# Backend - Python FastAPI Server

The backend API that handles analysis requests, manages Qdrant connections, and processes credit payments.

## What This Does (ELI5)

Think of the backend as a waiter at a restaurant:
1. **Frontend** (customer) asks for something
2. **Backend** (waiter) takes the order
3. **Qdrant** (kitchen) finds similar patterns
4. **Backend** brings back the results

## Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start Qdrant (if not running):**
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

5. **Seed the database:**
   ```bash
   python scripts/seed_data.py
   ```

6. **Run the server:**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Health check
- `GET /health` - Detailed health status
- `POST /analyze` - Analyze content for threats
- `GET /credits/{address}` - Get credit balance
- `POST /credits/topup` - Add credits (admin)
- `GET /patterns` - Get database stats

## Testing

Test the API with curl:

```bash
# Health check
curl http://localhost:8000/health

# Analyze content
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"content": "URGENT: Click here to verify your account!"}'
```

## Project Structure

```
backend/
├── app.py                 # Main FastAPI application
├── services/
│   ├── qdrant_service.py # Qdrant vector database interactions
│   ├── analyzer.py       # Main analysis logic
│   └── credit_manager.py # Credit/billing management
├── scripts/
│   └── seed_data.py      # Seed database with sample patterns
└── requirements.txt      # Python dependencies
```


