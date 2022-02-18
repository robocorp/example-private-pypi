# example-private-pypi
Recipe for accessing private PyPI packages with credentials in Robocorp Vault

`robot.yaml` defines a robot:

    shell: python prepare.py PYPI_SECRETS "python the_real_robot.py"

`prepare.py` reads credentials from Robocorp Vault and injects them as environment variables for `pip install`. As a final step it runs the command defined in `robot.yaml`.

    my_env = os.environ.copy()
    secrets = Vault().get_secret(argv[1])
    for key in secrets.keys():
        my_env[key] = secrets[key]

    subprocess.run("python -m pip install -r requirements.txt", env=my_env, shell=True)
    subprocess.run(argv[2], shell=True)

