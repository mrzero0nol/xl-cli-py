# xl_cli/session.py

import json
import os

SESSION_FILE = os.path.expanduser("~/.xl_session.json")

def save_session(token: str):
    """Saves the session token to the session file."""
    session_data = {"token": token}
    try:
        with open(SESSION_FILE, "w") as f:
            json.dump(session_data, f)
        print(f"Session saved successfully to {SESSION_FILE}")
    except IOError as e:
        print(f"Error: Could not save session to {SESSION_FILE}. Reason: {e}")

def get_session_token() -> str | None:
    """
    Loads the session token from the session file.
    Returns the token if the file exists and is valid, otherwise None.
    """
    if not os.path.exists(SESSION_FILE):
        return None

    try:
        with open(SESSION_FILE, "r") as f:
            session_data = json.load(f)
            return session_data.get("token")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Warning: Could not read session file at {SESSION_FILE}. Reason: {e}")
        return None

def clear_session():
    """Deletes the session file, effectively logging the user out."""
    if os.path.exists(SESSION_FILE):
        try:
            os.remove(SESSION_FILE)
            print("Session cleared. You have been logged out.")
        except OSError as e:
            print(f"Error: Could not clear session file. Reason: {e}")
    else:
        print("No active session to clear.")

def is_logged_in() -> bool:
    """Checks if a valid session token exists."""
    return get_session_token() is not None
