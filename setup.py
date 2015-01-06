#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='bzutils',
    description='''Basic utils for daily needs''',
    version='0.0.1',
    author='Ali Bozorgkhan',
    author_email='alibozorgkhan@gmail.com',
    url='https://github.com/alibozorgkhan/utils',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
