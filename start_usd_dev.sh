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

echo "💻 Environment ready! Use 'code .' to open VS Code"
