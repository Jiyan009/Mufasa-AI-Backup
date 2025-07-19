#!/usr/bin/env python3
"""
Setup script for Mufasa AI
Installs dependencies and prepares the application for running
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    
    packages = ["streamlit", "requests"]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False
    
    return True

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            print("📝 Creating .env file from template...")
            with open(".env.example", "r") as src, open(".env", "w") as dst:
                dst.write(src.read())
            print("✅ .env file created")
            print("⚠️  Please edit .env file and add your SARVAM_API_KEY")
        else:
            print("📝 Creating basic .env file...")
            with open(".env", "w") as f:
                f.write("# Mufasa AI Configuration\n")
                f.write("SARVAM_API_KEY=your_api_key_here\n")
            print("✅ .env file created")
            print("⚠️  Please edit .env file and add your SARVAM_API_KEY")
    else:
        print("✅ .env file already exists")

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ is required")
        print(f"Current version: {version.major}.{version.minor}")
        return False
    
    print(f"✅ Python version {version.major}.{version.minor} is compatible")
    return True

def main():
    """Main setup function"""
    print("🦁 Mufasa AI Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create environment file
    create_env_file()
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file and add your SARVAM_API_KEY")
    print("2. Run: python run.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\nEnjoy chatting with Mufasa AI! 🦁")

if __name__ == "__main__":
    main()