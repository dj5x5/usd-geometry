#!/usr/bin/env python3
"""
Technical Artist USD Geometry Creation Suite
"""
from pxr import Usd, UsdGeom, Gf
from pathlib import Path
import math
from typing import List, Tuple, Dict

class TechArtistGeometry:
    """Professional geometry creation for technical artists"""
    
    def __init__(self, output_dir: str = "my_usd_files"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def create_cone(self, resolution: int = 16, height: float = 2.0, 
                   radius: float = 1.0, name: str = "cone") -> Path:
        """Create professional cone geometry"""
        filepath = self.output_dir / f"{name}.usda"
        stage = Usd.Stage.CreateNew(str(filepath))
        
        # Create hierarchy
        world = UsdGeom.Xform.Define(stage, '/World')
        mesh = UsdGeom.Mesh.Define(stage, f'/World/{name.title()}')
        
        # Generate vertices
        points = []
        # Base circle
        for i in range(resolution):
            angle = 2 * math.pi * i / resolution
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            points.append((x, 0, z))
        
        # Apex
        points.append((0, height, 0))
        
        # Generate faces
        face_vertex_counts = []
        face_vertex_indices = []
        
        # Side faces
        for i in range(resolution):
            next_i = (i + 1) % resolution
            face_vertex_indices.extend([i, next_i, resolution])
            face_vertex_counts.append(3)
        
        # Base face (optional)
        base_indices = list(reversed(range(resolution)))
        face_vertex_indices.extend(base_indices)
        face_vertex_counts.append(resolution)
        
        # Apply to mesh
        mesh.GetPointsAttr().Set(points)
        mesh.GetFaceVertexCountsAttr().Set(face_vertex_counts)
        mesh.GetFaceVertexIndicesAttr().Set(face_vertex_indices)
        
        # Professional USD attributes
        mesh.CreateOrientationAttr().Set("leftHanded")
        mesh.CreateSubdivisionSchemeAttr().Set("none")
        
        # Add metadata for technical artists
        stage.GetRootLayer().customLayerData = {
            'creator': 'Technical Artist USD Toolkit',
            'geometry_type': 'cone',
            'parameters': {
                'resolution': resolution,
                'height': height,
                'radius': radius
            }
        }
        
        stage.GetRootLayer().Save()
        print(f"✅ Created: {filepath}")
        return filepath
    
    def create_sphere(self, resolution: int = 20, radius: float = 1.0, 
                     name: str = "sphere") -> Path:
        """Create UV sphere geometry"""
        filepath = self.output_dir / f"{name}.usda"
        stage = Usd.Stage.CreateNew(str(filepath))
        
        mesh = UsdGeom.Mesh.Define(stage, f'/World/{name.title()}')
        
        points = []
        face_vertex_counts = []
        face_vertex_indices = []
        
        # Generate sphere vertices
        for v in range(resolution + 1):  # Vertical
            for u in range(resolution):  # Horizontal
                theta = math.pi * v / resolution  # 0 to pi
                phi = 2 * math.pi * u / resolution  # 0 to 2pi
                
                x = radius * math.sin(theta) * math.cos(phi)
                y = radius * math.cos(theta)
                z = radius * math.sin(theta) * math.sin(phi)
                points.append((x, y, z))
        
        # Generate faces
        for v in range(resolution):
            for u in range(resolution):
                # Current vertex indices
                current = v * resolution + u
                next_u = v * resolution + (u + 1) % resolution
                next_v = (v + 1) * resolution + u
                next_both = (v + 1) * resolution + (u + 1) % resolution
                
                # Create quad as two triangles
                face_vertex_indices.extend([current, next_v, next_both, next_u])
                face_vertex_counts.append(4)
        
        mesh.GetPointsAttr().Set(points)
        mesh.GetFaceVertexCountsAttr().Set(face_vertex_counts)
        mesh.GetFaceVertexIndicesAttr().Set(face_vertex_indices)
        mesh.CreateOrientationAttr().Set("leftHanded")
        
        stage.GetRootLayer().Save()
        print(f"✅ Created: {filepath}")
        return filepath

def main():
    """Demo for technical artists"""
    print("🎨 Technical Artist USD Geometry Suite")
    print("=" * 50)
    
    artist = TechArtistGeometry()
    
    # Create various geometries
    cone_file = artist.create_cone(resolution=24, height=3.0, name="detailed_cone")
    sphere_file = artist.create_sphere(resolution=16, name="smooth_sphere")
    
    print(f"\n📁 Geometry created in: {artist.output_dir}")
    print("🔧 Ready for Maya/Houdini import!")

if __name__ == "__main__":
    main()
