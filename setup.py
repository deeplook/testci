#!/usr/bin/env python

import sys
from os.path import abspath, dirname, join

from setuptools import setup

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []
this_directory = abspath(dirname(__file__))
with open(join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="testci",
    version="0.0.1",
    description=(
        "Explore Travis-CI build/platform options."
    ),
    long_description_content_type="text/x-rst",
    long_description=long_description,
    url="https://github.com/deeplook/testci",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Installation/Setup",
    ],
    setup_requires=[] + pytest_runner,
    tests_require=["pytest"],
    py_modules=["testci"],
    entry_points={"console_scripts": ["testci=testci:main"]},
)
