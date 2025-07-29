#!/usr/bin/env python3
"""
Simple USD functionality test
"""
def test_usd():
    try:
        print("🔧 Testing USD Import...")
        from pxr import Usd, UsdGeom, Sdf
        print("✅ USD modules imported successfully")
        
        print("🔧 Testing USD Stage Creation...")
        stage = Usd.Stage.CreateInMemory()
        print("✅ USD Stage created")
        
        print("🔧 Testing USD Geometry...")
        mesh = UsdGeom.Mesh.Define(stage, '/TestMesh')
        print("✅ USD Geometry created")
        
        print("🎯 USD is fully functional!")
        return True
        
    except ImportError as e:
        print(f"❌ USD import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ USD functionality failed: {e}")
        return False

if __name__ == "__main__":
    success = test_usd()
    if success:
        print("\n✨ Ready to create 3D geometry!")
    else:
        print("\n⚠️  Fix USD installation before proceeding")
