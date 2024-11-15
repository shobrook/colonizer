try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
import sys

if sys.version_info[:3] < (3, 0, 0):
    sys.stdout.write("Requires Python 3 to run.")
    sys.exit(1)

with open("README.md", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="colonizer",
    version="1.0.4",
    description="A terrible tool for bad people",
    url="https://github.com/shobrook/colonizer",
    author="shobrook",
    author_email="shobrookj@gmail.com",
    keywords="pypi npm node python package reserve template project generator",
    include_package_data=True,
    packages=["colonizer"],
    entry_points={"console_scripts": ["colonizer = colonizer.colonizer:main"]},
    # install_requires=["pystache"],
    requires=[],
    python_requires=">=3",
    license="MIT",
)
