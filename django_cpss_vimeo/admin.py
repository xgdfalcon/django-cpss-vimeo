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

from itertools import chain

from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models.client import VimeoClientOption

@admin.register(VimeoClientOption)
class VimeoOptionAdmin(admin.ModelAdmin):
    list_display = ('vimeo_project_id', 'site', 'vimeo_user_id')
    list_filter = ('site',)
    list_select_related = True

    @staticmethod
    def _get_all_field_names(model):
        names = chain.from_iterable(
            (field.name, field.attname)
                if hasattr(field, 'attname') else (field.name,)
            for field in model.get_fields()
            # For complete backwards compatibility, you may want to exclude
            # GenericForeignKey from the results.
            if not (field.many_to_one and field.related_model is None)
        )
        return list(set(names))

