import pytest, pymongo
from .. import Retirement
from . import DatabaseDouble


def test4(applet=Retirement.Retirement(), db=None ):
    mock = DatabaseDouble.DatabaseDouble()
    applet.calculate_when_savings_goal_reached(100, 100000, 1, 1000000, db, mock=mock)
    assert len( mock.retrieve( "transactions" ) ) == 1

def test5(applet=Retirement.Retirement(), db=None, mock=None):
    stub = DatabaseDouble.DatabaseDouble()
    stub.store( "stub_solution1", 100 )

    applet.calculate_when_savings_goal_reached(100, 100, 1, 1000000, db, mock=mock, stub=stub)
    assert stub.retrieve( "solution_that_would_have_been_sent_to_db" )  == stub.retrieve( "stub_solution1")

def test6(applet=Retirement.Retirement(), db=None, mock=None):
    stub = DatabaseDouble.DatabaseDouble()
    stub.store( "stub_solution2", 24 )

    applet.calculate_when_savings_goal_reached(23, 1000000, 1, 1000000, db, mock=mock, stub=stub)
    assert stub.retrieve( "solution_that_would_have_been_sent_to_db" )  == stub.retrieve("stub_solution2")

def test7(applet=Retirement.Retirement(), db=None, mock=None):
    stub = DatabaseDouble.DatabaseDouble()
    stub.store( "stub_solution3", 55 )

    applet.calculate_when_savings_goal_reached(25, 100000, 0.25, 1000000, db, mock=mock, stub=stub)
    assert stub.retrieve( "solution_that_would_have_been_sent_to_db" )  == stub.retrieve( "stub_solution3")


db_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = db_client["function_solution_records_fake_db"]

mock = DatabaseDouble.DatabaseDouble()

applet = Retirement.Retirement()


test4(applet, db=db)
test5(applet, db, mock=mock)
test6(applet, db, mock=mock)
test7(applet, db, mock=mock)
