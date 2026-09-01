# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Defines the gen_efi_app bundle.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.utils.reflection import instance_to_dict

from gen_efi_app.core.service.iservice import IService
from gen_efi_app.core.service.isubprocessor import ISubProcessor
from gen_efi_app.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://electux.github.io/gen_efi_app'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__ = '1.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(slots=True, frozen=True, kw_only=True)
class GenEfiAppBundle:
    '''
        GenEfiApp bundle holding the components of the gen_efi_app.

        It defines:

            :attributes:
                | base - The base bundle with the base components.
                | service - The service orchestrating the gen_efi_app execution.
                | subprocessor - The adapter executing the gen_efi_app sub-processes.
                | cli - The command-line interface adapter.
            :methods:
                | to_dict - Converts the gen_efi_app bundle to a dictionary.
    '''

    base: BaseBundle
    service: IService
    subprocessor: ISubProcessor
    cli: ICLI

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the gen_efi_app bundle to a dictionary.

            :return: Dictionary representation of the gen_efi_app bundle.
            :exceptions: None.
        '''
        return instance_to_dict(self)
