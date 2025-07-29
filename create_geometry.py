"""
Modern USD 3D geometry creation - working example
"""
from pxr import Usd, UsdGeom, Sdf, Gf
from pathlib import Path
import math

def create_cone_geometry(resolution=12, height=2.0):
    """Create cone geometry data"""
    # Base circle points
    points = []
    for i in range(resolution):
        angle = 2 * math.pi * i / resolution
        x = math.cos(angle)
        z = math.sin(angle)
        points.append((x, 0, z))
    
    # Add apex
    points.append((0, height, 0))
    
    # Create triangular faces
    face_vertex_counts = []
    face_vertex_indices = []
    
    for i in range(resolution):
        next_i = (i + 1) % resolution
        # Triangle: base vertex i, base vertex i+1, apex
        face_vertex_indices.extend([i, next_i, resolution])
        face_vertex_counts.append(3)
    
    return points, face_vertex_counts, face_vertex_indices

def export_to_usd(points, face_counts, face_indices, filename="cone.usda"):
    """Export geometry to USD file"""
    
    # Create output directory
    output_dir = Path("usd_output")
    output_dir.mkdir(exist_ok=True)
    filepath = output_dir / filename
    
    # Create USD stage
    stage = Usd.Stage.CreateNew(str(filepath))
    
    # Create hierarchy
    world = UsdGeom.Xform.Define(stage, '/World')
    
    # Create mesh
    mesh = UsdGeom.Mesh.Define(stage, '/World/Cone')
    
    # Set mesh data
    mesh.GetPointsAttr().Set(points)
    mesh.GetFaceVertexCountsAttr().Set(face_counts)
    mesh.GetFaceVertexIndicesAttr().Set(face_indices)
    
    # Set USD best practices
    mesh.CreateOrientationAttr().Set("leftHanded")
    mesh.CreateSubdivisionSchemeAttr().Set("none")
    
    # Save the file
    stage.GetRootLayer().Save()
    
    print(f"✅ USD file created: {filepath}")
    return filepath

def main():
    """Create and export cone geometry"""
    print("🎯 Creating USD Cone Geometry")
    
    # Create geometry
    points, face_counts, face_indices = create_cone_geometry(resolution=16, height=2.5)
    
    # Export to USD
    filepath = export_to_usd(points, face_counts, face_indices, "my_cone.usda")
    
    print(f"📁 Cone created with {len(points)} vertices")
    print(f"📁 File saved: {filepath}")
    
    # Display file contents (first 20 lines)
    print("\n📄 USD File Preview:")
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            if i < 20:
                print(f"  {line.strip()}")
            else:
                print("  ...")
                break

if __name__ == "__main__":
    main()
