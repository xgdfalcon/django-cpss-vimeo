#! /usr/bin/env python
# encoding: utf-8

#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
#

import os
import sys
from distutils.sysconfig import get_python_lib
from os.path import join, dirname

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup()