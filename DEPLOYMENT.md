# Deployment Guide for Mufasa AI

This guide covers various deployment options for Mufasa AI.

## Quick Start

### Local Development
```bash
# 1. Set your API key
export SARVAM_API_KEY="your_api_key_here"

# 2. Run the application
python run.py
# OR
streamlit run app.py --server.port 5000
```

## Environment Setup

### Required Environment Variables
- `SARVAM_API_KEY`: Your Sarvam AI API key (required)

### Optional Environment Variables
- `PORT`: Custom port (default: 5000)
- `DEBUG`: Enable debug mode (default: false)

## Deployment Options

### 1. Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Add secrets: `SARVAM_API_KEY`
   - Deploy!

3. **Configuration**
   - App URL: `your-app-name.streamlit.app`
   - Automatic SSL certificate
   - Free hosting for public repositories

### 2. Docker Deployment

#### Build and Run
```bash
# Build the image
docker build -t mufasa-ai .

# Run the container
docker run -p 5000:5000 -e SARVAM_API_KEY="your_key" mufasa-ai
```

#### Using Docker Compose
```bash
# Copy environment file
cp .env.example .env
# Edit .env with your API key

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### 3. Heroku Deployment

1. **Create Heroku App**
   ```bash
   heroku create mufasa-ai-app
   ```

2. **Add Procfile**
   ```
   web: streamlit run app.py --server.port $PORT --server.headless true
   ```

3. **Set Environment Variables**
   ```bash
   heroku config:set SARVAM_API_KEY="your_key"
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### 4. AWS Deployment

#### Using AWS App Runner
1. **Create apprunner.yaml**
   ```yaml
   version: 1.0
   runtime: python3
   build:
     commands:
       build:
         - pip install -r requirements.txt
   run:
     runtime-version: 3.9
     command: streamlit run app.py --server.port 8080
     network:
       port: 8080
       env: PORT
   ```

2. **Deploy via AWS Console**
   - Create App Runner service
   - Connect to your repository
   - Add environment variables
   - Deploy

#### Using ECS Fargate
1. **Push to ECR**
   ```bash
   aws ecr create-repository --repository-name mufasa-ai
   docker tag mufasa-ai:latest your-account.dkr.ecr.region.amazonaws.com/mufasa-ai:latest
   docker push your-account.dkr.ecr.region.amazonaws.com/mufasa-ai:latest
   ```

2. **Create ECS Task Definition**
3. **Create ECS Service**
4. **Configure Load Balancer**

### 5. Google Cloud Platform

#### Using Cloud Run
```bash
# Build and deploy
gcloud run deploy mufasa-ai \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars SARVAM_API_KEY="your_key"
```

#### Using App Engine
1. **Create app.yaml**
   ```yaml
   runtime: python39
   
   env_variables:
     SARVAM_API_KEY: "your_key"
   
   entrypoint: streamlit run app.py --server.port $PORT --server.headless true
   ```

2. **Deploy**
   ```bash
   gcloud app deploy
   ```

### 6. DigitalOcean App Platform

1. **Create .do/app.yaml**
   ```yaml
   name: mufasa-ai
   services:
   - name: web
     source_dir: /
     github:
       repo: your-username/mufasa-ai
       branch: main
     run_command: streamlit run app.py --server.port $PORT
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: SARVAM_API_KEY
       value: your_key_here
   ```

2. **Deploy via CLI or Console**

## Performance Optimization

### Caching
- Streamlit caching is already implemented
- API client and language support are cached
- Consider Redis for production scaling

### Resource Limits
```python
# app.py - Add resource monitoring
import psutil

@st.cache_data
def get_system_stats():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }
```

### Environment-Specific Configuration
```python
# config.py
import os

class Config:
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    SARVAM_API_KEY = os.getenv('SARVAM_API_KEY')
    PORT = int(os.getenv('PORT', 5000))
    
    # Production optimizations
    CACHE_TTL = int(os.getenv('CACHE_TTL', 3600))
    MAX_REQUESTS = int(os.getenv('MAX_REQUESTS', 100))
```

## Monitoring and Logging

### Basic Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Health Checks
```python
# health.py
@st.cache_data(ttl=60)
def health_check():
    """Simple health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }
```

## Security Considerations

### API Key Security
- Never commit API keys to version control
- Use environment variables or secret management
- Rotate keys regularly

### HTTPS
- Always use HTTPS in production
- Most cloud providers offer automatic SSL

### Input Validation
```python
def validate_input(text):
    """Validate user input"""
    if len(text) > 1000:
        raise ValueError("Input too long")
    
    # Add more validation as needed
    return text.strip()
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find and kill process
   lsof -ti:5000 | xargs kill -9
   ```

2. **Memory Issues**
   - Increase container memory limits
   - Implement session cleanup
   - Monitor memory usage

3. **API Rate Limits**
   - Implement request queuing
   - Add exponential backoff
   - Cache responses when possible

4. **Unicode Issues**
   - Ensure UTF-8 encoding
   - Set LANG environment variable
   - Use proper fonts for Indian scripts

### Debug Mode
```bash
# Enable debug logging
export DEBUG=true
streamlit run app.py --logger.level debug
```

## Scaling

### Horizontal Scaling
- Use load balancers
- Implement session affinity if needed
- Consider using Redis for shared state

### Vertical Scaling
- Monitor CPU and memory usage
- Increase container resources as needed
- Optimize heavy operations

### Database Integration (Future)
```python
# For future chat history persistence
import sqlite3

def save_chat_history(user_id, messages):
    """Save chat history to database"""
    pass

def load_chat_history(user_id):
    """Load chat history from database"""
    pass
```

## Cost Optimization

### API Usage
- Monitor Sarvam AI API usage
- Implement request caching
- Set usage limits per user

### Infrastructure
- Use appropriate instance sizes
- Implement auto-scaling
- Monitor costs regularly

---

For additional help, consult the specific platform documentation or create an issue in the repository.