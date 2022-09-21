# example-private-pypi

Recipe for accessing private PyPI packages with credentials in Robocorp Vault.

But not limited to, as in the [requirements-private.txt](https://github.com/robocorp/example-private-pypi/blob/master/requirements-private.txt)
you'll find examples on how to install Python packages from the following:
- Private repository using a Vault provided `github_token`.
- Local source with a directory path accessible by the robot.

## Setup & Run

1. Create a Vault secrets store named "private_pypi".
   1. Inside of it fill-in the secrets you're going to use, like: `pypi_usr`,
      `pypi_pwd` and/or `github_token`.
2. Run the bot with VSCode (and make sure the Robocorp extension is connected to the
   cloud, so it can access the online Vault) and select a task which demonstrates how
   the private packages get installed and used.

### Tasks

- `Private PyPI Library Usage`: Installs and uses a library from a private PyPI.
  Requires the following secret keys in the "private_pypi" Vault: `pypi_usr` &
  `pypi_pwd`.
- `Private Repo Or Local Source Library Usage`: Installs and uses a library coming from
  either a private repository or a local source. For the private repository, the
  `github_token` secret key will be enough.

## How it works

1. The [robot.yaml](https://github.com/robocorp/example-private-pypi/blob/master/robot.yaml) contains an entry called `preRunScripts` which
   instructs **rcc** to execute a script like
   [private-pip-install.py](https://github.com/robocorp/example-private-pypi/blob/master/bin/private-pip-install.py) right before the robot run.
2. The script receives as parameters the Vault secret store name and the path to the
   [requirements](https://github.com/robocorp/example-private-pypi/blob/master/requirements-private.txt) file to be installed by **pip**,
   containing private sources for the dependencies.
3. The script injects into the env, variables used by the `pip install` which is run to
   install the private requirements.
4. Once the script finishes, the selected task will run and use the library installed
   previously, thus demonstrating that the Python environment contains the requested
   dependencies coming from private sources.
