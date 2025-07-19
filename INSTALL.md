# Installation Guide for Mufasa AI

## Quick Install

### Option 1: Automated Setup (Recommended)
```bash
# Run the setup script
python setup.py

# Edit your API key
nano .env

# Start the application
python run.py
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install streamlit requests

# Set your API key
export SARVAM_API_KEY="your_api_key_here"

# Run the application
streamlit run app.py --server.port 5000
```

## Requirements

- **Python 3.7+**
- **Internet connection** for API calls
- **Sarvam AI API Key** ([Get one here](https://api.sarvam.ai))

## Dependencies

The application requires these Python packages:
- `streamlit` (≥1.28.0) - Web framework
- `requests` (≥2.31.0) - HTTP library

## Environment Setup

### 1. Get Sarvam AI API Key
1. Visit [Sarvam AI](https://api.sarvam.ai)
2. Sign up and get your API key
3. Save it for the next step

### 2. Configure Environment
Create a `.env` file in the project directory:
```env
SARVAM_API_KEY=your_actual_api_key_here
```

### 3. Install Dependencies
```bash
pip install streamlit requests
```

## Running the Application

### Method 1: Using run.py (Recommended)
```bash
python run.py
```

### Method 2: Direct Streamlit
```bash
streamlit run app.py --server.port 5000
```

### Method 3: Docker
```bash
# Build and run
docker build -t mufasa-ai .
docker run -p 5000:5000 -e SARVAM_API_KEY="your_key" mufasa-ai
```

## Verification

After starting the application:
1. Open http://localhost:5000 in your browser
2. You should see the Mufasa AI interface
3. Select a language and try sending a message
4. The tiger mascot should animate and you should get a response

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Kill existing process
lsof -ti:5000 | xargs kill -9
# Or use a different port
streamlit run app.py --server.port 8501
```

**Missing dependencies:**
```bash
pip install --upgrade streamlit requests
```

**API key not working:**
- Check if the key is correctly set in .env
- Verify the key is valid at Sarvam AI dashboard
- Ensure no extra spaces or quotes in the key

**Unicode/Font issues:**
- Ensure your browser supports Unicode fonts
- Try switching to a different browser
- Check if system fonts support Indian scripts

### Debug Mode
```bash
# Run with debug information
export DEBUG=true
streamlit run app.py --logger.level debug
```

## Platform-Specific Notes

### Windows
```cmd
# Use Windows Command Prompt or PowerShell
set SARVAM_API_KEY=your_key_here
python run.py
```

### macOS/Linux
```bash
export SARVAM_API_KEY="your_key_here"
python run.py
```

### Python Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv mufasa-env

# Activate it
# On Windows:
mufasa-env\Scripts\activate
# On macOS/Linux:
source mufasa-env/bin/activate

# Install dependencies
pip install streamlit requests

# Run application
python run.py
```

## Alternative Installation Methods

### Using pip (if packaged)
```bash
pip install mufasa-ai
mufasa-ai
```

### Using conda
```bash
conda create -n mufasa python=3.9
conda activate mufasa
pip install streamlit requests
python run.py
```

### Using Poetry
```bash
poetry install
poetry run python run.py
```

## Development Setup

For developers who want to modify the code:

```bash
# Clone the repository
git clone <repository-url>
cd mufasa-ai

# Create development environment
python -m venv dev-env
source dev-env/bin/activate  # or dev-env\Scripts\activate on Windows

# Install in development mode
pip install -e .
pip install streamlit requests

# Install development dependencies (if any)
pip install pytest black flake8

# Run the application
python run.py
```

## Uninstallation

To remove Mufasa AI:

```bash
# If using virtual environment
rm -rf mufasa-env

# If installed globally
pip uninstall streamlit requests

# Remove application files
rm -rf mufasa-ai/
```

## Getting Help

- **Documentation**: Check README.md and DEPLOYMENT.md
- **Issues**: Create an issue in the repository
- **API Problems**: Contact Sarvam AI support
- **Streamlit Issues**: Check [Streamlit documentation](https://docs.streamlit.io)

---

Happy chatting with Mufasa AI! 🦁