# -*- coding: UTF-8 -*-

'''
Module
    gen_efi_command_test.py
Info
    Unit tests for GenEfiCommandDefinition and GenEfiCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_efi_app.core.service.iservice import IService
from gen_efi_app.infrastructure.command.gen_efi_command_definition import GenEfiCommandDefinition
from gen_efi_app.infrastructure.command.gen_efi_command_executor import GenEfiCommandExecutor
from gen_efi_app.infrastructure.command.command import CommandBundle


class TestGenEfiCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenEfiCommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate EFI application project files')
        self.assertEqual(len(definition.options), 2)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenEfiCommandDefinition()
        executor = GenEfiCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}

        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)

        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenEfiCommandDefinition()
        executor = GenEfiCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False

        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenEfiCommandDefinition()
        executor = GenEfiCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = GenEfiCommandDefinition()
        executor = GenEfiCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)

    def test_command_bundle(self) -> None:
        definition = GenEfiCommandDefinition()
        executor = GenEfiCommandExecutor(definition)
        bundle = CommandBundle(definition=definition, executor=executor)
        self.assertEqual(bundle.definition, definition)
        self.assertEqual(bundle.executor, executor)
