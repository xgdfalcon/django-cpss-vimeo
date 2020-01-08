#! /usr/bin/env python
# encoding: utf-8
from os.path import join, dirname

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='vimeo-django',
    version='0.1.0',
    author='Larry Latouf (XGDFalcon®)',
    author_email='xgdfalcon@gmail.com',
    description='Vimeo API, Django integration.',
    license='APACHE',
    keywords='django, vimeo',
    url='https://github.com/CPSSw/django-vimeo',
    packages=[
        'vimeo_django',
        'vimeo_django.migrations',
    ],
    long_description='This is the Django component of the PyVimeo project, it implements the needed functionality to integrate PyVimeo in a Django based project',
    install_requires=['PyVimeo>=1.0.11'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet',
        'License :: OSI Approved :: Apache License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False
)