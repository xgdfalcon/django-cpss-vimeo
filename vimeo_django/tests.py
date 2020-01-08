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
from vimeo_django.models.client import VimeoClientOption

CLIENT_SECRET = "<your-client-secret>"
CLIENT_ID = "<your-client-id>"
ACCESS_TOKEN = "<your-access-token>"
USER_ID = "<your-user-id>"
PROJECT_ID = "<target-project-id>"

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
        

