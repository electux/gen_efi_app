# -*- coding: UTF-8 -*-

'''
Module
    gen_efi_app_pro_test.py
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
    Defines class GenEfiTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenEfi.
Execute
    python3 -m unittest -v gen_efi_app_pro_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_efi_app.pro import GenEfi
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


class GenEfiTestCase(TestCase):
    '''
        Defines class GenEfiTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenEfi.
        GenEfi unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_get_reader - Is reader ok.
                | test_get_writer - Is writer ok.
                | test_gen_project_empty - Create project with missing name.
                | test_gen_project_none - Create project with None name.
                | test_gen_project - Create project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenEfi = GenEfi()
        self.assertIsNotNone(generator)

    def test_get_reader(self) -> None:
        '''Is reader ok'''
        generator: GenEfi = GenEfi()
        self.assertIsNotNone(generator.get_reader())

    def test_get_writer(self) -> None:
        '''Is writer ok'''
        generator: GenEfi = GenEfi()
        self.assertIsNotNone(generator.get_writer())

    def test_gen_project_empty(self) -> None:
        '''Create project with missing name'''
        generator: GenEfi = GenEfi()
        with self.assertRaises(ATSValueError):
            generator.gen_project("")

    def test_gen_project_none(self) -> None:
        '''Create project with None name'''
        generator: GenEfi = GenEfi()
        with self.assertRaises(ATSTypeError):
            generator.gen_project(None)  # type: ignore

    def test_gen_project(self) -> None:
        '''Create project'''
        generator: GenEfi = GenEfi()
        self.assertTrue(generator.gen_project('full_simple'))


if __name__ == '__main__':
    main()
