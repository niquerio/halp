#!/usr/bin/env bash

echo "📦 Build python package"
poetry build


wheel=$(ls -Art dist/*.whl | tail -n 1)

echo "🛠️ Install package"
pip install --break-system-packages --force-reinstall $wheel

