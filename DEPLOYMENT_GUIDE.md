# Production Deployment Guide

## Quick Start - Railway (Recommended)

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Create new project from GitHub repo
4. Railway auto-detects and deploys backend
5. Add Postgres database from Railway dashboard
6. Set environment variables in Railway
7. Deploy frontend separately to Vercel

## Step-by-Step Deployment

### Backend Deployment

#### Using Railway (Easiest)
```bash
# 1. Install Railway CLI
npm i -g @railway/cli

# 2. Login
railway login

# 3. Initialize project in backend folder
cd backend
railway init

# 4. Set environment variables
railway env set CLERK_SECRET_KEY=xxx
railway env set DATABASE_URL=xxx
railway env set FRONTEND_URL=https://yourdomain.com

# 5. Deploy
railway up
```

#### Using Render (Alternative)
1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect GitHub repo
4. Build command: `pip install -e .`
5. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add PostgreSQL database
7. Set environment variables
8. Deploy

#### Using Heroku (Legacy)
```bash
# Install Heroku CLI
heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set CLERK_SECRET_KEY=xxx

# Deploy
git push heroku main
```

### Frontend Deployment

#### Using Vercel (Quickest)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd frontend
vercel

# Follow prompts, set VITE_CLERK_PUBLISHABLE_KEY during setup
```

Or via GitHub:
1. Push to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import project from GitHub
4. Set environment variable `VITE_CLERK_PUBLISHABLE_KEY`
5. Deploy

#### Using Netlify (Alternative)
1. Go to [netlify.com](https://netlify.com)
2. Connect GitHub
3. Build command: `npm run build`
4. Publish directory: `dist`
5. Set `VITE_CLERK_PUBLISHABLE_KEY` in environment
6. Deploy

### Database Setup

#### Using Supabase (Recommended)
```bash
# 1. Create account at supabase.com
# 2. Create new project
# 3. Copy connection string
# 4. Set DATABASE_URL in backend env vars
```

#### Using Railway PostgreSQL
```bash
# 1. Add Postgres plugin from Railway dashboard
# 2. Railway auto-generates DATABASE_URL
# 3. Copy to backend environment variables
```

#### Using AWS RDS
```bash
# 1. Create RDS PostgreSQL instance
# 2. Configure security groups
# 3. Get connection string: postgresql://user:pass@host:5432/dbname
# 4. Set as DATABASE_URL
```

## Environment Variables Checklist

### Backend (.env in production)
- [ ] `CLERK_SECRET_KEY` - From Clerk Dashboard
- [ ] `CLERK_PUBLISHABLE_KEY` - From Clerk Dashboard
- [ ] `CLERK_WEBHOOK_SECRET` - From Clerk Dashboard
- [ ] `CLERK_JWKS_URL` - From Clerk Dashboard
- [ ] `DATABASE_URL` - PostgreSQL connection string
- [ ] `FRONTEND_URL` - Your frontend domain

### Frontend (.env.production)
- [ ] `VITE_CLERK_PUBLISHABLE_KEY` - Same as backend's CLERK_PUBLISHABLE_KEY

## Domain & DNS Setup

1. Purchase domain (GoDaddy, Namecheap, etc.)
2. Update nameservers to your provider:
   - **Vercel**: Follow their DNS guide
   - **Netlify**: Follow their DNS guide
   - **Railway/Render**: Add custom domain in dashboard
3. Configure backend domain (api.yourdomain.com)
4. Update `FRONTEND_URL` in backend to your frontend domain

## Security Checklist

- [ ] Enable HTTPS (automatic with Vercel/Render/Railway)
- [ ] Set secure CORS origins
- [ ] Rotate Clerk webhook secrets
- [ ] Use environment variables for all secrets
- [ ] Enable database backups
- [ ] Set up monitoring/logging
- [ ] Configure rate limiting
- [ ] Review database security groups

## Monitoring & Logging

### Railway
- Built-in logs in dashboard
- Can integrate Datadog, Sentry

### Vercel
- Analytics tab shows performance
- Real-time monitoring available

### Render
- Logs available in dashboard
- Can integrate external services

## Cost Estimation

| Service | Free Tier | Paid |
|---------|-----------|------|
| Vercel (Frontend) | ✅ Unlimited deployments | - |
| Railway (Backend) | ✅ $5/month credit | From $5/month |
| Supabase (DB) | ✅ 500MB | From $5/month |
| Clerk (Auth) | ✅ Up to 10k users | Usage-based |
| **Total** | **Free to $5** | **From $10/month** |

## Deployment Commands

```bash
# Backend deployment (Railway)
railway up

# Frontend deployment (Vercel)
vercel --prod

# Check logs
railway logs
vercel logs --prod

# Rollback if needed
railway canary --id=xxx
```

## Common Issues & Fixes

### Database Connection Error
```
SSL certificate verification error
→ Add ?sslmode=require to DATABASE_URL
```

### CORS Error
```
origin not allowed
→ Update FRONTEND_URL in backend to match frontend domain
```

### Webhook Not Receiving
```
→ Check CLERK_WEBHOOK_SECRET in Clerk dashboard
→ Verify backend is accessible from internet
→ Check logs for actual errors
```

## Post-Deployment

1. Test all features in production
2. Monitor error logs for first week
3. Set up automated backups
4. Configure alerting
5. Plan scaling strategy

## Support

- Clerk Docs: https://clerk.com/docs
- FastAPI Docs: https://fastapi.tiangolo.com
- Railway Docs: https://docs.railway.app
- Vercel Docs: https://vercel.com/docs
