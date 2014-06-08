#!/usr/bin/env python

from setuptools import setup

setup(
    name='mezzanine-openshift',
    version='1.2',
    description='Mezzanine configured for deployment on OpenShift.',
    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',
    url='http://isaacbythewood.com/',
    install_requires=[
        'Django==1.6.5',
        'psycopg2==2.5.3', # important as Openshift default is the older 2.0.4 version throwing errors
        'mezzanine==3.1.4',
        'django_compressor==1.4',
        'cartridge',
        'mezzanine-slides',
    ],
)
