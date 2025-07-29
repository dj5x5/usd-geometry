#!/bin/bash
# USD Development Workflow

echo "🚀 USD Development Environment"

# Activate environment
source .usd_env/bin/activate

# Quick system check
echo "📋 System Status:"
python -c "from pxr import Usd; print('✅ USD Ready')"

# Show available commands
echo "
💻 Available commands:
  python create_first_cone.py       # Create cone geometry
  python system_check_fixed.py      # Full system check
  code .                            # Open in VS Code
  git status                        # Check repository status
"
