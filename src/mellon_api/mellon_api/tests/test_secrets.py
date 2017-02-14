import os.path
import unittest
import zope.testrunner

from mellon_api import testing

class MellonApiwargsTestCase(unittest.TestCase):
    layer = testing.MELLON_API_RUNTIME_LAYER
    model_count = 75
    
    def setUp(self):
        self.endpoint = "/api/secrets"
        self.layer.create_full_model(count=self.model_count)
        self.layer.session.flush()
    
    def tearDown(self):
        self.layer.session.rollback()
    
    def test_secret(self):
        json = self.layer.get_json(self.endpoint+'/secret_1')
        self.assertEquals(json['name'], 'secret 1')
    
    def test_secret_collection(self):
        json = self.layer.get_json(self.endpoint+'?results_per_page='+str(self.model_count))
        self.assertEquals(len(json['objects']), self.model_count)
    
class test_suite(object):
    layer = testing.MELLON_API_RUNTIME_LAYER
    
    def __new__(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(MellonApiwargsTestCase))
        return suite

if __name__ == '__main__':
    zope.testrunner.run([
                         '--path', os.path.dirname(__file__),
                         '--tests-pattern', os.path.splitext(
                                                os.path.basename(__file__))[0]
                         ])