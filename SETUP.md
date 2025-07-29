# USD Development Environment Setup

## Working Configuration
- **Platform**: macOS 15.5 ARM64 (Apple Silicon)
- **Python**: 3.10.13 in virtual environment
- **USD**: usd-core 25.5.1 (pip-installed)
- **TBB Fix**: oneTBB 2021.9.0 for compatibility

# USD Environment Setup

## Quick Start

1. **Create virtual environment:**
   ```
   python3 -m venv .usd_env
   source .usd_env/bin/activate
   ```

2. **Install Python dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Fix TBB compatibility (ARM Mac only):**
   ```
   # Download compatible TBB version
   wget https://github.com/uxlfoundation/oneTBB/releases/download/v2021.9.0/oneapi-tbb-2021.9.0-mac.tgz
   tar -xzf oneapi-tbb-2021.9.0-mac.tgz
   sudo cp -r oneapi-tbb-2021.9.0/lib/* /opt/homebrew/lib/
   
   # Set library path (add to your shell profile)
   export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
   ```

4. **Verify installation:**
   ```
   python test_usd_fix.py
   ```

5. **Start developing:**
   ```
   source start_usd_artist.sh
   python create_geometry.py
   ```

## Troubleshooting

If you get TBB symbol errors, ensure the library path is set:
```
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

## System Requirements

- macOS with Apple Silicon (ARM64)
- Python 3.10+
- Homebrew installed
- Git for repository management

## File Structure

After setup, your project should look like:
```
USD_v03/
├── .usd_env/                 # Virtual environment
├── my_usd_files/            # Generated USD geometry files
├── src/                     # Source code
├── create_geometry.py       # Geometry creation tool
├── test_usd_fix.py         # USD installation validator
├── start_usd_artist.sh     # Daily workflow script
├── requirements.txt        # Python dependencies
└── SETUP.md               # This file
```