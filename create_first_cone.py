#!/usr/bin/env python3
"""
Your first USD geometry creation - working immediately!
"""
from pxr import Usd, UsdGeom
import math
from pathlib import Path

def create_cone_usd():
    """Create a cone and export to USD"""
    
    # Create output directory
    output_dir = Path("my_usd_files")
    output_dir.mkdir(exist_ok=True)
    
    # Create USD stage
    stage = Usd.Stage.CreateNew(str(output_dir / "cone.usda"))
    
    # Create cone geometry
    cone_mesh = UsdGeom.Mesh.Define(stage, '/Cone')
    
    # Define cone vertices (base circle + apex)
    resolution = 12
    points = []
    
    # Base circle
    for i in range(resolution):
        angle = 2 * math.pi * i / resolution
        x = math.cos(angle)
        z = math.sin(angle)
        points.append((x, 0, z))
    
    # Apex
    points.append((0, 2, 0))
    
    # Define faces (triangles from base to apex)
    face_vertex_counts = []
    face_vertex_indices = []
    
    for i in range(resolution):
        next_i = (i + 1) % resolution
        # Triangle: base[i], base[next_i], apex
        face_vertex_indices.extend([i, next_i, resolution])
        face_vertex_counts.append(3)
    
    # Set mesh data
    cone_mesh.GetPointsAttr().Set(points)
    cone_mesh.GetFaceVertexCountsAttr().Set(face_vertex_counts)
    cone_mesh.GetFaceVertexIndicesAttr().Set(face_vertex_indices)
    
    # Set orientation
    cone_mesh.CreateOrientationAttr().Set("leftHanded")
    
    # Save the stage
    stage.GetRootLayer().Save()
    
    print(f"✅ Cone created: {output_dir / 'cone.usda'}")
    print(f"📊 Vertices: {len(points)}")
    print(f"📐 Faces: {len(face_vertex_counts)}")

if __name__ == "__main__":
    create_cone_usd()
