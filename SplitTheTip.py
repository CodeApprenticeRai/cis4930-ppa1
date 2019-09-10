import math
from utilities import isfloat

class SplitTheTip:
    def command_line_routine(self):
        print("You've selected the function: SPLIT THE TIP")
        while (True):
            dinner_total = input("Enter a dinner total: ")

            if isfloat((dinner_total)):
                dinner_total = float(dinner_total)
                break
            else:
                print("Dinner total must be a float.")

        while (True):
            number_of_guests = input("Enter the number of guests: ")

            if number_of_guests.isdigit():
                number_of_guests = int(number_of_guests)
                break
            else:
                print("Number of guests must be an integer")

        distributed_tips = self.split_tip(dinner_total, number_of_guests)
        print("The split tips are {}\n\n".format(distributed_tips))
        return None

    def split_tip(self, dinner_total, number_of_guests):
        remaining_total = dinner_total
        distributed_tips = []
        for i in range( number_of_guests - 1 ):
            distributed_tip = round( dinner_total / number_of_guests, 2 )
            distributed_tips.append( distributed_tip  )
            remaining_total -= distributed_tip

        distributed_tips.append( round( remaining_total, 2 ) )

        return distributed_tips
