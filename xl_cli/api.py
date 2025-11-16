# xl_cli/api.py

import requests
import json
from . import config
from .session import get_session_token

class XLAPIClient:
    def __init__(self):
        self.base_url = config.BASE_API_URL
        self.ciam_url = config.BASE_CIAM_URL
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": config.UA,
            "X-Device-ID": config.AX_DEVICE_ID,
            "X-FP-Key": config.AX_FP_KEY,
            "X-Api-Key": config.API_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _get_auth_headers(self):
        """Returns headers required for authenticated requests."""
        token = get_session_token()
        if not token:
            raise Exception("You are not logged in. Please run 'xl-cli login' first.")
        return {
            "Authorization": f"Bearer {token}"
        }

    def request_otp(self, msisdn: str):
        """
        Requests an OTP for the given phone number (msisdn).
        """
        url = f"{self.ciam_url}/ciam/v1/request-otp"
        payload = {
            "msisdn": msisdn,
            "isdCode": "62"
        }
        headers = {
            "Authorization": f"Basic {config.BASIC_AUTH}"
        }

        try:
            response = self.session.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            if e.response:
                print(f"Error details: {e.response.text}")
            return None

    def validate_otp(self, msisdn: str, otp: str):
        """
        Validates the OTP and retrieves an authentication token.
        """
        url = f"{self.ciam_url}/ciam/v1/validate-otp"
        payload = {
            "msisdn": msisdn,
            "otp": otp
        }
        headers = {
            "Authorization": f"Basic {config.BASIC_AUTH}"
        }

        try:
            response = self.session.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            # Assuming the token is in the response JSON, e.g., {"token": "..."}
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            if e.response:
                print(f"Error details: {e.response.text}")
            return None

    def get_packages(self):
        """
        Fetches the list of available data packages.
        (This is a placeholder, endpoint and parameters are guessed)
        """
        url = f"{self.base_url}/v1/packages"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            if e.response:
                print(f"Error details: {e.response.text}")
            return None


    def purchase_package(self, package_id: str, family_code: str):
        """
        Purchases a data package using a family code.
        (This is a placeholder, endpoint, payload, and encryption are guessed)
        """
        # In a real scenario, this payload might need to be encrypted.
        # We will add encryption logic later if needed.
        url = f"{self.base_url}/v1/purchase"
        payload = {
            "packageId": package_id,
            "familyCode": family_code
        }
        headers = self._get_auth_headers()

        try:
            response = self.session.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            if e.response:
                print(f"Error details: {e.response.text}")
            return None
