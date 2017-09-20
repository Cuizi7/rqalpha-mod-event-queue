# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip.req import parse_requirements


setup(
    name='rqalpha-mod-event-queue',
    version='0.0.4',
    description='A mod for RQAlpha to replace its default event bus with a queued event bus.',
    packages=find_packages(exclude=[]),
    author='cuizi7',
    author_email='cuizi7@163.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)