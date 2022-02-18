import os
import sys
import subprocess
from RPA.Robocorp.Vault import Vault

EX_OK = getattr(os, "EX_OK", 0)
EX_USAGE = getattr(os, "EX_USAGE", 64)


class UsageError(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv):
    try:
        if len(argv) < 3:
            raise UsageError("Usage:  %s <secret_name> <command_line>" % sys.argv[0])

        # THIS THE BEEF
        # - INJECT SECRETS TO ENVIRONMENT VARIABLES
        my_env = os.environ.copy()
        secrets = Vault().get_secret(argv[1])
        for key in secrets.keys():
            my_env[key] = secrets[key]

        # ...AND RUN PIP INSTALL FOR PRIVATE PYPI
        subprocess.run("python -m pip install -r requirements.txt", env=my_env, shell=True)
        # FINISH WITH RUNNING THE REAL ROBOT
        subprocess.run(argv[2], shell=True)

        return EX_OK

    except UsageError as error:
        print(error.msg, file=sys.stderr)
        return EX_USAGE


if __name__ == '__main__':
    sys.exit(main(sys.argv))
