#!/bin/bash
# USD Environment Setup for ARM Mac

export USD_INSTALL_ROOT="$HOME/usd_install"
export PYTHONPATH="$USD_INSTALL_ROOT/lib/python:$PYTHONPATH"
export PATH="$USD_INSTALL_ROOT/bin:$PATH"

# For macOS ARM64 compatibility
export DYLD_LIBRARY_PATH="$USD_INSTALL_ROOT/lib:$DYLD_LIBRARY_PATH"

echo "USD environment configured"
echo "USD_INSTALL_ROOT: $USD_INSTALL_ROOT"
