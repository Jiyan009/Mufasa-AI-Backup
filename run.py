#!/usr/bin/env python3
"""
Simple runner script for Mufasa AI
This script provides an easy way to start the application
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import requests
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install dependencies:")
        print("pip install streamlit requests")
        sys.exit(1)

def check_api_key():
    """Check if API key is set"""
    api_key = os.getenv("SARVAM_API_KEY")
    if not api_key or api_key == "default_api_key":
        print("⚠️  Warning: SARVAM_API_KEY not found!")
        print("Please set your Sarvam AI API key:")
        print("export SARVAM_API_KEY='your_api_key_here'")
        print("\nOr create a .env file with:")
        print("SARVAM_API_KEY=your_api_key_here")
        print("\nThe app will start anyway but may not work properly without a valid API key.")
        input("Press Enter to continue anyway...")

def main():
    """Main function to run the application"""
    print("🦁 Starting Mufasa AI...")
    print("=" * 50)
    
    # Check dependencies
    check_dependencies()
    
    # Check API key
    check_api_key()
    
    # Start the application
    try:
        print("🚀 Launching Streamlit application...")
        print("📱 Application will be available at: http://localhost:5000")
        print("🛑 Press Ctrl+C to stop the application")
        print("=" * 50)
        
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "5000",
            "--server.headless", "true"
        ])
    except KeyboardInterrupt:
        print("\n👋 Mufasa AI stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()