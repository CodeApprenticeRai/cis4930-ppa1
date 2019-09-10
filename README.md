# cis4930-ppa1 Project Report / Documentation 
This README.md file summarizes and provides documentation for 
Professional Practice Assignment 1 of CIS4930 Software Testing for Continuous Delivery. 

## Quick Start
Basic Setup 
1. Install python 3
2. Clone this repository `git clone https://github.com/CodeApprenticeRai/cis4930-ppa1.git`
3. Change into project directory 
4. Install pytest `pip install pytest`

Run command line application:   
1. `python main.py`  

Test all functions:  
1. change into `/tests` from the root directory: `cd /tests`
2. Run `pytest`

## Functions Tested

#### Retirement  
There are three tests on the Retirement function: 
* Test on the case of age already being 100  
* Test on the case of goal being a year away
* Test on the case of not already having met goal

Constraints: The constraints are given for the function through the 
problem definition.  
Completeness of Tests: The set of tests test the extemes of the domain,
and then a random number in the domain.   


#### Shortest Distance  
There are three tests on the Shortest Distance function: 
* Test on the case of calculating the distance between points with the same coordinates
* Test on the case of calculating the distance between a point and an invalid point (a value of a coordinate is infinity)
* Test on the case of calculating the case where both points given do not have any extreme values

Constraints: The domain is (-inf, inf)
Completeness of Tests: The set of tests test the extemes of the domain,
and then a random number in the domain.   

#### Email Verifier
There are four tests on the Email Verifier function: 
* Test on the case of the email string being an empty string
* Test on the case of the email string being invalid because of a type of definitional constraint: beginning with a period.
* Test on the case of the email string being invalid because of a type of definitional constraint: non-domain part of sub-string ending with a period.
* Test on the case of a valid email string

Constraints: The constraints are given for the function through the 
problem definition.  
Completeness of Tests: The tests written, are tests on the constraints dictated by the problem definition.

#### Split the Tip
There are two tests on the Email Verifier function: 
* Test on the case given in the function description 
* Test on the extreme case where the total amount to split is 0


Constraints: The domain of the function is  [ 0, inf ).  
Completeness of Tests: The tests written, are tests on the constraints dictated by the problem definition.


## Naming and Organizational Conventions  
The command line app is written in the `/main.py` file,
and when this file is ran by ```python main.py``` the command line application will run as
specified in the assignment prompt.  

Each function is found within a class that is named in correspondence to the name used in the assignment
prompt. E.g. :
The follow is a an interface of the file: cis4930_ppa1/EmailVerifier.py

```
 class EmailVerifier:
    def command_line_routine(self): 
        pass 
        
    def verify_email(self, email):
        pass
```

Each of these classes implement `command_line_routine()`, which is a command line input routine that
 requests of the user to input the arguments for the function, and then runs the function on the input data. 

##### Tests  
Tests can be found in `cis4930-ppa1/tests` folder. Test are implemented using the pytest module. Each test is a function that is of the form `textX(app)`
where the X is an incremental number starting at 1. Run all tests by changing in tho the `cis4930-ppa1/tests` folder,
and then running the command `pytest` into the terminal prompt. This will run all tests on all functions,
and return a report of it.

##### Setup
See 'Quick Start' section for setup instructions. 

## Test Results
   * Screenshots / Report goes here.
   * Screencast of RGR of Test First Proces for Each function goes here
   * Screencast of command line application goes here 
## Test Coverage Report

