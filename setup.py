from setuptools import setup

# Save people like Pat from themselves:
import sys

if sys.version_info < (3, 0):
    sys.exit("Sorry, Python < 3.0 is not supported")

import re

VERSIONFILE = "tockloader/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="tockloader",
    version=verstr,
    description="TockOS Support Tool",
    long_description="Please visit `Github <https://github.com/tock/tockloader>`_ for more information.",
    author="Tock Project Developers",
    author_email="tock-dev@googlegroups.com",
    url="https://github.com/tock/tockloader",
    packages=["tockloader"],
    entry_points={"console_scripts": ["tockloader = tockloader.main:main"]},
    include_package_data=True,
    install_requires=[
        "argcomplete >= 1.8.2",
        "colorama >= 0.3.7",
        "crcmod >= 1.7",
        "ecdsa >= 0.19.1",
        "pycryptodome >= 3.15.0",
        "pynrfjprog == 10.19.0",
        "pyserial >= 3.0.1",
        "siphash >= 0.0.1",
        "six >= 1.9.0",
        "toml >= 0.10.2",
        "tqdm >= 4.45.0 ",
        "questionary >= 1.10.0",
    ],
)
