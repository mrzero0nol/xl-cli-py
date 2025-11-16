# xl_cli/main.py

import click
from .api import XLAPIClient
from .session import save_session, clear_session, is_logged_in

@click.group()
def cli():
    """A CLI tool to interact with the XL Axiata API."""
    pass

@cli.command()
def login():
    """Logs in to the XL service by requesting and validating an OTP."""
    if is_logged_in():
        click.echo("You are already logged in.")
        return

    msisdn = click.prompt("Please enter your phone number (e.g., 81234567890)", type=str)

    client = XLAPIClient()

    click.echo(f"Requesting OTP for {msisdn}...")
    otp_response = client.request_otp(msisdn)

    if not otp_response or otp_response.get('success') is False:
        click.echo("Failed to request OTP. Please check the number and try again.")
        return

    click.echo("OTP has been sent to your number.")

    otp_code = click.prompt("Please enter the OTP you received", type=str)

    click.echo("Validating OTP...")
    token_response = client.validate_otp(msisdn, otp_code)

    # Assuming a successful response contains a 'token'
    if token_response and 'token' in token_response:
        save_session(token_response['token'])
        click.echo("Login successful!")
    else:
        click.echo("Login failed. The OTP may be incorrect or expired.")

@cli.command(name="list-packages")
def list_packages():
    """Lists available data packages."""
    if not is_logged_in():
        click.echo("You must be logged in to view packages. Please run 'login' first.")
        return

    client = XLAPIClient()
    click.echo("Fetching packages...")
    packages = client.get_packages()

    if packages and isinstance(packages, list):
        # Assuming packages is a list of dicts with 'id', 'name', 'price'
        for pkg in packages:
            click.echo(f"ID: {pkg.get('id', 'N/A')} | Name: {pkg.get('name', 'N/A')} | Price: {pkg.get('price', 'N/A')}")
    else:
        click.echo("Could not retrieve packages or no packages are available.")

@cli.command(name="buy-package")
@click.argument("package_id")
@click.argument("family_code")
def buy_package(package_id, family_code):
    """Purchases a package using a specific package ID and family code."""
    if not is_logged_in():
        click.echo("You must be logged in to purchase a package. Please run 'login' first.")
        return

    client = XLAPIClient()
    click.echo(f"Attempting to purchase package {package_id} with family code...")

    purchase_response = client.purchase_package(package_id, family_code)

    if purchase_response and purchase_response.get('success'):
        click.echo("Package purchased successfully!")
        click.echo(f"Transaction ID: {purchase_response.get('transactionId', 'N/A')}")
    else:
        error_message = purchase_response.get('message', 'An unknown error occurred.')
        click.echo(f"Failed to purchase package. Reason: {error_message}")

@cli.command()
def logout():
    """Logs out by clearing the current session."""
    clear_session()

if __name__ == "__main__":
    cli()
