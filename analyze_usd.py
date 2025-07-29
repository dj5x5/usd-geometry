#!/usr/bin/env python3
"""
USD File Analysis Tool for Technical Artists
"""
from pxr import Usd, UsdGeom
from pathlib import Path

def analyze_usd_file(filepath: Path):
    """Analyze USD file structure"""
    print(f"🔍 Analyzing: {filepath.name}")
    print("=" * 50)
    
    stage = Usd.Stage.Open(str(filepath))
    if not stage:
        print("❌ Could not open file")
        return
    
    # Traverse hierarchy
    print("📁 Scene Hierarchy:")
    for prim in stage.Traverse():
        indent = "  " * (len(prim.GetPath().pathString.split('/')) - 2)
        prim_type = prim.GetTypeName()
        print(f"{indent}{prim.GetName()} ({prim_type})")
        
        # Show mesh details
        if prim_type == "Mesh":
            mesh = UsdGeom.Mesh(prim)
            points = mesh.GetPointsAttr().Get()
            faces = mesh.GetFaceVertexCountsAttr().Get()
            if points and faces:
                print(f"{indent}  └─ Vertices: {len(points)}, Faces: {len(faces)}")
    
    # Show layer info
    print(f"\n💾 File Info:")
    print(f"  Format: {filepath.suffix}")
    print(f"  Size: {filepath.stat().st_size} bytes")
    
    # Custom metadata
    custom_data = stage.GetRootLayer().customLayerData
    if custom_data:
        print(f"  Metadata: {custom_data}")

def main():
    """Analyze all USD files in project"""
    usd_dir = Path("my_usd_files")
    
    if not usd_dir.exists():
        print("No USD files found. Run create_geometry.py first!")
        return
    
    usd_files = list(usd_dir.glob("*.usd*"))
    
    for usd_file in usd_files:
        analyze_usd_file(usd_file)
        print()

if __name__ == "__main__":
    main()
