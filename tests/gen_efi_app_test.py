# -*- coding: UTF-8 -*-

'''
Module
    gen_efi_app_test.py
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
    Defines class GenEfiAppTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenEfiApp.
Execute
    python3 -m unittest -v gen_efi_app_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from gen_efi_app import GenEfiApp
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/gen_efi_app'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__: str = '1.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class GenEfiAppTestCase(TestCase):
    '''
        Defines class GenEfiAppTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenEfiApp.
        GenEfiApp unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_missing_args - Missing args.
                | test_process - Generate project.
                | test_pro_already_exists - Generate already existing project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenEfiApp = GenEfiApp()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Missing args'''
        sys.argv.clear()
        generator: GenEfiApp = GenEfiApp()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, '-d')
        sys.argv.insert(1, 'wrong')
        generator: GenEfiApp = GenEfiApp()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'latest')
        generator: GenEfiApp = GenEfiApp()
        self.assertTrue(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Generate already existing project'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'fresh_new')
        generator: GenEfiApp = GenEfiApp()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
