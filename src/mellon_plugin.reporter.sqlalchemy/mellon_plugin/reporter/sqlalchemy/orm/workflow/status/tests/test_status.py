import os.path
import unittest
import zope.testrunner
from sparc.testing.fixture import test_suite_mixin

from ..testing import MELLON_SA_ORM_WORKFLOW_STATUS_RUNTIME_LAYER
from .. import IConfiguredAssignablesStatuses
from zope import component


class MellonOrmWorkflowStatusTestCase(unittest.TestCase):
    layer = MELLON_SA_ORM_WORKFLOW_STATUS_RUNTIME_LAYER
    
    def test_status(self):
        #verify we can read available statuses from utility appropriately
        items = list(component.getUtility(IConfiguredAssignablesStatuses).items())
        self.assertEquals(items[0][1], 'token_1')


class test_suite(test_suite_mixin):
    layer = MELLON_SA_ORM_WORKFLOW_STATUS_RUNTIME_LAYER
    package = 'mellon_plugin.reporter.sqlalchemy.orm.workflow.status'
    module = 'status'
    
    def __new__(cls):
        suite = super(test_suite, cls).__new__(cls)
        suite.addTest(unittest.makeSuite(MellonOrmWorkflowStatusTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])