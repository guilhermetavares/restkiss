#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='restkiss',
    version='2.0.2',
    description='A lightweight REST miniframework for Python.',
    author='Bruno Marques',
    author_email='bruno@cravefood.services',
    url='http://github.com/CraveFood/restkiss',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'restkiss',
    ],
    requires=[
        'six(>=1.4.0)',
    ],
    install_requires=[
        'six>=1.4.0',
    ],
    tests_require=[
        'mock',
        'tox',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Flask',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
