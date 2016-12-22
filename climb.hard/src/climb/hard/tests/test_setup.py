# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from climb.hard.testing import CLIMB_HARD_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that climb.hard is properly installed."""

    layer = CLIMB_HARD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if climb.hard is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('climb.hard'))

    def test_browserlayer(self):
        """Test that IClimbHardLayer is registered."""
        from climb.hard.interfaces import IClimbHardLayer
        from plone.browserlayer import utils
        self.assertIn(IClimbHardLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CLIMB_HARD_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['climb.hard'])

    def test_product_uninstalled(self):
        """Test if climb.hard is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('climb.hard'))

    def test_browserlayer_removed(self):
        """Test that IClimbHardLayer is removed."""
        from climb.hard.interfaces import IClimbHardLayer
        from plone.browserlayer import utils
        self.assertNotIn(IClimbHardLayer, utils.registered_layers())
