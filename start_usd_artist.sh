#!/bin/bash
# Technical Artist USD Daily Workflow

echo "🎨 USD Technical Artist Environment"
echo "=================================="

# Navigate to project
cd /Users/dymaxion/Documents/PROJECTS/CODE/USD_v03

# Activate virtual environment
source .usd_env/bin/activate

# Set up clean environment
source setup_usd_env.sh

# Quick functionality test
python -c "
from pxr import Usd, UsdGeom
import sys
print(f'✅ USD {sys.modules[\"pxr\"].__file__.split(\"/\")[-3]} ready')
print('✅ Geometry creation enabled')
print('✅ File export/import ready')
"

echo ""
echo "📁 Project Structure:"
echo "  my_usd_files/     - Your USD geometry files"
echo "  src/primitives/   - Shape generation scripts"  
echo "  src/exporters/    - Maya/Houdini integration"
echo ""
echo "🚀 Ready for Technical Artist work!"
echo "Common commands:"
echo "  code .                          # Open in VS Code"
echo "  python create_geometry.py       # Create 3D shapes"
echo "  python analyze_usd.py          # Study USD structure"
echo ""
