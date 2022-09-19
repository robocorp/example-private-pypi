*** Settings ***
Library    RPA.Cloud.Google


*** Tasks ***
Private PyPI Library Usage
    Init Gmail    use_robocorp_vault=${True}
