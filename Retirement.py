from .utilities import isfloat

class Retirement:
    def command_line_routine(self):
        print("You've selected the function: RETIREMENT")

        while (True):
            age = input("Enter your age: ")
            if age.isdigit():
                age = (int(age))
                break
            else:
                print("Age must be an integer.")

        while (True):
            salary = input("Enter your salary: ")
            if isfloat(salary):
                salary = (float(salary))
                break
            else:
                print("Salary must be a float/int.")

        while (True):
            percentage_saved = input("Enter the percentage you save of your salary as a float between 0-1: ")
            if isfloat(percentage_saved):
                percentage_saved = (float(percentage_saved))
                if ( ( percentage_saved > 1 ) or ( percentage_saved < 0 ) ):
                    print("Percentage saved must be a float between 0-1.")
                else:
                    break
            else:
                print("Salary must be a float/int.")

        while (True):
            savings_goal = input("Enter your savings goal: ")
            if isfloat(savings_goal):
                savings_goal = (float(savings_goal))
                break
            else:
                print("Savings goal must be a float/int.")

        retirement_age = self.calculate_when_savings_goal_reached(age, salary, percentage_saved,savings_goal)
        print("Your retirement age will be {}\n\n".format(retirement_age))
        return None

    def calculate_when_savings_goal_reached(self, age, salary, percentage_saved, savings_goal):
        capital = 0
        while ( (age < 100) and (capital < savings_goal)):
            capital += salary * percentage_saved * 1.35
            age += 1
        return age
