#!/usr/bin/env python3
"""
Fixed system check that properly detects USD installation
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

def check_usd_packages():
    """Check for USD packages more comprehensively"""
    usd_packages = ['usd-core', 'usd-python', 'OpenUSD']
    
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    installed_packages = result.stdout.lower()
    
    found_packages = []
    for pkg in usd_packages:
        if pkg.lower() in installed_packages:
            # Get version
            version_result = subprocess.run(['pip', 'show', pkg], 
                                          capture_output=True, text=True)
            if version_result.returncode == 0:
                for line in version_result.stdout.split('\n'):
                    if line.startswith('Version:'):
                        version = line.split('Version:')[1].strip()
                        found_packages.append(f"{pkg}: {version}")
                        break
            else:
                found_packages.append(f"{pkg}: installed")
    
    return found_packages

def check_system():
    """Generate comprehensive system report"""
    print("🖥️  SYSTEM INFORMATION")
    print("=" * 50)
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    print(f"\n📁 ENVIRONMENT")
    print("=" * 50)
    venv_path = Path(sys.executable).parent.parent
    print(f"Virtual env: {venv_path}")
    print(f"Working directory: {Path.cwd()}")
    
    print(f"\n📦 USD PACKAGES")
    print("=" * 50)
    usd_packages = check_usd_packages()
    if usd_packages:
        for pkg in usd_packages:
            print(f"✅ {pkg}")
    else:
        print("⚠️  No explicit USD packages found, but USD may be installed via dependencies")
    
    print(f"\n🎯 USD FUNCTIONALITY")
    print("=" * 50)
    try:
        from pxr import Usd, UsdGeom, Sdf
        print("✅ USD Core modules: Successfully imported")
        
        # Test basic functionality
        stage = Usd.Stage.CreateInMemory()
        print("✅ USD Stage creation: Working")
        
        mesh = UsdGeom.Mesh.Define(stage, '/TestMesh')
        print("✅ USD Geometry creation: Working")
        
        # Test file creation
        test_file = Path("temp_test.usda")
        stage2 = Usd.Stage.CreateNew(str(test_file))
        stage2.GetRootLayer().Save()
        if test_file.exists():
            print("✅ USD File creation: Working")
            test_file.unlink()  # Clean up
        
    except Exception as e:
        print(f"❌ USD functionality: {e}")

if __name__ == "__main__":
    check_system()
