# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenEfiAppBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_efi_app.setup.keys import GenEfiAppBundleKeys


class TestGenEfiAppBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenEfiAppBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenEfiAppBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenEfiAppBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenEfiAppBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenEfiAppBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenEfiAppBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenEfiAppBundleKeys.OPTION_INFO_FILE, opts)
