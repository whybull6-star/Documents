# 🌐 Qdrant Cloud Setup - Step by Step

## Step 1: Sign Up for Qdrant Cloud

1. **Open your web browser** and go to:
   ```
   https://cloud.qdrant.io/
   ```

2. **Click "Sign Up"** (top right corner)

3. **Choose sign-up method:**
   - Sign up with email (recommended)
   - Or use GitHub/Google if you prefer

4. **Fill in your details:**
   - Email address
   - Password
   - Accept terms and conditions

5. **Verify your email:**
   - Check your inbox
   - Click the verification link
   - You'll be redirected back to Qdrant Cloud

---

## Step 2: Create Your First Cluster

1. **After logging in**, you'll see the dashboard

2. **Click "Create Cluster"** button (usually a big green/blue button)

3. **Fill in cluster details:**
   - **Cluster Name**: `lurantis-dev` (or any name you like)
   - **Region**: Choose closest to you (e.g., `us-east-1` for US East)
   - **Plan**: Select **"Free"** or **"Starter"** (free tier is fine for testing)

4. **Click "Create Cluster"**

5. **Wait for cluster to be created** (~2-3 minutes)
   - You'll see a progress indicator
   - Status will change from "Creating" to "Running"

---

## Step 3: Get Your Credentials

Once your cluster is running:

1. **Click on your cluster name** to open cluster details

2. **Find the "Connection" or "API" section**

3. **Copy these two things:**

   **a) Cluster URL:**
   - Looks like: `https://xxxxx.us-east-1-0.aws.cloud.qdrant.io`
   - Or: `https://xxxxx.eu-west-1-0.aws.cloud.qdrant.io`
   - **Copy the entire URL**

   **b) API Key:**
   - Click "Show API Key" or "Generate API Key"
   - **Copy the API key** (long string of characters)
   - ⚠️ **Save this somewhere safe!** You won't be able to see it again

---

## Step 4: Update Your Backend Configuration

### Option A: Using PowerShell (Easiest)

1. **Open PowerShell** (Win + X, then click "Windows PowerShell")

2. **Navigate to your backend folder:**
   ```powershell
   cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
   ```

3. **Create the .env file:**
   ```powershell
   # Replace YOUR_CLUSTER_URL and YOUR_API_KEY with your actual values
   @"
   QDRANT_URL=https://your-cluster-url.qdrant.io
   QDRANT_API_KEY=your-api-key-here
   API_URL=http://localhost:8000
   "@ | Out-File -FilePath .env -Encoding utf8
   ```

4. **Edit the file:**
   - Open `.env` file in Notepad
   - Replace `https://your-cluster-url.qdrant.io` with your actual cluster URL
   - Replace `your-api-key-here` with your actual API key
   - Save the file

### Option B: Manual Creation (Simpler)

1. **Navigate to backend folder:**
   ```bash
   cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
   ```

2. **Create a new file named `.env`** in that folder

3. **Open it in Notepad** and paste this:
   ```
   QDRANT_URL=https://your-cluster-url.qdrant.io
   QDRANT_API_KEY=your-api-key-here
   API_URL=http://localhost:8000
   ```

4. **Replace the placeholders:**
   - Replace `https://your-cluster-url.qdrant.io` with your actual cluster URL
   - Replace `your-api-key-here` with your actual API key

5. **Save the file**

---

## Step 5: Update Qdrant Service to Use API Key

We need to update the code to use the API key. Let me check the current implementation:

**The enhanced Qdrant service should already support API keys, but let's verify:**

Open `backend/services/enhanced_qdrant_service.py` and check the `__init__` method. It should look like this:

```python
def __init__(self):
    # Get Qdrant URL from environment or use default
    self.qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    self.qdrant_api_key = os.getenv("QDRANT_API_KEY", None)
    
    # Initialize Qdrant client
    if self.qdrant_api_key:
        self.client = QdrantClient(url=self.qdrant_url, api_key=self.qdrant_api_key)
    else:
        self.client = QdrantClient(url=self.qdrant_url)
```

If it doesn't have API key support, we'll need to update it.

---

## Step 6: Test the Connection

1. **Make sure your `.env` file is correct**

2. **Activate your virtual environment:**
   ```bash
   cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
   venv\Scripts\activate
   ```

3. **Test the connection:**
   ```bash
   python -c "from services.enhanced_qdrant_service import EnhancedQdrantService; import asyncio; q = EnhancedQdrantService(); print('Connected!' if asyncio.run(q.check_health()) else 'Failed')"
   ```

   Or simply try seeding:
   ```bash
   python scripts/seed_enhanced_patterns.py
   ```

---

## Step 7: Continue with Setup

Once connected, continue with the normal setup:

```bash
# Seed the database
python scripts/seed_enhanced_patterns.py

# Start the server
python app_enhanced.py
```

---

## ✅ Verification Checklist

- [ ] Qdrant Cloud account created
- [ ] Cluster created and status is "Running"
- [ ] Cluster URL copied
- [ ] API key copied and saved
- [ ] `.env` file created in `backend/` folder
- [ ] `.env` file contains correct URL and API key
- [ ] Connection test successful
- [ ] Database seeded successfully

---

## 🐛 Troubleshooting

### "Invalid API key" error
- Double-check your API key in `.env` file
- Make sure there are no extra spaces
- Try generating a new API key in Qdrant Cloud

### "Connection refused" error
- Verify your cluster URL is correct
- Make sure cluster status is "Running" in Qdrant Cloud dashboard
- Check if URL starts with `https://`

### Can't find API key
- Go to your cluster in Qdrant Cloud
- Look for "API" or "Connection" tab
- Click "Show API Key" or "Generate New API Key"

### Still having issues?
- Make sure your `.env` file is in the `backend/` folder (not root folder)
- Check file is named exactly `.env` (not `.env.txt`)
- Restart your terminal after creating `.env` file

---

## 📝 Example .env File

Your `.env` file should look like this (with your actual values):

```
QDRANT_URL=https://abc123def456.us-east-1-0.aws.cloud.qdrant.io
QDRANT_API_KEY=QDRANT_API_KEY_abc123def456ghi789jkl012mno345pqr678stu901vwx234yz
API_URL=http://localhost:8000
```

**Important:** 
- No quotes around the values
- No spaces around the `=` sign
- One value per line

---

## 🎉 Next Steps

Once everything is connected:
1. Seed the database: `python scripts/seed_enhanced_patterns.py`
2. Start the server: `python app_enhanced.py`
3. Test it: `curl http://localhost:8000/health`

You're all set! 🚀

