#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='base_model',
    version='0.1.0',
    description="Base model with uuid as primary key, and other helper fields like is_removed, removed_time, created_time, modified_time.",
    long_description=readme + '\n\n' + history,
    author="Aldiantoro Nugroho",
    author_email='kriwil@gmail.com',
    url='https://github.com/kriwil/django-base-model',
    packages=[
        'base_model',
    ],
    package_dir={'base_model':
                 'base_model'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='base_model',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)