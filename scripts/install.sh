#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Log function for better readability
log() {
    echo -e "\033[1;32m[INFO]\033[0m $1"
}

log "Installing Poetry..."

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH (for the current session)
export PATH="$HOME/.local/bin:$PATH"

# Disable virtualenv creation (use system Python environment)
poetry config virtualenvs.create true

log "Poetry installation complete."

# Verify installation
poetry --version

log "Installing poetry shell"
# ref: https://github.com/python-poetry/poetry-plugin-shell
poetry self add poetry-plugin-shell

log "Installing project dependencies with Poetry..."

# Install project dependencies
poetry install --no-root

sudo apt update
sudo apt install -y chromium
sudo apt install -y chromium-driver
sudo apt update && sudo apt install -y fonts-wqy-zenhei fonts-noto fonts-noto-cjk
# # 安裝 Chrome 瀏覽器
# sudo apt-get update && apt-get install -y wget gnupg2
# sudo wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# sudo echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# sudo apt-get update && apt-get install -y google-chrome-stable