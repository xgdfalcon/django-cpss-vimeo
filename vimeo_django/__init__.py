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

__version__ = '1.0.0'



# django.contrib.auth.load_backend() will import and instanciate the
# authentication backend ignoring the possibility that it might
# require more arguments. Here we set a monkey patch to
# BaseAuth.__init__ to ignore the mandatory strategy argument and load
# it.

# def baseauth_init_workaround(original_init):
#     def fake_init(self, strategy=None, *args, **kwargs):
#         from .utils import load_strategy
#         original_init(self, strategy or load_strategy(), *args, **kwargs)
#     return fake_init


# if not getattr(BaseAuth, '__init_patched', False):
#     BaseAuth.__init__ = baseauth_init_workaround(BaseAuth.__init__)
#     BaseAuth.__init_patched = True

default_app_config = 'vimeo_django.config.PythonVimeoAuthConfig'
