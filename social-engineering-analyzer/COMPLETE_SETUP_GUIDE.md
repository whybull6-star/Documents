# 🚀 Complete Setup Guide - From Zero to Running

## Step 1: Open Terminal/Command Prompt

### Windows:
1. Press `Win + R` (Windows key + R)
2. Type: `cmd` or `powershell`
3. Press Enter

**OR**

1. Press `Win + X`
2. Click "Windows PowerShell" or "Command Prompt"

---

## Step 2: Navigate to Your Backend Folder

**Copy and paste this command:**

```bash
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend
```

**Press Enter**

You should see your prompt change to show the backend folder path.

---

## Step 3: Check if Virtual Environment Exists

**Check if `venv` folder exists:**

```bash
dir
```

**Look for a folder named `venv`**

- ✅ **If you see `venv` folder** → Skip to Step 5 (Activate)
- ❌ **If you DON'T see `venv` folder** → Continue to Step 4 (Create it)

---

## Step 4: Create Virtual Environment (If Needed)

**Only do this if you don't have a `venv` folder!**

```bash
python -m venv venv
```

**Press Enter and wait** (takes a few seconds)

You should see the command complete without errors.

**Verify it was created:**

```bash
dir
```

You should now see a `venv` folder in the list.

---

## Step 5: Activate Virtual Environment

**This is the IMPORTANT step!**

```bash
venv\Scripts\activate
```

**Press Enter**

### ✅ Success Looks Like This:

Your command prompt should now show:
```
(venv) C:\Users\valoo\Documents\social-engineering-analyzer\backend>
```

**Notice the `(venv)` at the beginning!** This means it's activated.

### ❌ If It Doesn't Work:

**Try this instead:**
```bash
.\venv\Scripts\activate
```

**Or:**
```bash
venv\Scripts\activate.bat
```

---

## Step 6: Verify Virtual Environment is Active

**Check that `(venv)` appears in your prompt**

If you see `(venv)` at the start of your command line, you're good! ✅

**Test it:**
```bash
python --version
```

This should show your Python version.

---

## Step 7: Install Dependencies (If Not Already Done)

**Only if you haven't installed packages yet:**

```bash
pip install -r requirements.txt
```

**Press Enter and wait** (this takes several minutes - downloads ~500MB)

You'll see lots of "Downloading..." messages. This is normal!

---

## Step 8: Verify Everything is Ready

**Check if packages are installed:**

```bash
python -c "import qdrant_client; print('Qdrant installed!')"
```

Should print: `Qdrant installed!`

---

## ✅ You're Ready!

Now you can run:

```bash
# Seed the database
python scripts/seed_enhanced_patterns.py

# Start the server
python app_enhanced.py
```

---

## 🔄 Every Time You Open a New Terminal

**You need to activate venv again!**

1. Open terminal
2. Navigate: `cd C:\Users\valoo\Documents\social-engineering-analyzer\backend`
3. Activate: `venv\Scripts\activate`
4. You should see `(venv)` in your prompt
5. Now you can run Python commands

---

## 🐛 Troubleshooting

### "venv\Scripts\activate : The term 'activate' is not recognized"

**Solution:** You're in PowerShell, use:
```powershell
.\venv\Scripts\Activate.ps1
```

**If that gives an error about execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

### "python: command not found"

**Solution:** Python might not be in your PATH. Try:
```bash
py -m venv venv
py scripts/seed_enhanced_patterns.py
```

### "(venv)" doesn't appear after activation

**Solution:** 
- Make sure you're in the `backend` folder
- Make sure `venv` folder exists
- Try: `.\venv\Scripts\activate.bat`

---

## 📝 Quick Reference Card

**Copy-paste these commands in order:**

```bash
# 1. Navigate to backend
cd C:\Users\valoo\Documents\social-engineering-analyzer\backend

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Verify it's active (you should see (venv) in prompt)
# If you see (venv), you're good!

# 4. Now you can run commands:
python scripts/seed_enhanced_patterns.py
python app_enhanced.py
```

---

## 💡 Pro Tips

1. **Always activate venv first** before running Python scripts
2. **Keep terminal open** - closing it deactivates venv
3. **Look for `(venv)`** - this confirms it's active
4. **Each new terminal** needs activation again

---

**Need help?** Check which step you're on and let me know what error you see!

