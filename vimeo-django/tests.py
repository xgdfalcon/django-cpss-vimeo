#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
# 

"""
This python module provides the models for the video vault application.

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.test import TestCase
from django.test.client import RequestFactory
from .models.client import VimeoClientOption
import os

CLIENT_SECRET = os.environ['CLIENT_SECRET'] 
CLIENT_ID = os.environ['CLIENT_ID'] 
ACCESS_TOKEN = os.environ['ACCESS_TOKEN'] 
USER_ID = os.environ['USER_ID'] 
PROJECT_ID = os.environ['PROJECT_ID'] 

class VimeoDjangoTestCase(TestCase):
    def setUp(self):
        VimeoClientOption.objects.create(
            vimeo_user_id=USER_ID,
            vimeo_client_id=CLIENT_ID,
            vimeo_client_secret=CLIENT_SECRET,
            vimeo_access_token=ACCESS_TOKEN,
            vimeo_project_id=PROJECT_ID)

    def test_retrieve_project(self):
        # response = self.client.get('/')
        collection = VimeoClientOption.objects.get(vimeo_project_id=PROJECT_ID)
        result = collection.get_folder_contents()
        print(result)
        

    def test_get_project(self):
        rf = RequestFactory()
        get_request = rf.get('project/'+PROJECT_ID)
        print(get_request)
        

