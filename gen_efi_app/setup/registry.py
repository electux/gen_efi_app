# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_efi_app components for simplification of bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_efi_app.core.service.iservice import IService
from gen_efi_app.core.service.isubprocessor import ISubProcessor
from gen_efi_app.infrastructure.cli.icli import ICLI
from gen_efi_app.setup.bundle import GenEfiAppBundle
from gen_efi_app.setup.validator import GenEfiAppBundleValidator
from gen_efi_app.setup.keys import GenEfiAppBundleKeys
from gen_efi_app.setup.dependencies import GenEfiAppBundleDependencies
from gen_efi_app.setup.dep_validator import GenEfiAppBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://electux.github.io/gen_efi_app'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__ = '1.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenEfiAppBundleRegistry:
    '''
        Encapsulates core gen_efi_app components for simplification of bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_efi_app bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenEfiAppBundleDependencies) -> GenEfiAppBundle:
        '''
            Creates the gen_efi_app bundle.

            :param dependencies: The gen_efi_app bundle dependencies.
            :return: The gen_efi_app bundle.
            :exceptions:
                | ATSValueError: The gen_efi_app bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_efi_app bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_efi_app bundle must be provided and have proper values.
                | ATSTypeError:  The gen_efi_app bundle must be an instance of GenEfiAppBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenEfiAppBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenEfiAppBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenEfiAppBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(
            GenEfiAppBundleKeys.DEPENDENCY_SUBPROCESSOR
        ) if dependencies else None
        cli: ICLI | None = dependencies.get(GenEfiAppBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenEfiAppBundle = GenEfiAppBundle(
            base=base, service=service, subprocessor=subprocessor, cli=cli
        )

        GenEfiAppBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
