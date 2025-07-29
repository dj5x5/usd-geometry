"""
Basic 3D shape generators for USD export
Following PEP 20 principles of elegance and simplicity
"""
from pxr import Usd, UsdGeom, Sdf
from pathlib import Path
import math
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class GeometryData:
    """Elegant data structure for 3D geometry"""
    points: List[Tuple[float, float, float]]
    face_vertex_counts: List[int]
    face_vertex_indices: List[int]

def create_cone(resolution: int = 12, height: float = 2.0) -> GeometryData:
    """Create cone geometry with mathematical precision"""
    # Generate base circle points
    points = [
        (math.cos(2 * math.pi * i / resolution), 0, 
         math.sin(2 * math.pi * i / resolution))
        for i in range(resolution)
    ]
    
    # Add apex
    points.append((0, height, 0))
    
    # Generate triangular faces
    face_vertex_indices = []
    face_vertex_counts = []
    
    for i in range(resolution):
        triangle = [i, (i + 1) % resolution, resolution]
        face_vertex_indices.extend(triangle)
        face_vertex_counts.append(3)
    
    return GeometryData(points, face_vertex_counts, face_vertex_indices)

if __name__ == "__main__":
    # Test the cone creation
    cone = create_cone(resolution=16)
    print(f"Created cone with {len(cone.points)} points")
