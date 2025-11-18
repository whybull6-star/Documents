# Installing Docker for Windows

## Quick Install

1. **Download Docker Desktop:**
   - Go to: https://www.docker.com/products/docker-desktop/
   - Click "Download for Windows"
   - Run the installer

2. **Install Docker Desktop:**
   - Run the downloaded `.exe` file
   - Follow the installation wizard
   - **Important**: Make sure "Use WSL 2 instead of Hyper-V" is checked (if available)
   - Restart your computer when prompted

3. **Start Docker Desktop:**
   - After restart, open Docker Desktop from Start Menu
   - Wait for it to start (you'll see a whale icon in system tray)
   - Docker is ready when the icon stops animating

4. **Verify Installation:**
   - Open a NEW terminal/command prompt
   - Run: `docker --version`
   - You should see: `Docker version XX.XX.X`

5. **Now run the Qdrant command:**
   ```bash
   docker run -d -p 6333:6333 --name qdrant qdrant/qdrant
   ```

---

## Alternative: Run Qdrant Without Docker

If you don't want to install Docker, you can use **Qdrant Cloud** (free tier available):

### Option A: Use Qdrant Cloud (Easiest)

1. **Sign up for free:**
   - Go to: https://cloud.qdrant.io/
   - Sign up (free tier available)
   - Create a cluster

2. **Get your cluster URL:**
   - Copy your cluster URL (looks like: `https://xxxxx.qdrant.io`)
   - Copy your API key

3. **Update your `.env` file:**
   ```env
   QDRANT_URL=https://your-cluster-url.qdrant.io
   QDRANT_API_KEY=your-api-key-here
   ```

4. **Skip the Docker step** and continue with backend setup!

---

### Option B: Install Qdrant Locally (Advanced)

If you have Python, you can run Qdrant directly:

```bash
pip install qdrant-client
```

But this requires more setup. **Docker is the easiest option.**

---

## Troubleshooting Docker Installation

### "Docker Desktop won't start"
- Make sure virtualization is enabled in BIOS
- Check Windows features: Enable "Virtual Machine Platform" and "Windows Subsystem for Linux"
- Restart computer

### "WSL 2 installation is incomplete"
- Install WSL 2: https://aka.ms/wsl2kernel
- Restart computer
- Try Docker Desktop again

### Still having issues?
- Use Qdrant Cloud instead (Option A above) - it's free and easier!

