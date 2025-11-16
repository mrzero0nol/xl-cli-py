#!/bin/bash

# A simple setup script for the XL CLI Tool on Termux.

# Colors for output
GREEN='\033[0;32m'
NC='\033[0m' # No Color
YELLOW='\033[1;33m'
RED='\033[0;31m'

echo -e "${GREEN}Starting XL CLI setup...${NC}"

# --- Step 1: Install Dependencies ---
echo -e "\n${YELLOW}Step 1: Installing Python dependencies...${NC}"
if pip install -r xl_cli/requirements.txt; then
    echo -e "${GREEN}Dependencies installed successfully.${NC}"
else
    echo -e "${RED}Failed to install dependencies. Please check your internet connection and try again.${NC}"
    exit 1
fi

# --- Step 2: Prepare the executable script ---
echo -e "\n${YELLOW}Step 2: Preparing the 'xl' command...${NC}"

# Get the absolute path to the current directory
PROJECT_DIR=$(pwd)
EXECUTABLE_PATH="$PROJECT_DIR/xl"
PYTHON_COMMAND="python3 -m xl_cli.main \"\$@\""

# Modify the 'xl' script to use the absolute path of the project
# This ensures it can be run from any directory
# We use a temporary file to avoid issues with sed's in-place editing on some systems
sed "s|python3 -m xl_cli.main \"\$@\"|cd $PROJECT_DIR \&\& $PYTHON_COMMAND|" "$EXECUTABLE_PATH" > "$EXECUTABLE_PATH.tmp" && mv "$EXECUTABLE_PATH.tmp" "$EXECUTABLE_PATH"

if [ $? -eq 0 ]; then
    echo "Executable script configured."
else
    echo -e "${RED}Failed to configure the executable script.${NC}"
    exit 1
fi

# Make the script executable
chmod +x "$EXECUTABLE_PATH"
if [ $? -eq 0 ]; then
    echo "Executable permissions set."
else
    echo -e "${RED}Failed to set executable permissions.${NC}"
    exit 1
fi

# --- Step 3: Move the executable to Termux bin directory ---
# This makes the 'xl' command available system-wide in Termux
TERMUX_BIN_DIR="/data/data/com.termux/files/usr/bin"
echo -e "\n${YELLOW}Step 3: Installing the 'xl' command to ${TERMUX_BIN_DIR}...${NC}"

if [ -d "$TERMUX_BIN_DIR" ]; then
    mv "$EXECUTABLE_PATH" "$TERMUX_BIN_DIR/xl"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Command 'xl' installed successfully!${NC}"
    else
        echo -e "${RED}Failed to move the 'xl' command. You may need to run this with higher privileges.${NC}"
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

exit 0
