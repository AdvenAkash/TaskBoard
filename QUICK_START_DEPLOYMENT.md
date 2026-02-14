# Quick Start: Deploy to Production in 10 Minutes

## Option A: Railway (Easiest - Recommended)

### Backend + Database Deployment

```bash
# 1. Install Railway CLI
npm i -g @railway/cli

# 2. Login & Create Project
railway login
cd backend
railway init

# 3. Add PostgreSQL Database
railway add            # Select "PostgreSQL"

# 4. Set Environment Variables
railway env set ENVIRONMENT=production
railway env set CLERK_SECRET_KEY=pk_live_xxxxx
railway env set CLERK_PUBLISHABLE_KEY=pk_live_xxxxx
railway env set CLERK_WEBHOOK_SECRET=whsec_xxxxx
railway env set CLERK_JWKS_URL=https://xxx.clerk.accounts.com/.well-known/jwks.json

# 5. Deploy
railway up

# 6. Get your backend URL (save this!)
railway status    # Backend URL shows here
```

### Frontend Deployment

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Deploy
cd frontend
vercel --prod

# 3. During setup, add environment variable:
# VITE_CLERK_PUBLISHABLE_KEY = your_key_from_step_4

# 4. After deployment, update backend:
railway env set FRONTEND_URL=https://your-vercel-domain.vercel.app
```

---

## Option B: Render + Vercel

### Backend Deployment to Render

1. Go to [https://render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Select your GitHub repo
4. Fill in:
   - **Name:** `task-board-api`
   - **Build Command:** `pip install -e .`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free tier

5. Click "Create Database" → PostgreSQL → Free tier
6. Add Environment Variables:
   ```
   ENVIRONMENT=production
   CLERK_SECRET_KEY=pk_live_xxxxx
   CLERK_PUBLISHABLE_KEY=pk_live_xxxxx
   CLERK_WEBHOOK_SECRET=whsec_xxxxx
   CLERK_JWKS_URL=https://xxx.clerk.accounts.com/.well-known/jwks.json
   FRONTEND_URL=https://your-vercel-domain.vercel.app
   ```
7. Click "Deploy"

### Frontend Deployment to Vercel

1. Go to [https://vercel.com](https://vercel.com)
2. Click "Add New +" → "Project"
3. Import your GitHub repo
4. Set Root Directory: `frontend`
5. Add Environment Variable:
   ```
   VITE_CLERK_PUBLISHABLE_KEY=pk_live_xxxxx
   ```
6. Click "Deploy"

---

## Option C: Heroku (Legacy - Not Recommended)

```bash
# 1. Install Heroku CLI & login
heroku login

# 2. Create app
heroku create your-app-name

# 3. Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 4. Deploy
cd backend
git push heroku main

# 5. Set environment variables
heroku config:set ENVIRONMENT=production
heroku config:set CLERK_SECRET_KEY=pk_live_xxxxx
heroku config:set FRONTEND_URL=https://your-frontend-url.com
```

---

## Getting Your Secrets from Clerk

1. Go to [https://dashboard.clerk.com](https://dashboard.clerk.com)
2. Click your application
3. Go to **API Keys**:
   - Copy `Publishable Key` → `CLERK_PUBLISHABLE_KEY`
   - Copy `Secret Key` → `CLERK_SECRET_KEY`

4. Go to **Webhooks** → Create webhook pointing to:
   - **Endpoint URL:** `https://your-api.com/api/webhooks/clerk`
   - Select events: `user.created`, `user.updated`, `user.deleted`
   - Copy `Signing Secret` → `CLERK_WEBHOOK_SECRET`

5. Go to **JWKS Endpoint** - copy the URL → `CLERK_JWKS_URL`

---

## Custom Domain Setup

### Using Vercel (Frontend)

1. In Vercel dashboard → Settings → Domains
2. Add your domain (e.g., `yourdomain.com`)
3. Update nameservers at your registrar to Vercel's
4. Update `FRONTEND_URL` in backend to `https://yourdomain.com`

### Using Render (Backend API)

1. In Render dashboard → Web Service → Settings → Custom Domains
2. Add `api.yourdomain.com` or similar
3. Follow their DNS setup instructions

---

## Testing Production

```bash
# Test backend
curl https://your-api-url.com/docs

# Test frontend
Open https://your-vercel-domain.vercel.app in browser

# Test webhook
# Go to Clerk dashboard → Webhooks → Test endpoint
```

---

## GitHub Secrets Setup (For CI/CD)

Go to **GitHub repo → Settings → Secrets and Variables → Actions**

Add these secrets:

**For Render:**
```
RENDER_SERVICE_ID=srv_xxxxx
RENDER_API_KEY=rnd_xxxxx
```

**For Railway:**
```
RAILWAY_TOKEN=your_token
```

**For Vercel:**
```
VERCEL_TOKEN=your_token
VERCEL_ORG_ID=your_org_id
VERCEL_PROJECT_ID=your_project_id
```

---

## Monitor & Debug

### Railway
```bash
railway logs              # View live logs
railway status           # Check status
railway down            # Stop service
```

### Render
- Logs available in dashboard
- Real-time streaming

### Vercel
- Analytics & logs in dashboard
- Performance metrics included

---

## Cost Breakdown

| Item | Free | Notes |
|------|------|-------|
| **Railway** | $5/month credit | Covers small app |
| **Vercel** | ✅ Unlimited | Frontend hosting free |
| **Supabase** | ✅ 500MB | Postgres database |
| **Clerk** | ✅ 10k users | Auth service |
| **Total** | **$0-5/month** | Easily scales to paid |

---

## Next Steps

1. ✅ Choose deployment platform above
2. ✅ Get Clerk secrets
3. ✅ Deploy backend
4. ✅ Deploy frontend
5. ✅ Set up custom domain (optional)
6. ✅ Configure webhooks in Clerk
7. ✅ Test all features
8. ✅ Set up monitoring

---

## Support Links

- **Clerk Docs:** https://clerk.com/docs
- **Railway Docs:** https://docs.railway.app
- **Render Docs:** https://render.com/docs
- **Vercel Docs:** https://vercel.com/docs
- **FastAPI Deployment:** https://fastapi.tiangolo.com/deployment/
