import pytest, pymongo
from .. import EmailVerifier

'''
Conditions:
    * Should accept: int age, float annual salary, float percentage saved
    * Should return what age savings goal will be met.
'''

# Case of empty string
def test1(applet=EmailVerifier.EmailVerifier(), db=None):
    test_result = applet.verify_email("", db)
    assert test_result  == False

# Case of invalid email becuase of email non-domain portion of email starting with a '.'
def test2(applet=EmailVerifier.EmailVerifier(), db=None):
    test_result = applet.verify_email(".dfdsaf@gmail.com", db)
    assert test_result == False

# Case of invalid email becuase of email non-domain portion of email ending with a '.'
def test3(applet=EmailVerifier.EmailVerifier(), db=None):
    test_result = applet.verify_email("sdfsdklfj.@gmail.com", db)
    assert test_result == False

# Case of valid email
def test4(applet=EmailVerifier.EmailVerifier(), db=None):
    test_result = applet.verify_email("j.!$%*+-=?^_{|}~.smith@gmail.com", db)
    assert test_result == True

applet = EmailVerifier.EmailVerifier()

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client["function_solution_records_fake_db"]

test1(applet, db)
test2(applet, db)
test3(applet, db)
test4(applet, db)
