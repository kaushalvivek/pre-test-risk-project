import os
from user import User
from state import State
from job import *
from model import *

def print_status ():
    os.system("tput reset")
    print("\n\n"+"#"*100+"\n\n"+\
    "STATE:"+str(State.state)+"\n\n"+\
    "FEEDBACK: "+str(feedback_array[State.state])+"\n\n"\
    "RECESSION:\nProbability:"+str(State.recession_probability)+"\n\n"\
    "JOB:\nTime:"+str(User.time_at_job)+"\nQuality:"+str(State.job_quality)+"\nCurrent Booming:"\
    +str(State.current_booming)+"\nSector Score:"+str(State.sector_score))
    x = input ("\nProceed\n")

def  print_feedback ():
    print (random.choice(feedback_statement[feedback_array[State.state+1]]))
    return

def print_job_continued ():
    os.system("tput reset")
    print ("-"*70+"Happy to see your dedication!"+"-"*70+"\n")
    print ("You continue to be an employee at "+str(company[User.current_company[-1]])+"!\n")
    print ("Your annual pay will be $"+"{:,}".format(int(User.current_salary[-1]))+" for the next 2 years.\n")
    print ("Your skills as a "+ get_sector(User.current_sector[-1]) +" will increase by "+str(2*User.current_growth[-1])+" points, over these 2 years.\n")
    input ("Press Enter to fast forward two years.")
    return


def print_after_job ():
    choice = int(User.current_choice)
    os.system("tput reset")
    print ("*"*70 + " Two years later, in your career... "+"*"*70+'\n')
    print ("Congratulations, you have successfully completed two years at "+str(company[User.current_company[-1]]+'!\n'))
    print ("Your skills and networth have increased, as you can see in the chart below.\n")
    print ("The feedback from your superiors for this job is :\n")
    print_feedback()
    print ("")
    return

def print_job_details ():
    choice = int(User.current_choice)
    os.system ("tput reset")
    print ("-"*80+"Congratulations!"+"-"*80+"\n")
    print ("You are now an employee at "+str(company[State.company_selected[choice-1]])+".\n")
    print ("Your annual pay will be $"+"{:,}".format(int(State.salary[choice-1]))+" for the next 2 years.\n")
    print ("Your skills as a "+ get_sector(State.sectors_selected[choice-1]) +" will increase by "+str(2*State.growth[choice-1])+" points, over these 2 years.\n")
    input ("Press Enter to fast forward two years.")
    return 1

def print_jobs (state):
    os.system("tput reset")
    print ("The following jobs are available in the market right now:-")
    if State.fired_flag != 1:
        print ("S.No '0' is your current job with updated details.\n")
    for i in range (0,5) :
        sector_selected = get_sector(State.sectors_selected[i])
        print(str(i+1)+'. '+company[State.company_selected[i]])
        print ('   Role          : '+sector_selected)
        print ('   Annual Salary : $'+"{:,}".format(int(State.salary[i])))
        print ('   Annual Growth : '+str(State.growth[i])+' points\n')
    if State.fired_flag != 1:
        print ("0. "+company[User.current_company[state-1]]+" \t\t\t\t*** Current Job ***")
        print ('   Role          : '+get_sector(User.current_sector[-1]))
        print ('   Annual Salary : $'+"{:,}".format(int(User.current_salary[state-1]*1.02))+\
         " \t\t\t[An increase of $"+"{:,}".format(int(User.current_salary[state-1]*0.05))+"]")
        print ('   Annual Growth : '+str(User.current_growth[state-1])+' points\n')
    return

def print_networth ():
    print ("Your current networth is $"+"{:,}".format(int(User.networth)))
    return

def print_placement_offers():
    for i in range (0,5) :
        sector_selected = get_sector(State.sectors_selected[i])
        print(str(i+1)+'. '+company[State.company_selected[i]])
        print ('   Role          : '+sector_selected)
        print ('   Annual Salary : $'+"{:,}".format(int(State.salary[i])))
        print ('   Annual Growth : '+str(State.growth[i])+' points\n')
    return

def print_alert():
    print("PREDICTION: "+ get_sector(State.current_booming[-1])+" profiles will be in demand in the years to come.\n")

def print_choice_prompt():
    User.current_choice = input ("Enter S.No. of job you wish to choose:\n")
    return

def print_skills ():
    print ('\nYour current skills are as follows - [each score out of 100]:\n'+ \
    '\nWeb Development and Design\t\t'+str(User.skills[0])+" points"+\
    '\nSoftware Development and Consultancy\t'+str(User.skills[1])+" points"+\
    '\nInvestment Analysis and Consultancy\t'+str(User.skills[2])+" points"+\
    '\nSystems Engineering and Architecture\t'+str(User.skills[3])+" points"+\
    '\nData Science and Analysis\t\t'+str(User.skills[4])+" points\n")
    return

def print_fire ():
    pass

def print_basic_data ():
    print ('#'*70+'\n')
    print_alert()
    print_networth()
    print_skills()
    
    print ('#'*70+'\n')
    return

