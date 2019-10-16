'''
    * map all meaningless input to infinity
    * function returns distance based on distance formula
'''
from utilities import isfloat
import math

class ShortestDistance:
    def command_line_routine(self):
        print("You've selected the function: SHORTEST DISTANCE")
        while (True):

            coord = input("Enter the X coordinate for the first point: ")
            if coord.isdigit():
                point1 = [int(coord)]
                break
            else:
                print("X total must be an integer.")

        while (True):

            coord = input("Enter the Y coordinate for the first point: ")
            if coord.isdigit():
                point1.append( int(coord) )
                break
            else:
                print("X total must be an integer.")

        while (True):

            coord = input("Enter the X coordinate for the second point: ")
            if coord.isdigit():
                point2 = [int(coord)]
                break
            else:
                print("X total must be an integer.")

        while (True):

            coord = input("Enter the Y coordinate for the second point: ")
            if coord.isdigit():
                point2.append(int(coord))
                break
            else:
                print("X total must be an integer.")

        _distance = self.distance(point1, point2)
        print("The shortest distance between {} and {} is {}\n\n".format(point1, point2, _distance))
        return None

    def distance(self, point1, point2):
        if ( ( len(point1) < 2) or ( len(point2) < 2) ):
            return float('inf')
        _distance = 0
        for i in range(2):
            _distance += (point2[i] - point1[i])**(2)
        return math.sqrt( _distance )
