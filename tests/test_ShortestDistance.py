import pytest
from .. import ShortestDistance

'''
Conditions: 
    * Should accept: int age, float annual salary, float percentage saved
    * Should return what age savings goal will be met.
'''

# identity distance
def test1(applet=ShortestDistance.ShortestDistance()):
    _distance = applet.distance((0,0), (0,0))
    assert _distance  == 0

# Case of comparison to infinity distance
def test2(applet=ShortestDistance.ShortestDistance()):
    _distance = applet.distance((0,0), (0, float("inf")))
    assert _distance == float('inf')

# Case of comparison between two non-extreme numbers
def test3(applet=ShortestDistance.ShortestDistance()):
    _distance = applet.distance((1, 4), (5, 4))
    assert _distance == 4

applet = ShortestDistance.ShortestDistance()
test1(applet)
test2(applet)
test3(applet)