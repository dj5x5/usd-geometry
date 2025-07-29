#!/usr/bin/env python3
"""
Comprehensive USD installation detector
"""
import os
import sys
from pathlib import Path

def check_pip_usd():
    """Check pip-installed USD"""
    print("🔍 PIP-INSTALLED USD")
    print("=" * 50)
    
    try:
        import pxr
        pip_location = Path(pxr.__file__).parent
        print(f"✅ Pip USD location: {pip_location}")
        
        # Check what modules are available
        pxr_modules = [item for item in dir(pxr) if not item.startswith('_')]
        print(f"✅ Available modules: {len(pxr_modules)} ({', '.join(pxr_modules[:5])}...)")
        
        # Try to get version info
        try:
            from pxr import Tf
            print("✅ Core functionality available")
        except:
            print("⚠️  Some core modules may be missing")
            
        return str(pip_location)
    except ImportError:
        print("❌ No pip USD installation found")
        return None

def check_source_build():
    """Check source-built USD"""
    print("\n🏗️  SOURCE-BUILT USD")
    print("=" * 50)
    
    usd_root = os.environ.get('USD_INSTALL_ROOT', os.path.expanduser('~/usd_install'))
    usd_path = Path(usd_root)
    
    print(f"Checking: {usd_path}")
    
    if not usd_path.exists():
        print("❌ USD install directory doesn't exist")
        return None
    
    # Check directory structure
    lib_dir = usd_path / "lib"
    python_dir = lib_dir / "python"
    bin_dir = usd_path / "bin"
    
    print(f"📁 Install directory: {'✅' if usd_path.exists() else '❌'} {usd_path}")
    print(f"📁 Lib directory: {'✅' if lib_dir.exists() else '❌'} {lib_dir}")
    print(f"📁 Python directory: {'✅' if python_dir.exists() else '❌'} {python_dir}")
    print(f"📁 Bin directory: {'✅' if bin_dir.exists() else '❌'} {bin_dir}")
    
    # Check for pxr modules
    pxr_dir = python_dir / "pxr"
    if pxr_dir.exists():
        pxr_modules = list(pxr_dir.glob("*"))
        print(f"✅ PXR modules found: {len(pxr_modules)}")
        print(f"   Sample modules: {[m.name for m in pxr_modules[:5]]}")
    else:
        print("❌ No PXR modules found in source build")
    
    # Check for executables
    if bin_dir.exists():
        executables = list(bin_dir.glob("usd*"))
        print(f"🔧 USD executables: {len(executables)}")
        if executables:
            print(f"   Found: {[e.name for e in executables[:3]]}")
    
    return str(usd_path) if python_dir.exists() else None

def test_import_priority():
    """Test which USD gets imported with different PYTHONPATH settings"""
    print("\n🎯 IMPORT PRIORITY TEST")
    print("=" * 50)
    
    current_pythonpath = os.environ.get('PYTHONPATH', '')
    print(f"Current PYTHONPATH: {current_pythonpath}")
    
    # Test current import
    try:
        import pxr
        current_location = pxr.__file__
        print(f"Current USD import: {current_location}")
    except ImportError:
        print("❌ Cannot import USD")
        return
    
    # Test what happens if we add source build to path
    usd_root = os.environ.get('USD_INSTALL_ROOT', os.path.expanduser('~/usd_install'))
    source_python_path = f"{usd_root}/lib/python"
    
    if Path(source_python_path).exists():
        print(f"\n🔄 Testing with source build in PYTHONPATH...")
        # Note: We can't actually modify sys.path and reimport in the same session
        # But we can check if the path exists
        print(f"Source build Python path exists: {Path(source_python_path).exists()}")
        
        # Check what would be imported
        potential_pxr = Path(source_python_path) / "pxr" / "__init__.py"
        print(f"Source build pxr module: {'✅' if potential_pxr.exists() else '❌'} {potential_pxr}")

def main():
    """Run comprehensive USD detection"""
    print("🔎 USD INSTALLATION DETECTIVE")
    print("=" * 70)
    
    pip_location = check_pip_usd()
    source_location = check_source_build()
    test_import_priority()
    
    print(f"\n📊 SUMMARY")
    print("=" * 50)
    
    if pip_location and source_location:
        print("🎯 You have BOTH installations:")
        print(f"   Pip USD: {pip_location}")
        print(f"   Source USD: {source_location}")
        print("   Currently using: Pip installation")
        print("   To use source build: Add to PYTHONPATH first")
    elif pip_location:
        print("🎯 You have PIP installation only:")
        print(f"   Location: {pip_location}")
        print("   Status: Working and active")
    elif source_location:
        print("🎯 You have SOURCE installation only:")
        print(f"   Location: {source_location}")
        print("   Note: Ensure PYTHONPATH is set correctly")
    else:
        print("❌ No USD installations detected")

if __name__ == "__main__":
    main()
