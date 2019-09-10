import pytest
from .. import SplitTheTip

'''
Conditions: 
    * Should accept: int age, float annual salary, float percentage saved
    * Should return what age savings goal will be met.
'''

# Case Given
def test1(applet=SplitTheTip.SplitTheTip()):
    test_result = applet.split_tip(15.16, 3)
    assert test_result  == [5.05, 5.05, 5.06]

# Case of 0 total amount
def test2(applet=SplitTheTip.SplitTheTip()):
    test_result = applet.split_tip(0, 3)
    assert test_result == [0, 0, 0]




applet = SplitTheTip.SplitTheTip()
test1(applet)
test2(applet)