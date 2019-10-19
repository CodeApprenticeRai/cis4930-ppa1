import sys
sys.path.append(".")

import pymongo, time
from utilities import isfloat

class Retirement:
    def command_line_routine(self, db=None):
        print("You've selected the function: RETIREMENT")

        print("\n\nHistory:")

        if ( type(db) == type(None) ):
            db_client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = db_client["function_solution_records"]

        collection = db["records"]

        # TODO: Clean this up.
        print("Starting Age", "Salary", "Percentage Saved", "Savings Goal", "Solution", "Time", sep="\t")
        for record in collection.find({ "function_name": "Retirement"}):
            print(
                record["parameters"]["starting_age"],
                record["parameters"]["salary"],
                record["parameters"]["percentage_saved"],
                record["parameters"]["savings_goal"],
                record["solution"], record["time"],
                sep="\t" )

        print( "*"*5, "End of History", "*"*5, "\n\n", sep="" )

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

    def calculate_when_savings_goal_reached(self, starting_age, salary, percentage_saved, savings_goal, db=None, mock=None, stub=None):
        capital = 0
        age = starting_age
        while ( (age < 100) and (capital < savings_goal)):
            capital += salary * percentage_saved * 1.35
            age += 1

        current_unix_time = int( time.time() )
        if ( type(db) == type(None) ):
            db_client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = db_client["function_solution_records"]

        collection = db["records"]

        data = {
            "function_name": "Retirement",
            "time": current_unix_time,
            "parameters": {
                "starting_age": starting_age,
                "salary": salary,
                "percentage_saved": percentage_saved,
                "savings_goal": savings_goal
            },
            "solution": age
        }
    
        if mock:
            mock.store( "transactions", [data] )

        if stub:
            stub.store( "solution_that_would_have_been_sent_to_db", data["solution"] )



        if ( collection.find_one( data["parameters"] ) == None ): #avoid duplicate records
            collection.insert_one(data)

        return age

if __name__ == "__main__":
    retirement_calculator = Retirement()
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = db_client["function_solution_records"]

    starting_age = int(sys.argv[1])
    salary = float(sys.argv[2])
    percentage_saved = float(sys.argv[3])
    savings_goal = float(sys.argv[4])


    print( retirement_calculator.calculate_when_savings_goal_reached(starting_age, salary, percentage_saved, savings_goal, db ), sep="", end="" )
    sys.stdout.flush()
