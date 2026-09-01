# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenEfiAppBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_efi_app.setup.bundle import GenEfiAppBundle
from gen_efi_app.setup.factory import GenEfiAppBundleFactory


class TestGenEfiAppBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenEfiAppBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenEfiAppBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_efi_app/infrastructure/config/gen_efi_app.cfg'}
        bundle = GenEfiAppBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenEfiAppBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenEfiAppBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenEfiAppBundleFactory.get_version(), '1.3.7')
