#########
# HELPERS
#########


import os
import tempfile
from subprocess import check_call


#########
# HELPERS
#########


def create_package_json(package_name: str, author: str, author_email: str) -> str:
    return f"""
{{
  "name": "{package_name}",
  "version": "0.0.1",
  "description": "A placeholder package to claim the name {package_name}",
  "main": "index.js",
  "author": "{author} <{author_email}>",
  "license": "ISC"
}}
"""


def create_package(package_name: str, author: str, author_email: str) -> str:
    # Create a temporary directory for the package
    temp_dir = tempfile.mkdtemp()
    package_dir = os.path.join(temp_dir, package_name)

    # Create package structure
    os.makedirs(package_dir)
    with open(os.path.join(package_dir, "index.js"), "w") as f:
        pass  # Empty file

    # Create package.json
    with open(os.path.join(package_dir, "package.json"), "w") as f:
        f.write(create_package_json(package_name, author, author_email))

    return package_dir


def upload_package(package_dir: str):
    check_call(["npm", "publish"], cwd=package_dir)


######
# MAIN
######


def claim_npm_package(package_name: str, author: str, author_name: str):
    package_dir = create_package(package_name, author, author_name)
    upload_package(package_dir)
