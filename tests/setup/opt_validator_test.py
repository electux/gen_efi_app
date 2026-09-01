# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenEfiAppBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_efi_app.setup.opt_validator import GenEfiAppBundleOptionsValidator


class TestGenEfiAppBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenEfiAppBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenEfiAppBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenEfiAppBundleOptionsValidator.validate("not_a_mapping")

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenEfiAppBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenEfiAppBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenEfiAppBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenEfiAppBundleOptionsValidator.is_valid({'info_file': 123}))
