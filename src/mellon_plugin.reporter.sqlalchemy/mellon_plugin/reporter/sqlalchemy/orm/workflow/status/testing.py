from mellon.testing import MellonApplicationRuntimeLayer
import mellon_plugin.reporter.sqlalchemy

class MellonOrmRuntimeWorkflowStatusLayer(MellonApplicationRuntimeLayer):
    def setUp(self):
        self.config = \
            {
             'MellonWorkflowSecretAssignableStatuses':
                [
                    {'token': 'token_1',
                     'value': u'title 1',
                     'description': u'description 1'},
                    {'token': 'token_2',
                     'value': u'title 2',
                     'description': u'description 2'},
                 ],
             'ZCMLConfiguration':
                [
                    {'package':'mellon_plugin.reporter.sqlalchemy.orm.workflow'}
                ]
            }
        super(MellonOrmRuntimeWorkflowStatusLayer, self).setUp()
MELLON_SA_ORM_WORKFLOW_STATUS_RUNTIME_LAYER = MellonOrmRuntimeWorkflowStatusLayer(mellon_plugin.reporter.sqlalchemy)