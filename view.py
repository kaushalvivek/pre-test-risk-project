'''
VIEW

All fuctions that print information to the end-user are here.
Fucntions that take an input from the end-user are also here.
All functions here are either internally called, or called by the controller or main module.
Function names are self-explanatory.

Imported by main.
'''

import os
import random
import model

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
    print ("#"*158+"\n")
    model.name =     input ("Enter Your Name            : ")
    model.email =    input ("Enter Your email Address   : ")
    model.age =      input ("Enter Your Age             : ")
    model.branch =   input ("Enter Your Branch          : ")
    print("")
    model.mode =     int(input ("Enter mode as told     : "))
    model.scenario = int(input ("Enter scenario as told : "))
    return

def print_progress () :
    '''
    Will print the following information:
    - Current Net Worth
    - Number of times fired
    - Turn number
    '''
    os.system("clear")
    print ("\nNo. of times fired : "+str(model.fired_count))
    print ("Current Net Salary   : "+str(model.net_salary))
    print ("")
    return

def print_cutoff () :
    '''
    Prints the performance Cutoff for the year.
    '''
    print ("\n Your Performance Score for the year is : "+str(model.cutoff_score[model.iteration])+"\n")
    return


def print_jobs() :
    '''
    Will print company information, name
    Salary offered
    '''
    print ("-"*60)
    print ("JOB OFFER 1 :") 
    print ("-"*60+"\n")
    if model.co_flag :
        print ("Company               : " +str(model.company[model.lj_co[-1]]))
    print ("Annual Salary Offered : " + "$"+'{:6,.0f}'.format(model.lj_sal[-1]))
    print ("Performance Cutoff    : " + str(model.lj_req[-1]))
    print ("\n"+"-"*60)
    print ("JOB OFFER 2 :")
    print ("-"*60+"\n")
    if model.co_flag :
        print ("Company               : " +str(model.company[model.hj_co[-1]]))
    print ("Annual Salary Offered : " + "$"+'{:6,.0f}'.format(model.hj_sal[-1]))
    print ("Performance Cutoff    : " + str(model.hj_req[-1])+"\n")
    print ("-"*60+"\n")
    return

def print_final ():
    '''
    The final message printed
    '''
    os.system("clear")
    print ("Game Over")
    return

def take_input () :
    '''
    Input taken for job preference
    '''
    while(True):
        val = input ("Which job are you going to choose?\nEnter 1 for first, 2 for second : ")
        if val  == '1' or val == '2' :
            model.choice = int(val)
            break
        else:
            print("\nPlease enter a valid response\n")
    return

def print_feedback () :
    '''
    Feedback on result of previous job offer.
    '''
    print_progress()
    print_cutoff()
    if model.fired_flag == 1:
        print ("Your performance score was not up to the mark, you've been fired.")
    else:
        print ("You made it through the year! Congratulations!")
    model.fired_flag = 0
    input("Press any key to continue")
    return