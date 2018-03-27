#!/usr/bin/env python
import os
from setuptools import setup


with open(os.path.join('README.md'), 'r') as f:
    long_description = f.read()


setup(
    name='simple-config',
    version='1.0.0',
    description='A simple configuration file manager for python',
    long_description=long_description,
    author='keshaB Paudel',
    author_email='self@keshab.net',
    url='https://github.com/poudel/simple-config',
    py_modules=['simple_config'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    keywords='config json-config user-config'
)
