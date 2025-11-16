#!/bin/bash

# A simple setup script for the XL CLI Tool on Termux.

# Colors for output
GREEN='\033[0;32m'
NC='\033[0m' # No Color
YELLOW='\033[1;33m'
RED='\033[0;31m'

echo -e "${GREEN}Starting XL CLI setup...${NC}"
PROJECT_DIR=$(pwd)

# --- Step 1: Create config file if it doesn't exist ---
CONFIG_FILE="$PROJECT_DIR/xl_cli/config.json"
TEMPLATE_FILE="$PROJECT_DIR/xl_cli/config.json.template"

if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "\n${YELLOW}Step 1: Configuration file not found. Creating from template...${NC}"
    if cp "$TEMPLATE_FILE" "$CONFIG_FILE"; then
        echo -e "${GREEN}Created 'config.json'. You can edit this file later to update your API keys.${NC}"
    else
        echo -e "${RED}Failed to create configuration file.${NC}"
        exit 1
    fi
else
    echo -e "\n${GREEN}Step 1: Existing 'config.json' found. Skipping creation.${NC}"
fi

# --- Step 2: Install Dependencies ---
echo -e "\n${YELLOW}Step 2: Installing Python dependencies...${NC}"
if pip install -r xl_cli/requirements.txt; then
    echo -e "${GREEN}Dependencies installed successfully.${NC}"
else
    echo -e "${RED}Failed to install dependencies. Please check your internet connection and try again.${NC}"
    exit 1
fi

# --- Step 3: Prepare the executable script ---
echo -e "\n${YELLOW}Step 3: Preparing the 'xl' command...${NC}"
EXECUTABLE_PATH="$PROJECT_DIR/xl"
PYTHON_COMMAND="python3 -m xl_cli.main \"\$@\""

sed "s|python3 -m xl_cli.main \"\$@\"|cd $PROJECT_DIR \&\& $PYTHON_COMMAND|" "$EXECUTABLE_PATH" > "$EXECUTABLE_PATH.tmp" && mv "$EXECUTABLE_PATH.tmp" "$EXECUTABLE_PATH"
chmod +x "$EXECUTABLE_PATH"

# --- Step 4: Move the executable to Termux bin directory ---
TERMUX_BIN_DIR="/data/data/com.termux/files/usr/bin"
echo -e "\n${YELLOW}Step 4: Installing the 'xl' command to ${TERMUX_BIN_DIR}...${NC}"

if [ -d "$TERMUX_BIN_DIR" ]; then
    if mv "$EXECUTABLE_PATH" "$TERMUX_BIN_DIR/xl"; then
        echo -e "${GREEN}Command 'xl' installed successfully!${NC}"
    else
        echo -e "${RED}Failed to move the 'xl' command. If it exists, it may be in use.${NC}"
        exit 1
    fi
else
    echo -e "${RED}Termux bin directory not found. Are you running this on Termux?${NC}"
    exit 1
fi

# --- Final Message ---
echo -e "\n${GREEN}Setup is complete!${NC}"
echo "You can now run the application from anywhere by simply typing:"
echo -e "${YELLOW}xl${NC}\n"
echo "If you encounter a '403 Forbidden' error, it means your API keys in 'xl_cli/config.json' are likely expired."
echo "Please update them with new ones."

exit 0
