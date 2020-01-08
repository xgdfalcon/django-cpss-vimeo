#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
# 

"""
This python module provides...

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.apps import AppConfig

class PythonVimeoAuthConfig(AppConfig):
    # Full Python path to the application eg. 'django.contrib.admin'.
    name = 'vimeo_django'
    # Last component of the Python path to the application eg. 'admin'.
    label = 'vimeo_django'
    # Human-readable name for the application eg. "Admin".
    verbose_name = 'CPSS Vimeo Django'
