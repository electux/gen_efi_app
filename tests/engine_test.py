# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
Info
    Unit tests for GenEfiApp engine.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSValueError

from gen_efi_app.engine import GenEfiApp
from gen_efi_app.setup.bundle import GenEfiAppBundle
from gen_efi_app.setup.factory import GenEfiAppBundleFactory
from gen_efi_app.core.service.iservice import IService
from gen_efi_app.core.service.isubprocessor import ISubProcessor
from gen_efi_app.infrastructure.cli.icli import ICLI


class DummyService(IService):

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'DummyService'


class DummySubProcessor(ISubProcessor):

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'DummySubProcessor'


class DummyCLI(ICLI):

    def __init__(self, return_code: int = 0, stderr: str = '') -> None:
        self.return_code = return_code
        self.stderr = stderr

    def run(self) -> dict[str, object]:
        return {'returncode': self.return_code, 'stderr': self.stderr}

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'DummyCLI'


class TestGenEfiApp(unittest.TestCase):

    def test_engine_init_success(self) -> None:
        bundle = GenEfiAppBundleFactory.create_bundle()
        engine = GenEfiApp(bundle)
        self.assertTrue(engine.is_initialized())

    def test_engine_init_fail_validation(self) -> None:
        engine = GenEfiApp(None)
        self.assertFalse(engine.is_initialized())

    def test_engine_process_success(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_efi_app/infrastructure/config/gen_efi_app.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI(return_code=0)

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenEfiApp(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertTrue(engine.process())

    def test_engine_process_cli_failure(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_efi_app/infrastructure/config/gen_efi_app.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI(return_code=1, stderr='CLI error')

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenEfiApp(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_not_initialized(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_efi_app/infrastructure/config/gen_efi_app.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        mock_base.option_manager.is_initialized = Mock(return_value=False)

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenEfiApp(bundle)
        self.assertFalse(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_exception(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_efi_app/infrastructure/config/gen_efi_app.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()

        dummy_cli = DummyCLI()
        dummy_cli.run = Mock(side_effect=Exception('Unexpected error'))

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenEfiApp(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_validation_exception(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_efi_app/infrastructure/config/gen_efi_app.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()
        dummy_cli.run = Mock(side_effect=ATSValueError('Validation error in run'))

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenEfiApp(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    @patch('gen_efi_app.setup.validator.GenEfiAppBundleValidator.validate')
    def test_engine_init_generic_exception(self, mock_validate: Mock) -> None:
        mock_validate.side_effect = Exception('Unexpected generic validation error')

        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_efi_app/infrastructure/config/gen_efi_app.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenEfiAppBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenEfiApp(bundle)
        self.assertFalse(engine.is_initialized())
