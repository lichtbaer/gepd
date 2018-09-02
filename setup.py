#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of gepd.
# https://github.com/lichtbaer/dawum

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, johannes <johannes@kampagnen.eu>

from setuptools import setup, find_packages
from gepd import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='gepd',
    version=__version__,
    description='German election poll data from dawum.de',
    long_description='''
German election poll data from dawum.de
''',
    keywords='dawum.de, election, poll, german',
    author='johannes',
    author_email='johannes@kampagnen.eu',
    url='https://github.com/lichtbaer/dawum',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=["pandas", "requests"

        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'gepd=gepd.main:main'
            # add cli scripts here in this form:
            # 'gepd=gepd.cli:main',
        ],
    },
)
