import os
import random
import math
from user import User
from state import State
from model import *

'''
** FEEDBACK

Feedback will be a response from the company where you're working, 
essentially a job_review, while will be a score out of 5, randomly
predicted. 5 being good, 1 being bad. 

Affecs:
- Raise
- Firing
- Quality of Offers [Interesting Idea]

Affected By:
- Booming Sector
- Recession


** FIRING

Firing will be a probable event in each itertion, with the porbability 
depending on the following:

Affects:
- Qualitiy of Offers Recieved

Affected by:
- How long you've worked at a place (Will decrease with increase)
- Sector Stability
- Recession
- Booming Sector

** RECESSION

A random event that will hit with a probability of 0.1+(0.09*state)
Recesssion will not hit a sector that has boomed recently.

Affected By:
- Sector_Stability
- Current_Sector
- Booming Sector

Affects:
Everything

'''


def company_bankrupt ():
    '''
    Affected By:
    - Sector Stability
    - Recession
    - Company Stability Score
    '''
    pass

def manage_job_quality() :
    if State.job_quality < 5 and State.fired_flag != 1:
        State.job_quality = 5
    return

def initiate_recession():
    os.system("tput reset")
    print ("Recession in: "+ get_sector(State.recession_sector))
    temp = input("Press Enter to see the jobs available right now.\n")
    State.sector_score[State.recession_sector]  = 1
    # initiate firing
    # remove possibe jobs
    return

def booming_sector () :
    all_sector = [0,1,2,3,4]
    if State.recession_flag == 1:
        all_sector.remove(State.recession_sector)
    State.current_booming.append(random.choice(all_sector))
    return

def sector_score_control ():
    State.sector_score [State.current_booming[-1]] += 20
    State.sector_score [State.current_booming[-2]] -= 20
    for i in range (0,5):    
        temp = random.randint (0,40)
        State.sector_score[i]+=(temp - 20)
        if State.sector_score[i] < 0 :
            State.sector_score[i] = 0
        if State.sector_score[i] > 100 :
            State.sector_score[i] = 100
    return

def fire ():
    # Fire on '0'
    if (State.recession_flag == 1 and User.current_sector[-1] == State.recession_sector)\
     or feedback_array[State.state] == 0:
        State.job_quality -= 1     
        State.fired_flag = 1
        os.system("tput reset")
        input ("fired")    
    # Modify current job
    return

# def feedback_func ():
#     '''
#     21 arrays for 10 years 
#     1 each for booming/non-booming
#     1 special for recession in current sector

#     A comparison of skill increase vs years at company

#     Affected by:
#     - Sector Score + (Booming Sector) + (Recession) 40%
#     - Choice Score 10%
#     - Skill Score 10%
#     # - Time You've Spent at the Company 30%
#     - Random 40%

#     Include Skillset

#     Will Affect:
#     - Job Quality
#     - Firing
#     '''

#     os.system ("tput reset")
#     print (current_feedback)
#     input ("Test for feedback")
#     return

    # Remove first element, check if this does that.

    # sector_v = sector_score[User.current_sector[-1]]/20
    # choice_v = (100-int(base_dataset[User.current_company[-1]][6]))/20
    # time_v = (6 - User.time_at_job)
    # random_v = (5 - random.randint(0,9))
    # skill_v = (User.skills[User.current_sector[-1]])/20
    # # feedback = 0.2*(sector_v+random_v)+0.3*(choice_v+time_v)
    # feedback.append(math.floor((0.40*(sector_v)\
    # +0.10*(choice_v)+0.40*(random_v)+0.1*(skill_v))*0.75+0.25*feedback[-1]))
    # if feedback[-1] < 0:
    #     feedback[-1] = 0
    # os.system("tput reset")
    # y =input (str(skill_v)+"\n"+str(User.skills)+"Skill Score:\n"+str(0.1*skill_v)+\
    # "\nSector Info:\n"+str(sector_score)+"\nSector: "+str(0.40*sector_v)+"\nChoice: "+str(0.10*choice_v)+\
    # "\nTime: "+str(time_v)+"\nRandom: "+str(0.40*random_v)+"\nFeedback: "+str(feedback))
    # return

def recession ():
    all_sector = [0,1,2,3,4]
    if len(User.current_sector) != 0:
        all_sector.remove(State.current_booming[-1])
        all_sector.append(User.current_sector[-1])
    State.recession_sector = random.choice(all_sector)
    recession_variable = random.randint(0,100)
    if recession_variable < State.recession_probability:
        State.recession_flag = 1
        initiate_recession()
    else:
        State.recession_probability+=9
        pass
    return

def generate_job_events ():
    if State.fired_flag == 1:
        State.fired_flag = 0
    # elif State.fired_flag == 2:
        # State.fired_flag = 0
    if State.recession_flag == 0:
        recession()
    booming_sector()
    sector_score_control()
    fire()
    manage_job_quality()
    return

def generate_placement_events():
    if State.recession_flag == 0:
        recession()
    booming_sector()
    sector_score_control()
    manage_job_quality()
    return    


