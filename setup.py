#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2020 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_efi_app is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_efi_app is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_efi_app.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/gen_efi_app'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__: str = '1.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR: str = 'gen_efi_app/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='gen_efi_app',
    version='1.3.5',
    description='EFI Application generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://electux.github.io/gen_efi_app',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='EFI, App, x86_64, Intel, generator',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_efi_app', 'gen_efi_app.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_efi_app': [
            'py.typed',
            f'{CONF}/gen_efi_app.logo',
            f'{CONF}/gen_efi_app.cfg',
            f'{CONF}/gen_efi_app_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/cflags.template',
            f'{TEMPLATE}/ldflags.template',
            f'{TEMPLATE}/makefile.template',
            f'{TEMPLATE}/main.template',
            f'{TEMPLATE}/objects.template',
            f'{TEMPLATE}/ocflags.template',
            f'{LOG}/gen_efi_app.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_efi_app_run.py'
        ]
    )]
)
