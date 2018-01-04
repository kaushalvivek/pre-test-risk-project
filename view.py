'''
VIEW

All fuctions that print information to the end-user are here.
Fucntions that take an input from the end-user are also here.
All functions here are either internally called, or called by the controller or main module.
Function names are self-explanatory.
'''

import os
import random
import model
from user import User

def print_initiate() :
    '''
    Game intro and rules printed.
    '''
    print ("#"*158)
    print ("\nHello, thank you for participating in this project.\n")
    print ("INSTRUCTIONS:-\n")
    print ("1. There will be a total of ten turns.")
    print ("2. You'll be given two job choices in each turn, you have to choose one.")
    print ("3. You'll be given a one year contract for each job.")
    print ("4. The goal is to earn as much money as possible at the end of ten turns.")
    print ("5. Each job choice given will have the following:")
    print (" "*3+"~ Name of Company")
    print (" "*3+"~ Annual Salary")
    print (" "*3+"~ Performace Required")
    print ("6. After each turn, you'll be alloted a performance score.")
    print ("7. If the performance score is below the requirement of your previous job, you'll be fined $200,000.")
    print ("8. Best of luck. 3:)\n")
    input ("Press enter to continue...")
    return

def print_data_collect () :
    '''
    User information collected, and mode-scenario specified.
    '''
    os.system("clear")
    print ("#"*158)
    User.name = input ("\nEnter Your Name: ")
    User.email = input ("Enter Your email Address: ")
    User.age = input ("Enter Your Age: ")
    User.branch = input ("Enter Your Branch: ")
    print("")
    User.mode = input ("Enter mode as told: ")
    User.scenario = input ("Enter scenario as told: ")
    return

def print_progress () :
    print ("Salary Low: " + str(model.lj_sal[-1]))
    print ("Salary High: "+str(model.hj_sal[-1])+"\n")
    print ("Req Low: "+str(model.lj_req[-1]))
    print ("Req High: "+str(model.hj_req[-1])+"\n")
    input ("")
    pass

def print_jobs () :
    pass

def print_final ():
    pass

def take_input () :
    pass