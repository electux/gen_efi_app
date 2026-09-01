# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_efi_app bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_efi_app.setup.bundle import GenEfiAppBundle
from gen_efi_app.setup.options import GenEfiAppBundleOptions
from gen_efi_app.setup.registry import GenEfiAppBundleRegistry
from gen_efi_app.setup.dependencies import GenEfiAppBundleDependencies
from gen_efi_app.setup.opt_validator import GenEfiAppBundleOptionsValidator
from gen_efi_app.setup.keys import GenEfiAppBundleKeys
from gen_efi_app.core.service.engine import Service
from gen_efi_app.infrastructure.subprocessor import SubProcessor
from gen_efi_app.infrastructure.cli.engine import CLI
from gen_efi_app.infrastructure.cli.setup.bundle import CLIBundle
from gen_efi_app.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_efi_app.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_efi_app.infrastructure.command.command import CommandBundle
from gen_efi_app.infrastructure.command.gen_efi_command_definition import GenEfiCommandDefinition
from gen_efi_app.infrastructure.command.gen_efi_command_executor import GenEfiCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://electux.github.io/gen_efi_app'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__ = '1.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenEfiAppBundleFactory:
    '''
        Factory for creating the gen_efi_app bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_efi_app info file.
            :methods:
                | create_bundle - Creates the gen_efi_app bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = 'gen_efi_app/infrastructure/config/gen_efi_app.cfg'

    @classmethod
    def create_bundle(cls, options: GenEfiAppBundleOptions | None = None) -> GenEfiAppBundle:
        '''
            Creates the gen_efi_app bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_efi_app bundle.
            :return: The gen_efi_app bundle.
            :exceptions:
                | ATSValueError: The gen_efi_app bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_efi_app bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_efi_app bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_efi_app bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_efi_app bundle must be provided and have proper values.
                | ATSTypeError:  The gen_efi_app bundle must be an instance of GenEfiAppBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenEfiAppBundleOptionsValidator.validate(options)

        info_file = options.get(GenEfiAppBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_efi_definition: GenEfiCommandDefinition = GenEfiCommandDefinition()

        gen_efi_bundle: CommandBundle = CommandBundle(
            definition=gen_efi_definition,
            executor=GenEfiCommandExecutor(gen_efi_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_efi_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenEfiAppBundleRegistry.create_bundle(
            dependencies=GenEfiAppBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
