#!/bin/bash
# Technical Artist USD Daily Workflow - ARM Mac Optimized

echo "🎨 USD Technical Artist Environment"
echo "=================================="

# Navigate to project
cd /Users/dymaxion/Documents/PROJECTS/CODE/USD_v03

# Activate virtual environment
source .usd_env/bin/activate

# Set library path for TBB compatibility (critical for ARM Mac)
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"

# Quick USD verification
python -c "
from pxr import Usd, UsdGeom
print('✅ USD ready for geometry creation')
"

echo ""
echo "📁 Project Structure:"
echo "  my_usd_files/     - Your USD geometry files"
echo "  src/primitives/   - Shape generation scripts"  
echo "  src/exporters/    - Maya/Houdini integration"
echo ""
echo "🚀 Ready for Technical Artist work!"
echo "Common commands:"
echo "  python create_geometry.py       # Create 3D shapes"
echo "  python analyze_usd.py          # Study USD structure"
echo "  code .                         # Open in VS Code"
