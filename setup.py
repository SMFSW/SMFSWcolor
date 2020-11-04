# -*- coding:utf-8 -*-
"""
setup.py (SMFSWcolor)
Author: SMFSW

SMFSWcolor setup file
"""

__version__ = "0.3.0"

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='SMFSWcolor',
    version=__version__,
    packages=find_packages(exclude=['build', 'contrib', 'doc', 'docs', 'tests']),
    install_requires=['numpy'],
    url='N/A',
    author='SMFSW',
    author_email='xgarmanboziax@gmail.com',
    license='Copyright (c) 2016-2018 SMFSW',
    description='various color schemes classes, low level conversions & transformations',
    keywords=['Color', 'Conversion', 'CIE', 'Color scenarios'],
    long_description=open('README.md').read(),
    classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering',

            'Natural Language :: English',

            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
    ],
)
