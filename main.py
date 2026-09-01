# -*- coding: UTF-8 -*-

'''
Module
    main.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Main entry point for EFI Application Generator CLI.
'''

from __future__ import annotations

from sys import exit as sys_exit

from gen_efi_app.engine import GenEfiApp
from gen_efi_app.setup.factory import GenEfiAppBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://electux.github.io/gen_efi_app'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__ = '1.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Bootstraps and runs the gen_efi_app with required adapters.

        :return: True if successful, False otherwise.
        :exceptions: None.
    '''
    gen_efi_app: GenEfiApp = GenEfiApp(GenEfiAppBundleFactory.create_bundle())

    return gen_efi_app.process()


if __name__ == '__main__':
    '''
        Entry point for gen_efi_app execution.

        :exit code: 0 if successful, 1 otherwise.
        :exceptions: None.
    '''
    sys_exit(0 if main() else 1)
