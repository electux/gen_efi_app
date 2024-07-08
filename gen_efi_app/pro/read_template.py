# -*- coding: UTF-8 -*-

'''
Module
    read_template.py
Copyright
    Copyright (C) 2020 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ReadTemplate with attribute(s) and method(s).
    Creates an API for reading a template files.
'''

import sys
from typing import Any, List, Dict, Optional
from os.path import dirname, realpath, isdir

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.pro_config import ProConfig
    from ats_utilities.pro_config.template_dir import TemplateDir
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://electux.github.io/gen_efi_app'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_efi_app/blob/dev/LICENSE'
__version__ = '1.3.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileCheck, TemplateDir):
    '''
        Defines class ReadTemplate with attribute(s) and method(s).
        Creates an API for reading a templatee files.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _TEMPLATE_DIR - Prefix path to templates.
            :methods:
                | __init__ - Initials ReadTemplate constructor.
                | read - Reads a templates.
    '''

    _GEN_VERBOSE: str = 'GEN_AUTOCONF::PRO::READ_TEMPLATE'
    _TEMPLATE_DIR: str = '/../conf/template/'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ReadTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileCheck.__init__(self, verbose)
        TemplateDir.__init__(self, verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init reader'])
        current_dir: str = dirname(realpath(__file__))
        pro_template_dir: str = f'{current_dir}{self._TEMPLATE_DIR}'
        if isdir(pro_template_dir):
            self.template_dir = pro_template_dir

    def read(
        self, config: Dict[Any, Any], verbose: bool = False
    ) -> List[Dict[str, str]]:
        '''
            Reads a templates.

            :param config: Project configuration
            :type config: <Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: List with templates
            :rtype: <List[Dict[str, str]]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([('dict:config', config)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(config):
            raise ATSValueError('missing templates')
        templates: List[str] = config[ProConfig.TEMPLATES]
        modules: List[str] = config[ProConfig.MODULES]
        loaded_templates: List[Dict[str, str]] = []
        for template_file, module_file in zip(templates, modules):
            template_content: Optional[str] = None
            template_file_path: str = f'{self.template_dir}{template_file}'
            self.check_path(template_file_path, verbose)
            self.check_mode('r', verbose)
            self.check_format(template_file_path, ProConfig.FORMAT, verbose)
            if self.is_file_ok():
                with open(
                    template_file_path, 'r', encoding='utf-8'
                ) as template_module:
                    template_content = template_module.read()
                    loaded_templates.append({module_file: template_content})
        return loaded_templates
