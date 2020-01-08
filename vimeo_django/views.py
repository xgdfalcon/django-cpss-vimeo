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

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models.client import VimeoClientOption

# @login_required
def get_project(request, project_id):
    collection_instance = get_object_or_404(VimeoClientOption, vimeo_project_id=project_id)
    return HttpResponse(collection_instance.get_folder_contents())

