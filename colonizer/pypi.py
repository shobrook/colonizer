import os
import sys
import tempfile
from subprocess import check_call


#########
# HELPERS
#########


def create_setup_py(package_name: str, author: str, author_email: str) -> str:
    return f"""
from setuptools import setup

setup(
    name='{package_name}',
    description='{package_name}',
    version='0.0.1',
    author={author},
    author_email={author_email}
)
"""


def create_package(package_name: str, author: str, author_email: str) -> str:
    # Create a temporary directory for the package
    temp_dir = tempfile.mkdtemp()
    package_dir = os.path.join(temp_dir, package_name)

    # Create package structure
    os.makedirs(package_dir)
    with open(os.path.join(package_dir, "__init__.py"), "w") as f:
        pass  # Empty file

    # Create setup.py
    with open(os.path.join(temp_dir, "setup.py"), "w") as f:
        f.write(create_setup_py(package_name, author, author_email))

    # Build the package
    check_call([sys.executable, "setup.py", "sdist"], cwd=temp_dir)

    return temp_dir


def upload_package(package_dir: str):
    check_call(["twine", "upload", "dist/*"], cwd=package_dir)


######
# MAIN
######


def claim_pypi_package(package_name: str):
    package_dir = create_package(package_name)
    upload_package(package_dir)
