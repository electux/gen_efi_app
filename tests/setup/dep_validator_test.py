# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
Info
    Unit tests for GenEfiAppBundleDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_efi_app.setup.dep_validator import GenEfiAppBundleDependenciesValidator


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenEfiAppBundleDependenciesValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }
        GenEfiAppBundleDependenciesValidator.validate(dependencies)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenEfiAppBundleDependenciesValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenEfiAppBundleDependenciesValidator.validate("not_a_mapping")

    def test_validate_missing_dependency(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor
        }
        with self.assertRaises(Exception):
            GenEfiAppBundleDependenciesValidator.validate(dependencies)

    def test_is_valid_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }
        self.assertTrue(GenEfiAppBundleDependenciesValidator.is_valid(dependencies))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenEfiAppBundleDependenciesValidator.is_valid(None))
        self.assertFalse(GenEfiAppBundleDependenciesValidator.is_valid("not_a_mapping"))
        dependencies = {
            'base': Mock(spec=BaseBundle),
            'service': DummyService(),
            'subprocessor': DummySubProcessor()
        }
        self.assertFalse(GenEfiAppBundleDependenciesValidator.is_valid(dependencies))
