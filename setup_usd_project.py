#!/usr/bin/env python3
"""
Set up USD 3D geometry project with working environment
"""
import os
import subprocess
from pathlib import Path

def setup_environment():
    """Set up clean USD development environment"""
    
    # Install required packages in order
    packages = [
        "jinja2",           # Required by USD
        "usd-core",         # USD Python API
        "numpy<2.0",        # Compatible NumPy version
        "matplotlib",       # For visualization
        "jupyter",          # For notebooks
    ]
    
    print("Installing USD development packages...")
    for package in packages:
        print(f"Installing {package}...")
        subprocess.run(["pip", "install", package, "--upgrade"], check=True)
    
    # Test USD import
    try:
        from pxr import Usd, UsdGeom, Sdf
        print("✅ USD Core: Successfully imported")
        
        # Test basic functionality
        stage = Usd.Stage.CreateInMemory()
        mesh = UsdGeom.Mesh.Define(stage, '/TestMesh')
        print("✅ USD functionality: Working")
        
        return True
    except Exception as e:
        print(f"❌ USD test failed: {e}")
        return False

if __name__ == "__main__":
    setup_environment()
