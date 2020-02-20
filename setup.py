#!/usr/bin/python3
#
# Copyright (c) 2017-2019 NVIDIA CORPORATION. All rights reserved.
# This file is part of webloader (see TBD).
# See the LICENSE file for licensing terms (BSD-style).
#

VERSION='0.0.0'

import glob
import sys
from distutils.core import setup  # , Extension, Command

if sys.version_info < (3, 6):
    sys.exit("Python versions less than 3.6 are not supported")

scripts = []

setuptools.setup(
    name='webdataset',
    version=VERSION,
    description="Record sequential storage for deep learning.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/tmbdev/webdataset",
    author="Thomas Breuel",
    author_email="tmbdev+removeme@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords="object store, client, deep learning",
    packages=["webdataset"],
    python_requires=">=3.6",
    scripts=scripts,
    install_requires="Pillow simplejson braceexpand msgpack pyyaml numpy torch".split()
)
