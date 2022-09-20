# This library is installed from a private repo or local source through the pre-run
#  script invoking the pip installation of the requirements-private.txt file.
import fire


def hello(name="World"):
    return f"Hello {name}!"


if __name__ == "__main__":
    # This prints "Hello World" if it runs successfully.
    fire.Fire(hello)
