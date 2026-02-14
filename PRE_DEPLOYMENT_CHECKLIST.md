# Pre-Deployment Checklist

## Code Quality

- [ ] Run tests locally: `pytest` (backend)
- [ ] Run linter: `npm run lint` (frontend)
- [ ] No console errors/warnings
- [ ] All TODO comments resolved
- [ ] Removed console.log statements
- [ ] No hardcoded API URLs - using environment variables

## Backend (.env)

**Clerk Configuration:**
- [ ] `CLERK_SECRET_KEY` - From Clerk Dashboard → API Keys
- [ ] `CLERK_PUBLISHABLE_KEY` - From Clerk Dashboard → API Keys
- [ ] `CLERK_WEBHOOK_SECRET` - From Clerk Dashboard → Webhooks
- [ ] `CLERK_JWKS_URL` - From Clerk Dashboard → API Keys

**Database:**
- [ ] `DATABASE_URL` - PostgreSQL connection string
- [ ] Database created and accessible
- [ ] Migrations run successfully
- [ ] Database backed up (if migrating from dev)

**URLs:**
- [ ] `FRONTEND_URL` - Set to your production frontend domain
- [ ] CORS properly configured in FastAPI

**Environment:**
- [ ] `ENVIRONMENT=production` not set locally (for testing)
- [ ] All secrets use production keys from Clerk

## Frontend

- [ ] `VITE_CLERK_PUBLISHABLE_KEY` configured
- [ ] No hardcoded backend API URLs
- [ ] Build produces no errors: `npm run build`
- [ ] Build output in correct directory: `dist/`
- [ ] Environment variables use correct format: `VITE_*`

## Deployment Infrastructure

**Choose one platform:**
- [ ] Railway (recommended - easiest)
- [ ] Render
- [ ] Vercel (frontend only)
- [ ] Other: _________

**Database:**
- [ ] PostgreSQL instance created
- [ ] Connection string obtained
- [ ] Backups configured
- [ ] Security groups configured (only allow your app)

**Domains:**
- [ ] Domain purchased (optional)
- [ ] DNS configured (if using custom domain)
- [ ] SSL certificate setup (automatic on most platforms)

## Clerk Configuration

- [ ] Application created in Clerk
- [ ] API Keys copied to production environment
- [ ] Webhook created:
  - [ ] URL: `https://your-api.com/api/webhooks/clerk`
  - [ ] Events selected: `user.created`, `user.updated`, `user.deleted`
  - [ ] Signing secret copied to `CLERK_WEBHOOK_SECRET`
- [ ] Production instance used (not test instance)

## GitHub Setup

- [ ] Code pushed to GitHub
- [ ] `.github/workflows/` files created and committed
- [ ] GitHub Secrets configured (if using CI/CD):
  - [ ] `RENDER_API_KEY` or `RAILWAY_TOKEN` (backend)
  - [ ] `VERCEL_TOKEN` (frontend)
  - [ ] Optional: `SLACK_WEBHOOK` (for notifications)

## Testing Pre-Production

- [ ] Test backend locally with production environment variables
- [ ] Test frontend locally with production keys
- [ ] Test database connection
- [ ] Test authentication flow with Clerk
- [ ] Test API endpoints with Postman/curl
- [ ] Test webhook delivery (Clerk dashboard → Webhooks → Test)
- [ ] Check CORS configuration works

## Security

- [ ] No secrets in source code
- [ ] `.env` files in `.gitignore`
- [ ] API keys are production (not test keys)
- [ ] Database requires password/authentication
- [ ] HTTPS enabled (automatic)
- [ ] CORS whitelist restricted to your domain
- [ ] Rate limiting planned (if needed)
- [ ] Input validation implemented

## Monitoring & Logging

- [ ] Logging configured in production
- [ ] Error tracking setup (optional: Sentry, DataDog)
- [ ] Health check endpoint available: `/health`
- [ ] Dashboard monitoring enabled
- [ ] Alert emails configured

## Documentation

- [ ] README updated with production instructions
- [ ] Environment variables documented
- [ ] API endpoints documented
- [ ] Database schema documented
- [ ] Deployment instructions documented

## Post-Deployment Steps

- [ ] Access production URL in browser
- [ ] Test user signup/login flow
- [ ] Test creating/updating tasks
- [ ] Test Clerk webhooks triggered correctly
- [ ] Check backend logs for errors
- [ ] Verify database has user data
- [ ] Test on mobile devices
- [ ] Check performance with Lighthouse
- [ ] Monitor errors for first week

## Rollback Plan

- [ ] Know how to rollback deployed version
- [ ] Database backup created
- [ ] Previous version tags available in GitHub
- [ ] Downtime communication plan

## Cost Optimization

- [ ] Chose appropriate tier (free tier for starting)
- [ ] Database backup strategy planned
- [ ] Auto-scaling limits set (if applicable)
- [ ] Estimated monthly cost calculated

## Maintenance Plan

- [ ] Update dependencies schedule: ________
- [ ] SSL certificate renewal: automatic
- [ ] Database maintenance: ________
- [ ] Performance review: ________
- [ ] Security updates: ________

---

## Deployment Checklist

When you're ready to deploy:

1. **Today - 1 Hour Before:**
   - [ ] Final backup of database (if existing)
   - [ ] Test everything locally one more time
   - [ ] Notify team deployment is happening

2. **Deployment:**
   - [ ] Push code to GitHub
   - [ ] Deploy backend to chosen platform
   - [ ] Deploy frontend to chosen platform
   - [ ] Configure custom domains (if applicable)

3. **After Deployment:**
   - [ ] Test all features in production
   - [ ] Monitor logs for 30 minutes
   - [ ] Test critical user flows
   - [ ] Verify webhooks working
   - [ ] Notify team deployment successful

4. **Next 24 Hours:**
   - [ ] Monitor for errors
   - [ ] Check performance metrics
   - [ ] Respond to user feedback
   - [ ] Be ready to rollback if needed

---

## Help & Troubleshooting

**Backend won't start:**
- Check environment variables are set correctly
- Check PostgreSQL connection string
- Check database is accessible
- Review application logs

**Frontend blank page:**
- Check browser console for errors
- Verify Clerk key is correct
- Check API endpoint configuration
- Review network tab for failed requests

**Communication issues between frontend and backend:**
- Check CORS is allowing your frontend domain
- Verify `FRONTEND_URL` matches actual domain
- Check API endpoint is correct in frontend

**Clerk authentication not working:**
- Verify webhook is receiving events
- Check webhook secret matches configuration
- Verify user events are in Clerk dashboard
- Check JWT tokens are valid

**Database connection error:**
- Verify DATABASE_URL format
- Confirm database server is running
- Check network/firewall allows connection
- Verify username/password correct

---

**Deployment Date:** ______________
**Deployed By:** ______________
**Backend URL:** ______________
**Frontend URL:** ______________
**Notes:** ______________________________________________________________________
