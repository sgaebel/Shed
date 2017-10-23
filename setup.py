#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='shed',
      version='0.1',
      description='Assorted Python Tools and Snippets',
      author='Sebastian M. Gaebel',
      author_email='sebastian.gaebel@ligo.org',
      license='WTFNMFPL',
      url='https://github.com/sgaebel/GAPS',
      packages=['shed'],
      install_requires=['numpy', 'matplotlib', 'scipy'])

