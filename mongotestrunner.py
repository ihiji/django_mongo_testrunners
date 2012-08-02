from django.test.simple import DjangoTestSuiteRunner
from django.test import TransactionTestCase
from django.conf import settings

MONGO_DB = settings.MONGO_DB
DUMP_DIR = settings.DUMP_DIR

_running_test = False
from subprocess import call

class TestRunner(DjangoTestSuiteRunner):
    def setup_databases(self, **kwangs):
        global _running_test
        _running_test = True
        
        print 'Creating test-database: ' + MONGO_DB
        print 'restoring default data'
        call(["mongorestore", "--db", MONGO_DB, DUMP_DIR])
        return MONGO_DB
    
    def teardown_databases(self, db_name, **kwargs):
        from pymongo import Connection
        conn = Connection()
        conn.drop_database(db_name)
        print 'Dropping test-database: ' + db_name


class TestCase(TransactionTestCase):
    def _fixture_setup(self):
        pass
