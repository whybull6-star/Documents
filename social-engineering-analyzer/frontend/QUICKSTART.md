# Quick Start - View Landing Page Locally

## Step-by-Step Guide (ELI5)

### 1. Open Terminal in the frontend folder

Navigate to the frontend directory:
```bash
cd social-engineering-analyzer/frontend
```

### 2. Install Dependencies

This downloads all the code libraries we need (like React, Next.js, etc.):
```bash
npm install
```

**What this does:** Downloads all the packages listed in `package.json` into a `node_modules` folder.

**Time:** Takes about 1-2 minutes

### 3. Start the Development Server

```bash
npm run dev
```

**What this does:** Starts a web server on your computer at `http://localhost:3000`

**You should see:** 
```
✓ Ready in [time]
○ Local: http://localhost:3000
```

### 4. Open in Browser

1. Open your web browser (Chrome, Firefox, Edge, etc.)
2. Go to: `http://localhost:3000`
3. You should see the landing page!

### 5. Make Changes (Optional)

- Edit any file in `components/` or `app/`
- Save the file
- The page will automatically update in your browser (hot reload)

### 6. Stop the Server

Press `Ctrl + C` in the terminal to stop the server.

---

## Troubleshooting

### "npm: command not found"
**Problem:** Node.js isn't installed  
**Solution:** Download Node.js from https://nodejs.org (get the LTS version)

### "Port 3000 already in use"
**Problem:** Something else is using port 3000  
**Solution:** 
- Stop the other app using port 3000, OR
- Run: `npm run dev -- -p 3001` (uses port 3001 instead)

### "Module not found" errors
**Problem:** Dependencies aren't installed  
**Solution:** Run `npm install` again

### TypeScript errors (if you see red underlines in Cursor)
**Problem:** TypeScript checking is working (this is normal)  
**Solution:** As long as the page loads in the browser, these are just warnings and can be ignored for now

---

## What You'll See

The landing page includes:
- **Hero Section** - Big headline with buttons
- **Features Section** - 6 feature cards
- **How It Works** - 4-step process
- **Pricing** - 3 pricing tiers
- **CTA Section** - Call-to-action
- **Footer** - Links and info

All content is placeholder text for now - we'll update it after we define the problem!

---

## Next Steps

Once you can see the page:
1. Play around with it - scroll, click buttons (they don't do anything yet)
2. Notice the design - clean, modern, smooth
3. We'll customize the content once we define our solution

