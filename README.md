# USD 3D Geometry Project

Modern Python implementation for 3D geometry creation and manipulation using Pixar's Universal Scene Description (USD).

## Setup

1. Create virtual environment: `python -m venv .venv`
2. Activate: `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Project Structure

- `src/primitives/` - Basic shape generators
- `src/exporters/` - USD export utilities  
- `src/tutorials/` - SideFX tutorial implementations
- `output/` - Generated USD files
- `notebooks/` - Jupyter exploration notebooks

## Usage
# USD 3D Geometry Project - WORKING! ✅

Modern Python implementation for 3D geometry creation and manipulation using Pixar's Universal Scene Description (USD).

## Current Status
- ✅ **USD Core 25.5.1** - Fully functional
- ✅ **Geometry Creation** - Cone generation working
- ✅ **File Export** - USD files created successfully
- ✅ **Python Environment** - Virtual environment stable

## Setup

1. Create virtual environment: `python -m venv .usd_env`
2. Activate: `source .usd_env/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Quick Test


## TBB Compatibility Fix

For ARM Mac users experiencing TBB library conflicts:

```bash
# Download compatible TBB version
wget https://github.com/uxlfoundation/oneTBB/releases/download/v2021.9.0/oneapi-tbb-2021.9.0-mac.tgz
tar -xzf oneapi-tbb-2021.9.0-mac.tgz
sudo cp -r oneapi-tbb-2021.9.0/lib/* /opt/homebrew/lib/

# Set library path in your shell profile
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

