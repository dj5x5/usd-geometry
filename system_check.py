#!/usr/bin/env python3
"""
System and USD installation verification
"""
import sys
import platform
import subprocess
from pathlib import Path

def run_command(cmd):
    """Run shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except:
        return "Command failed"

def check_system():
    """Generate comprehensive system report"""
    print("🖥️  SYSTEM INFORMATION")
    print("=" * 50)
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    print(f"\n📁 ENVIRONMENT")
    print("=" * 50)
    venv_path = Path(sys.executable).parent.parent
    print(f"Virtual env: {venv_path}")
    print(f"Working directory: {Path.cwd()}")
    
    print(f"\n🏗️  BUILD TOOLS")
    print("=" * 50)
    print(f"Homebrew: {run_command('brew --version | head -1')}")
    print(f"Git: {run_command('git --version')}")
    print(f"CMake: {run_command('cmake --version | head -1')}")
    print(f"Pip: {run_command('pip --version')}")
    
    print(f"\n📦 PYTHON PACKAGES")
    print("=" * 50)
    packages = ['usd-core', 'numpy', 'matplotlib', 'PySide6', 'jupyter']
    for pkg in packages:
        try:
            __import__(pkg.replace('-', '_'))
            version = run_command(f'pip show {pkg} | grep Version')
            print(f"✅ {pkg}: {version.replace('Version: ', '')}")
        except ImportError:
            print(f"❌ {pkg}: Not installed")
    
    print(f"\n🎯 USD SPECIFIC")
    print("=" * 50)
    try:
        from pxr import Usd, UsdGeom, Sdf
        print("✅ USD Core modules: Successfully imported")
        
        # Test basic USD functionality
        stage = Usd.Stage.CreateInMemory()
        print("✅ USD Stage creation: Working")
        
        mesh = UsdGeom.Mesh.Define(stage, '/TestMesh')
        print("✅ USD Geometry creation: Working")
        
    except Exception as e:
        print(f"❌ USD functionality: {e}")

if __name__ == "__main__":
    check_system()
