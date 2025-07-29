#!/usr/bin/env python3
"""
Test USD installation after building from source
"""
import os
import sys
from pathlib import Path

def test_usd_environment():
    """Test USD environment and installation"""
    print("🔧 USD BUILD TEST")
    print("=" * 50)
    
    # Check environment variables
    usd_root = os.environ.get('USD_INSTALL_ROOT')
    if usd_root:
        print(f"✅ USD_INSTALL_ROOT: {usd_root}")
        
        # Check if USD was built
        usd_lib = Path(usd_root) / "lib" / "python"
        if usd_lib.exists():
            print(f"✅ USD Python libraries found: {usd_lib}")
        else:
            print(f"❌ USD Python libraries missing: {usd_lib}")
    else:
        print("❌ USD_INSTALL_ROOT not set")
    
    # Test USD import
    try:
        from pxr import Usd, UsdGeom, Sdf, Tf
        print("✅ USD Core: All modules imported successfully")
        
        # Test version info
        print(f"✅ USD Version info available")
        
        # Test basic functionality
        stage = Usd.Stage.CreateInMemory()
        mesh = UsdGeom.Mesh.Define(stage, '/TestMesh')
        print("✅ USD Stage and Mesh: Creation successful")
        
        # Test file creation
        test_file = Path.cwd() / "test_output.usda"
        stage = Usd.Stage.CreateNew(str(test_file))
        stage.GetRootLayer().Save()
        
        if test_file.exists():
            print(f"✅ USD File creation: {test_file}")
            test_file.unlink()  # Clean up
        
        print("\n🎯 SUCCESS: USD is fully functional!")
        return True
        
    except ImportError as e:
        print(f"❌ USD import failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Source setup_usd_env.sh")
        print("2. Check PYTHONPATH includes USD libraries")
        print("3. Verify USD build completed successfully")
        return False
    except Exception as e:
        print(f"❌ USD functionality test failed: {e}")
        return False

if __name__ == "__main__":
    test_usd_environment()
