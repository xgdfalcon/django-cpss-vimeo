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

from django.conf import settings
from vimeo import VimeoClient as VimeoClientBase
from django.contrib.sites.models import Site
from django.utils.translation import gettext as _
from django.db import models
from vimeo import VimeoClient
from .vimeo import CPSSVimeoCollectionType
import uuid


class VimeoClientManager(models.Manager):
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class VimeoClientType(models.Model):
    id = models.UUIDField(verbose_name=_("ID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    vimeo_user_id = models.CharField(
        verbose_name=_("Vimeo User ID"), max_length=100, default="")
    vimeo_client_id = models.CharField(
        verbose_name=_("Vimeo Client ID"), max_length=100, default="")
    vimeo_client_secret = models.CharField(
        verbose_name=_("Vimeo Client Secret"), max_length=100, default="")
    vimeo_access_token = models.CharField(
        verbose_name=_("Vimeo Access Token"), max_length=100, default="")
    vimeo_project_id = models.CharField(
        verbose_name=_("Vimeo Project ID/Folder ID"), unique=True, max_length=100, default="")
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, verbose_name=_('Site'), blank=True)

    class Meta:
        abstract = True


class VimeoClientOption(VimeoClientType):
    objects = VimeoClientManager()

    class Meta:
        db_table = 'vimeo_django_settings'
        verbose_name = _('CPSS Vimeo Client Setting')
        verbose_name_plural = _('CPSS Vimeo Client Settings')

    def __str__(self):
        return str(self.site.domain) + ": " + str(self.vimeo_project_id)

    def get_folder_contents(self):
        v = VimeoClient(
            token=self.vimeo_access_token,
            key=self.vimeo_client_id,
            secret=self.vimeo_client_secret
        )
        response = v.get('/users/' + self.vimeo_user_id +
                         '/projects/' + self.vimeo_project_id + '/videos')
        assert response.status_code == 200
        return CPSSVimeoCollectionType(response.json())

