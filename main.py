'''
    Develop a command line app that prompts the user to select a function to execute, provide input, get a correct response, select another function *or* allow the user to gracefully exit the app.
    The menu should be displayed after each function unless the user exits.
    Apply Test / Behavior-Driven Development to implement the command line app.
    The unit test coverage for the application should be greater than 85%.
'''
'''
    * prompts user to select a function to execute
    * select another function
    * allow user to gracefully exit
'''

from Retirement import Retirement
from ShortestDistance import ShortestDistance
from EmailVerifier import EmailVerifier
from SplitTheTip import SplitTheTip


class Assignment1:
    def __init__(self):
        self.function_choices = {
            1: Retirement(),
            2: ShortestDistance(),
            3: EmailVerifier(),
            4: SplitTheTip()
        }

    def run_a_function_routine(self):
        while (True):
            print("Please select which function you would like to execute:")
            print("\t1. Retirement", "\t2. Shortest Distance", "\t3. Email Verifier", "\t4. Split the Tip",  sep="\n")
            choice = input("Choice: ")

            if((not choice.isdigit()) or (int(choice) > 4) or (int(choice) <= 0)):
                print("Please enter an integer corresponding to the choices shown")

            else:
                choice = int(choice)
                self.function_choices[choice].command_line_routine()
                break

    def main(self):
        while(True):
            print("{} Welcome to Professional Practice Assignment 1 Function Tester! {}\n\n".format("*"*5, "*"*5))
            print("Please select an action from the below list: ")
            print("\t1. Execute a Function","\t2. Exit", sep="\n")
            choice = input("Choice: ")
            print("\n\n")
            if ( ( not choice.isdigit() ) or ( int(choice) > 2 ) or ( int(choice) <= 0 ) ):
                print("Please enter an integer corresponding to the choices shown")

            else:
                choice = int(choice)
                if ( choice == 1 ):
                    self.run_a_function_routine()
                else:
                    return None

### Driver Code
app = Assignment1()
app.main()
