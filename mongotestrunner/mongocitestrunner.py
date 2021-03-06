from django_jenkins.runner import CITestSuiteRunner
from django.test import TransactionTestCase
from django.conf import settings
from mongoengine.connection import connect, disconnect, get_connection

MONGO_DB = settings.MONGO_DB
DUMP_DIR = settings.DUMP_DIR

_running_test = False
from subprocess import call

class TestRunner(CITestSuiteRunner):
    def setup_databases(self, **kwangs):
        global _running_test
        _running_test = True
        disconnect()
        connect(MONGO_DB)
        print 'Creating test-database: ' + MONGO_DB
        print 'restoring default data'
        call(["mongorestore", "--db", MONGO_DB, DUMP_DIR])
        return MONGO_DB
    
    def teardown_databases(self, db_name, **kwargs):
        connection = get_connection()
        connection.drop_database(MONGO_DB)
        disconnect()
        print 'Dropping test-database: ' + db_name


class TestCase(TransactionTestCase):
    def _fixture_setup(self):
        pass
