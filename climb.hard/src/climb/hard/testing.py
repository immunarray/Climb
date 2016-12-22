# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import climb.hard


class ClimbHardLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=climb.hard)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'climb.hard:default')


CLIMB_HARD_FIXTURE = ClimbHardLayer()


CLIMB_HARD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CLIMB_HARD_FIXTURE,),
    name='ClimbHardLayer:IntegrationTesting'
)


CLIMB_HARD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CLIMB_HARD_FIXTURE,),
    name='ClimbHardLayer:FunctionalTesting'
)


CLIMB_HARD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CLIMB_HARD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ClimbHardLayer:AcceptanceTesting'
)
