import pytest
from .. import Retirement

'''
Conditions: 
    * Should accept: int age, float annual salary, float percentage saved
    * Should return what age savings goal will be met.
'''

# Case of age already being 100
def test1(applet=Retirement.Retirement()):
    age = applet.calculate_when_savings_goal_reached(100, 100000, 1, 1000000)
    assert age == 100

# Case of goal being a year away
def test2(applet=Retirement.Retirement()):
    age = applet.calculate_when_savings_goal_reached(25, 1000000, 1, 1000000)
    assert age == 26

# Case of not already having met goal
def test3(applet=Retirement.Retirement()):
    age = applet.calculate_when_savings_goal_reached(25, 100000, 0.25, 1000000)
    assert age == 55

applet = Retirement.Retirement()
test1(applet)
test2(applet)
test3(applet)