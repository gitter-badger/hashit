from setuptools import setup
from hashit.version import __version__

LONG_DES = open("README.md", "r").read()

setup(
    name = "hashit",
    author = "Javad Shafique",
    author_email = "javadshafique@hotmail.com",
    version=__version__,
    license="MIT",
    include_package_data=True,
    test_suite="tests.unit",
    entry_points = {
        "console_scripts":[
            "hashit = hashit.__main__:main"
        ]
    },
    url="https://github.com/JavadSM/hashit",
    packages=["hashit"],
    install_requires = ["argc"],
    description = "Hashing Application",
    long_description = LONG_DES,
    classifiers = [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators"
    ]
)
