# xl_cli/config.py

import json
import os
import sys

# The configuration is now loaded from an external config.json file.
# This makes it easier for users to update API keys without changing the code.

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def load_config():
    """Loads the configuration from config.json."""
    if not os.path.exists(CONFIG_FILE_PATH):
        print("Error: Configuration file 'config.json' not found in the 'xl_cli' directory.", file=sys.stderr)
        print("Please copy 'config.json.template' to 'config.json' and fill in your credentials.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error: Could not read or parse the configuration file: {e}", file=sys.stderr)
        sys.exit(1)

# Load the configuration once when the module is imported
_config = load_config()

# Assign config values to module-level variables for easy access
BASE_API_URL = _config.get("BASE_API_URL")
BASE_CIAM_URL = _config.get("BASE_CIAM_URL")
BASIC_AUTH = _config.get("BASIC_AUTH")
BASIC_KEYS = _config.get("BASIC_KEYS")
AX_DEVICE_ID = _config.get("AX_DEVICE_ID")
AX_FP_KEY = _config.get("AX_FP_KEY")
UA = _config.get("UA")
API_KEY = _config.get("API_KEY")
AES_KEY = _config.get("AES_KEY")
AES_KEY_ASCII = _config.get("AES_KEY_ASCII")

# Validate that essential keys are present
if not all([BASE_API_URL, BASE_CIAM_URL, BASIC_AUTH, API_KEY]):
    print("Error: One or more essential keys are missing from 'config.json'.", file=sys.stderr)
    print("Please ensure BASE_API_URL, BASE_CIAM_URL, BASIC_AUTH, and API_KEY are set.", file=sys.stderr)
    sys.exit(1)
