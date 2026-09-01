# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
Info
    Unit tests for GenEfiAppBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_efi_app.core.service.iservice import IService
from gen_efi_app.core.service.isubprocessor import ISubProcessor
from gen_efi_app.infrastructure.cli.icli import ICLI
from gen_efi_app.setup.bundle import GenEfiAppBundle


class TestGenEfiAppBundle(unittest.TestCase):

    def test_bundle_creation_and_to_dict(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        mock_service = Mock(spec=IService)
        mock_subprocessor = Mock(spec=ISubProcessor)
        mock_cli = Mock(spec=ICLI)

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=mock_service,
            subprocessor=mock_subprocessor,
            cli=mock_cli
        )

        self.assertEqual(bundle.base, mock_base)
        self.assertEqual(bundle.service, mock_service)
        self.assertEqual(bundle.subprocessor, mock_subprocessor)
        self.assertEqual(bundle.cli, mock_cli)

        bundle_dict = bundle.to_dict()
        self.assertIsInstance(bundle_dict, dict)
