# Frontend - Landing Page

Beautiful, modern landing page built with Next.js 14, React, and Tailwind CSS.

## Quick Start

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Create .env file:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your configuration values.

3. **Run development server:**
   ```bash
   npm run dev
   ```

4. **Open browser:**
   Navigate to `http://localhost:3000`

## Building for Production

```bash
npm run build
npm start
```

## Deployment

The frontend can be deployed to:
- **Vercel** (easiest - just connect GitHub repo)
- **AWS S3 + CloudFront** (see deploy/ folder)
- **Netlify** (also easy)

For production deployment, make sure to:
1. Set environment variables in your hosting platform
2. Update API URLs to point to production backend
3. Configure custom domain

## Project Structure

```
frontend/
├── app/              # Next.js 14 app directory
│   ├── page.tsx     # Home page
│   ├── layout.tsx   # Root layout
│   └── globals.css  # Global styles
├── components/      # React components
│   ├── Hero.tsx
│   ├── Features.tsx
│   ├── Navbar.tsx
│   └── ...
└── public/          # Static assets
```


