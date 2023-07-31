*** Settings ***
# This library isn't found by default in `rpaframework`, so if the pre-run script
#  managed to install this, it will be importable and usable.
Library    RPA.Cloud.Google


*** Tasks ***
Private PyPI Library Usage
    # If this keyword is accessible, by taking our scarce conda.yaml into account, it
    #  means that the additional package from the "requirements-private.txt" file
    #  (`rpaframework-google`) got installed successfully.
    Set Robocorp Vault    Google    service_account
    Init Sheets    use_robocorp_vault=${True}
