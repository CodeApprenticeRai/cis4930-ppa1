import pytest, pymongo
from .. import EmailVerifier
from . import DatabaseDouble


def test4(applet=EmailVerifier.EmailVerifier(), db=None ):
    mock = DatabaseDouble.DatabaseDouble()
    applet.verify_email("helloworld@gmail.com", db, mock=mock)
    assert len( mock.retrieve( "transactions" ) ) == 1

def test5(applet=EmailVerifier.EmailVerifier(), db=None, mock=None):
    stub = DatabaseDouble.DatabaseDouble()
    stub.store( "stub_solution1", False )

    applet.verify_email("", db, mock=mock, stub=stub)
    assert stub.retrieve( "solution_that_would_have_been_sent_to_db" )  == stub.retrieve( "stub_solution1")

def test6(applet=EmailVerifier.EmailVerifier(), db=None, mock=None):
    stub = DatabaseDouble.DatabaseDouble()
    stub.store( "stub_solution2", True )

    applet.verify_email("helloworld@gmail.com", db, mock=mock, stub=stub)
    assert stub.retrieve( "solution_that_would_have_been_sent_to_db" )  == stub.retrieve("stub_solution2")

def test7(applet=EmailVerifier.EmailVerifier(), db=None, mock=None):
    stub = DatabaseDouble.DatabaseDouble()
    stub.store( "stub_solution3", False )

    applet.verify_email("sdfsdklfj.@gmail.com", db, mock=mock, stub=stub)
    assert stub.retrieve( "solution_that_would_have_been_sent_to_db" )  == stub.retrieve( "stub_solution3")


db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client["function_solution_records_fake_db"]

mock = DatabaseDouble.DatabaseDouble()

applet = EmailVerifier.EmailVerifier()


test4(applet, db=db)
test5(applet, db, mock=mock)
test6(applet, db, mock=mock)
test7(applet, db, mock=mock)
