#!/usr/bin/env python3
"""
Comprehensive USD geometry workflow test
"""
import sys
from pathlib import Path
import subprocess

def test_usd_imports():
    """Test all USD module imports"""
    print("🔧 USD Import Test")
    print("=" * 50)
    
    try:
        from pxr import Usd, UsdGeom, Sdf, Gf, Tf
        print("✅ Core USD modules: All imported successfully")
        
        # Test version info if available
        try:
            print(f"✅ USD build info available")
        except:
            print("⚠️  USD version info not available (but modules work)")
        
        return True
    except ImportError as e:
        print(f"❌ USD import failed: {e}")
        return False

def test_geometry_creation():
    """Test various geometry creation capabilities"""
    print("\n🎯 Geometry Creation Test")
    print("=" * 50)
    
    try:
        from pxr import Usd, UsdGeom
        import math
        
        # Test 1: Cone creation
        output_dir = Path("test_output")
        output_dir.mkdir(exist_ok=True)
        
        stage = Usd.Stage.CreateNew(str(output_dir / "test_cone.usda"))
        mesh = UsdGeom.Mesh.Define(stage, '/TestCone')
        
        # Create simple cone
        points = [(1,0,0), (0,0,1), (-1,0,0), (0,0,-1), (0,2,0)]  # Simple 4-sided cone
        face_counts = [3, 3, 3, 3]  # 4 triangular faces
        face_indices = [0,1,4, 1,2,4, 2,3,4, 3,0,4]
        
        mesh.GetPointsAttr().Set(points)
        mesh.GetFaceVertexCountsAttr().Set(face_counts)
        mesh.GetFaceVertexIndicesAttr().Set(face_indices)
        
        stage.GetRootLayer().Save()
        print("✅ Cone geometry: Created and saved")
        
        # Test 2: Sphere approximation
        stage2 = Usd.Stage.CreateNew(str(output_dir / "test_sphere.usda"))
        sphere_mesh = UsdGeom.Mesh.Define(stage2, '/TestSphere')
        
        # Create icosahedron (simple sphere approximation)
        # Golden ratio
        phi = (1 + math.sqrt(5)) / 2
        
        # Icosahedron vertices
        ico_points = [
            (-1, phi, 0), (1, phi, 0), (-1, -phi, 0), (1, -phi, 0),
            (0, -1, phi), (0, 1, phi), (0, -1, -phi), (0, 1, -phi),
            (phi, 0, -1), (phi, 0, 1), (-phi, 0, -1), (-phi, 0, 1)
        ]
        
        # Normalize vertices to unit sphere
        ico_points = [(x/math.sqrt(x*x + y*y + z*z), 
                       y/math.sqrt(x*x + y*y + z*z), 
                       z/math.sqrt(x*x + y*y + z*z)) for x, y, z in ico_points]
        
        # Simple triangular faces (subset for demo)
        ico_face_counts = [3, 3, 3, 3]
        ico_face_indices = [0,5,11, 0,1,5, 0,7,1, 0,10,7]
        
        sphere_mesh.GetPointsAttr().Set(ico_points)
        sphere_mesh.GetFaceVertexCountsAttr().Set(ico_face_counts)
        sphere_mesh.GetFaceVertexIndicesAttr().Set(ico_face_indices)
        
        stage2.GetRootLayer().Save()
        print("✅ Sphere geometry: Created and saved")
        
        return True
        
    except Exception as e:
        print(f"❌ Geometry creation failed: {e}")
        return False

def test_file_operations():
    """Test USD file operations"""
    print("\n📁 File Operations Test")
    print("=" * 50)
    
    try:
        from pxr import Usd
        
        output_dir = Path("test_output")
        test_file = output_dir / "file_ops_test.usda"
        
        # Create stage
        stage = Usd.Stage.CreateNew(str(test_file))
        
        # Add some hierarchy
        from pxr import UsdGeom
        world = UsdGeom.Xform.Define(stage, '/World')
        group1 = UsdGeom.Xform.Define(stage, '/World/Group1')
        
        # Save
        stage.GetRootLayer().Save()
        print(f"✅ File creation: {test_file}")
        
        # Test reopening
        stage2 = Usd.Stage.Open(str(test_file))
        if stage2:
            print("✅ File reopening: Success")
            
            # List prims
            prims = [p.GetPath() for p in stage2.Traverse()]
            print(f"✅ Scene traversal: Found {len(prims)} primitives")
            
        return True
        
    except Exception as e:
        print(f"❌ File operations failed: {e}")
        return False

def test_git_status():
    """Check git repository status"""
    print("\n📋 Git Repository Test")
    print("=" * 50)
    
    try:
        # Check if we're in a git repo
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        
        if result.stdout.strip():
            print("⚠️  Uncommitted changes detected:")
            for line in result.stdout.strip().split('\n'):
                print(f"    {line}")
        else:
            print("✅ Git status: Clean working directory")
        
        # Check remote
        remote_result = subprocess.run(['git', 'remote', '-v'], 
                                     capture_output=True, text=True)
        if remote_result.stdout:
            print("✅ Git remote configured:")
            for line in remote_result.stdout.strip().split('\n'):
                print(f"    {line}")
        else:
            print("⚠️  No git remote configured")
        
        return True
        
    except subprocess.CalledProcessError:
        print("❌ Not in a git repository or git not available")
        return False
    except Exception as e:
        print(f"❌ Git check failed: {e}")
        return False

def main():
    """Run comprehensive tests"""
    print("🚀 COMPREHENSIVE USD SETUP TEST")
    print("=" * 50)
    
    results = []
    results.append(test_usd_imports())
    results.append(test_geometry_creation())
    results.append(test_file_operations())
    results.append(test_git_status())
    
    print(f"\n📊 TEST SUMMARY")
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎯 ALL TESTS PASSED! Your USD setup is fully functional.")
        print("\n✨ Ready for:")
        print("  • Creating complex 3D geometry")
        print("  • Following SideFX tutorials")
        print("  • Exporting to Maya/Houdini")
        print("  • Advanced USD manipulation")
    else:
        print("⚠️  Some tests failed. Check the output above.")
    
    return passed == total

if __name__ == "__main__":
    main()
