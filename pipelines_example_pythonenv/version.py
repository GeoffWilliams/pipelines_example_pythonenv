import os

version = "0.0.0"

def get_version():
    # set in pipelines environment
    build_number = os.environ.get("build_number", False)

    # python is picky about how version numbers are handled
    # see https://www.python.org/dev/peps/pep-0440
    return f"{version}+{build_number}" if build_number else version