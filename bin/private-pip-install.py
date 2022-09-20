#! /usr/bin/env python


import os
import subprocess
import sys

from RPA.Robocorp.Vault import Vault


# Some of these secrets (not all at once) will be required based on the env vars used
#  in the requirements-private.txt file.
REQUIRED_SECRETS = {
    # With private PyPI.
    "PYPI_USR": "pypi_usr",
    "PYPI_PWD": "pypi_pwd",
    # When installing from private repo.
    "GITHUB_TOKEN": "github_token",
}

lib_vault = Vault()


def pip_install(requirements_path, env=None):
    # Runs `pip install -Ur requirements-private.txt` with the current Python
    #  interpreter.
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-Ur", requirements_path],
        env=env
    )


def main(argv):
    if len(argv) != 3:
        print(f"Usage: {argv[0]} VAULT_SECRETS_NAME REQUIREMENTS_PATH")
        return

    # Prepares an environment with injected secrets from the Vault, required by the
    #  `pip install` command so it can access the private sources.
    pip_env = os.environ.copy()
    secrets = lib_vault.get_secret(argv[1])
    for env_var, secret_name in REQUIRED_SECRETS.items():
        pip_env[env_var] = secrets[secret_name]

    # Runs `pip install` over the provided requirements file within an env containing
    #  all the required secrets from the Vault.
    pip_install(argv[2], env=pip_env)


if __name__ == "__main__":
    main(sys.argv)
