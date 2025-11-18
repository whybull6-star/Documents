# 📦 Git Setup - Quick Reference

## First Time Setup

### 1. Check Git Installation
```bash
git --version
```

### 2. Configure Git (First Time Only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Navigate to Project
```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer
```

### 4. Initialize Git
```bash
git init
```

### 5. Check Status
```bash
git status
```

### 6. Add All Files
```bash
git add .
```

### 7. Commit
```bash
git commit -m "Initial commit - Lurantis project"
```

---

## Push to GitHub

### 1. Create GitHub Repository
- Go to: https://github.com/new
- Name: `lurantis`
- **Don't** initialize with README
- Click "Create repository"

### 2. Connect to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/lurantis.git
```

### 3. Rename Branch
```bash
git branch -M main
```

### 4. Push
```bash
git push -u origin main
```

**If asked for password**: Use Personal Access Token (not password)

---

## Create Personal Access Token

1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. Name: "Vercel Deployment"
5. Select scope: ✅ `repo`
6. Generate token
7. **Copy token** (use as password)

---

## Common Commands

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# Pull from GitHub
git pull

# Check remote
git remote -v
```

---

## If Something Goes Wrong

### Reset to Last Commit
```bash
git reset --hard HEAD
```

### Remove Remote
```bash
git remote remove origin
```

### Add Remote Again
```bash
git remote add origin https://github.com/YOUR_USERNAME/lurantis.git
```

