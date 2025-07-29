#!/bin/bash
# Complete USD development environment startup

echo "🚀 Starting USD Development Environment"

# Navigate to project
cd /Users/dymaxion/Documents/PROJECTS/CODE/USD_v03

# Activate Python environment
source .usd_env/bin/activate

# Set up USD environment
source setup_usd_env.sh

# Test USD functionality
python test_usd_build.py

echo "💻 Environment ready! Available commands:"
echo "  code .                          # Open VS Code"
echo "  python create_first_cone.py     # Create test geometry"
echo "  python system_check_fixed.py    # Full system check"
echo "  deactivate                      # Exit virtual environment"

# Note: Environment is now active in your current shell
