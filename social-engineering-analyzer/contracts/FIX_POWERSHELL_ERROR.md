# Fix PowerShell Script Execution Error

## The Problem
PowerShell is blocking npm from running because scripts are disabled by default on Windows.

## Quick Fix (3 Options)

### Option 1: Bypass for Current Terminal Session (Easiest)
Run this command in your PowerShell terminal:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Then try `npm install` again. This only works for this terminal session.

---

### Option 2: Change Execution Policy Permanently (Recommended)

**Run PowerShell as Administrator:**

1. **Press Windows key + X**
2. Click **"Windows PowerShell (Admin)"** or **"Terminal (Admin)"**
3. Click **"Yes"** when Windows asks for permission

**Then run this command:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**When it asks:** Type `Y` and press Enter

**Now close that admin terminal** and go back to Cursor terminal. Try `npm install` again.

---

### Option 3: Use Command Prompt Instead (Alternative)

If you prefer not to change PowerShell settings:

1. **In Cursor:** Terminal → New Terminal
2. **Change terminal type:** Click the dropdown next to "+" in terminal → Select "Command Prompt"
3. **Navigate to contracts folder:**
   ```
   cd C:\Users\valoo\Documents\social-engineering-analyzer\contracts
   ```
4. **Run:**
   ```
   npm install
   ```

Command Prompt doesn't have this restriction, so it will work.

---

## Recommended Solution

**For this project, I recommend Option 1 (quick bypass):**

Just run this in your current terminal:
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Then continue with:
```bash
npm install
```

This only affects this terminal window, so it's safe and won't change your system settings.

---

## After Fixing

Once you've fixed it, continue with deployment:

```bash
npm install
# Wait for it to finish...

# Then create .env file (as explained in DEPLOY_MAINNET.md)
# Then:
npm run deploy:mainnet
```

