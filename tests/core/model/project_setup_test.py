# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
Info
    Unit tests for ProjectSetup class.
'''

from __future__ import annotations

import unittest

from gen_efi_app.core.model.project_setup import ProjectSetup


class TestProjectSetup(unittest.TestCase):
    def test_project_setup_initialization(self) -> None:
        project_config = {'key': 'value'}
        setup = ProjectSetup(project_config=project_config)
        self.assertEqual(setup.project_config, project_config)
