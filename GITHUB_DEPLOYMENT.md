# GitHub Deployment Guide for Mufasa AI

This guide explains how to deploy Mufasa AI from the provided zip file to various platforms via GitHub.

## Quick GitHub Setup

### 1. Extract and Upload to GitHub

1. **Extract the zip file** `mufasa-ai-github-deployment.zip`
2. **Create a new GitHub repository**
   - Go to GitHub.com
   - Click "New repository"
   - Name it "mufasa-ai" or similar
   - Make it public (for free Streamlit Cloud deployment)

3. **Upload files to GitHub**
   ```bash
   # If using Git command line:
   git init
   git add .
   git commit -m "Initial commit: Mufasa AI - Wise AI Companion"
   git branch -M main
   git remote add origin https://github.com/yourusername/mufasa-ai.git
   git push -u origin main
   ```

   Or use GitHub's web interface to upload the extracted files.

## Deployment Options from GitHub

### Option 1: Streamlit Cloud (Recommended - Free)

1. **Go to [share.streamlit.io](https://share.streamlit.io)**
2. **Sign in with GitHub**
3. **Click "New app"**
4. **Select your repository**: `yourusername/mufasa-ai`
5. **Set main file path**: `app.py`
6. **Add secrets** in Advanced Settings:
   ```
   SARVAM_API_KEY = "your_actual_api_key_here"
   ```
7. **Click "Deploy"**

Your app will be available at: `https://your-app-name.streamlit.app`

### Option 2: Replit (Easy Import)

1. **Go to [replit.com](https://replit.com)**
2. **Click "Create Repl"**
3. **Choose "Import from GitHub"**
4. **Paste your repository URL**
5. **Add secret**: `SARVAM_API_KEY`
6. **Run the app**

### Option 3: Heroku

1. **Create Heroku app**
   ```bash
   heroku create your-mufasa-ai-app
   ```

2. **Add Procfile** (create this file):
   ```
   web: streamlit run app.py --server.port $PORT --server.headless true
   ```

3. **Set environment variables**
   ```bash
   heroku config:set SARVAM_API_KEY="your_key"
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### Option 4: Render

1. **Go to [render.com](https://render.com)**
2. **Create new Web Service**
3. **Connect GitHub repository**
4. **Settings**:
   - Build Command: `pip install -r dependencies.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.headless true`
5. **Add environment variable**: `SARVAM_API_KEY`
6. **Deploy**

### Option 5: Railway

1. **Go to [railway.app](https://railway.app)**
2. **Deploy from GitHub**
3. **Select repository**
4. **Add environment variable**: `SARVAM_API_KEY`
5. **Deploy automatically**

## File Structure in Zip

```
mufasa-ai-github-deployment.zip
├── app.py                    # Main Streamlit application
├── sarvam_client.py          # Sarvam AI API integration
├── language_support.py       # Multi-language features
├── tiger_mascot.py           # Interactive mascot system
├── image_tiger.py            # Tiger visual components
├── run.py                    # Local development runner
├── setup.py                  # Automated setup script
├── README.md                 # Project documentation
├── INSTALL.md                # Installation guide
├── DEPLOYMENT.md             # Comprehensive deployment guide
├── replit.md                 # Technical architecture docs
├── Dockerfile                # Container deployment
├── docker-compose.yml        # Docker orchestration
├── .env.example              # Environment template
├── .gitignore                # Git ignore patterns
├── dependencies.txt          # Python dependencies
├── packages.txt              # System packages (if needed)
└── .streamlit/
    └── config.toml           # Streamlit configuration
```

## Environment Variables Required

For all deployments, you need:

- **SARVAM_API_KEY**: Your Sarvam AI API key
  - Get from: [https://api.sarvam.ai](https://api.sarvam.ai)
  - Required for AI chat and translation features

## Platform-Specific Notes

### Streamlit Cloud
- **Pros**: Free, easy setup, automatic SSL, custom domains
- **Cons**: Public repos only for free tier
- **Best for**: Personal projects, demos, open source

### Heroku
- **Pros**: Robust platform, good for production
- **Cons**: No longer has free tier
- **Best for**: Production applications

### Render
- **Pros**: Modern platform, good free tier
- **Cons**: Newer platform
- **Best for**: Small to medium applications

### Railway
- **Pros**: Developer-friendly, good pricing
- **Cons**: Smaller platform
- **Best for**: Modern development workflows

### Replit
- **Pros**: Instant setup, collaborative editing
- **Cons**: Limited for production
- **Best for**: Development, learning, quick demos

## Testing Your Deployment

After deployment:

1. **Open your app URL**
2. **Check language selector** (11 Indian languages)
3. **Test auto-translate feature**
4. **Send a test message** to Mufasa AI
5. **Verify tiger mascot animations**

## Troubleshooting

### Common Issues

**Build Failures:**
- Check dependencies.txt format
- Verify Python version compatibility
- Check platform-specific requirements

**API Errors:**
- Verify SARVAM_API_KEY is set correctly
- Check API key validity
- Ensure internet connectivity

**Unicode Issues:**
- Most modern platforms handle Unicode well
- If issues persist, check platform documentation

**Performance:**
- Monitor resource usage
- Consider upgrading plan if needed
- Implement caching optimizations

### Support

- **Application Issues**: Check GitHub repository issues
- **Platform Issues**: Contact platform support
- **API Issues**: Contact Sarvam AI support

## Next Steps

1. **Extract the zip file**
2. **Choose your deployment platform**
3. **Follow the specific guide above**
4. **Set your SARVAM_API_KEY**
5. **Deploy and enjoy Mufasa AI!**

---

Your Mufasa AI is ready for the world! 🦁