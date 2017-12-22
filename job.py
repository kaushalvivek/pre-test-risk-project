from model import *
from user import User
from state import State
from events import *
import random
import math

# Risk different when continuing at a job
# Different salary % increase depending on performance
#



def initiate_sectors():
    for i in range (0,5):
        State.sector_score.append(random.randint(30,60))
    return

def continue_user(state):
    User.time_at_job += 2
    User.networth += 2*User.current_salary[-1]
    User.skills[int(User.current_sector[-1])] += 2*User.current_growth[-1]
    User.risk.append(User.risk[-1])
    User.gain.append(User.gain[-1])
    User.current_company.append(User.current_company[-1])
    User.current_sector.append(User.current_sector[-1])
    User.current_salary.append(User.current_salary[-1]*1.02)
    User.current_growth.append(User.current_growth[-1])

def update_user(state):
    User.time_at_job = 2
    choice = int(User.current_choice)
    User.networth += 2*State.salary[choice-1]
    User.skills[State.sectors_selected[choice-1]] += 2*State.growth[choice-1]
    User.risk.append(base_dataset[State.company_selected[choice-1]][4])
    User.gain.append(base_dataset[State.company_selected[choice-1]][5])
    User.current_company.append(State.company_selected[choice-1])
    User.current_sector.append(State.sectors_selected[choice-1])
    User.current_salary.append(State.salary[choice-1])
    User.current_growth.append(State.growth[choice-1])
    #Gain and Risk for sector and iteration count yet to be added
    return

def generate_jobs () :
    '''
    This function generates new jobs, separate from placement to keep options open for learning later.
    To Be Affected By:
    - Quality Score -- 
    - Booming Sector --
    - Sector Stability --

    - Recession
    - Feedback
    - Firing
    ''' 
    # temp = []
    # State.company_selected.clear()
    # State.sectors_selected.clear()
    # salary.clear()
    # growth.clear()
    # for i in range (0,6):
    #     #6 companies randomly selected one each from each domain
    #     State.company_selected.append(random.randint(10*i+0,10*i+9))
    #     for j in range (0,5):
    #         # Job selected from those available at the companies seleceted
    #         if sector_dataset[State.company_selected[i]][j] == 1.0 :
    #             temp.append(j)
    #     State.sectors_selected.append(random.choice(temp))
    # calculate_salary()
    # calculate_growth()
    # return    
    State.company_selected.clear()
    State.sectors_selected.clear()
    State.salary.clear()
    State.growth.clear()
    all_sectors = [0,1,2,3,4]
    all_sectors.remove(State.current_booming[-2])
    if State.recession_flag == 1 :
       if (State.recession_count == 3):
           State.recession_flag = 2
       State.recession_count +=1
       all_sectors.remove(State.recession_sector)
    for i in range (0,2):
        State.sectors_selected.append(State.current_booming[-2])
    for i in range (0,3):
        State.sectors_selected.append(random.choice(all_sectors))
    random.shuffle(State.sectors_selected)

    for i in range (0, len(State.sectors_selected)):
        job_rating = State.sector_score[State.sectors_selected[i]]* 0.05 + State.job_quality
        if job_rating > 10 :
            job_rating = 10
        elif job_rating < 0:
            job_rating = 0
        if job_rating >= 8:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (0, 10) or k in range (20, 30) )])
        elif job_rating >=7:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (10, 20) or k in range (50, 60) )])
        elif job_rating >= 5:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (30, 40))])
        else:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (40, 50) )])
        State.company_selected.append(temp)
    calculate_salary()
    calculate_growth()
    return

def generate_placement () :
    '''
    This function generates the companies where the user is initially placed.
    To Be Affected by:
    - Quality Score - Company
    - Booming Sector - Sector
    - Sector Stability - Company

    Algo:
    Use quality score to set probability of jobs.
    Higher Quality Score will make good jobs more probable.
    Good Jobs: 1-10, 20-30
    Good-Okay Jobs : 11-20, 50-60
    Okay Jobs : 30-40
    lol - 40-50 

    Based on 3 listed factors, a score will be calculated for
    each job, this score will determine what kind of offer it ends up being.

    2 Jobs for Booming Sector, 3 others
    
    '''
    # temp = []
    # for i in range (0,6):
    #     #6 companies randomly selected one each from each domain
    #     State.company_selected.append(random.randint(10*i+0,10*i+9))
    #     for j in range (0,5):
    #         # Job selected from those available at the companies seleceted
    #         if sector_dataset[State.company_selected[i]][j] == 1.0 :
    #             temp.append(j)
    #     State.sectors_selected.append(random.choice(temp))
    
    all_sectors = [0,1,2,3,4]
    all_sectors.remove(State.current_booming[-2])
    if State.recession_flag == 1 :
        if (State.recession_count == 3):
            State.recession_flag = 2
        State.recession_count +=1
        all_sectors.remove(State.recession_sector)
    for i in range (0,2):
        State.sectors_selected.append(State.current_booming[-2])
    for i in range (0,3):
        State.sectors_selected.append(random.choice(all_sectors))
    random.shuffle(State.sectors_selected)

    for i in range (0, len(State.sectors_selected)):
        job_rating = State.sector_score[State.sectors_selected[i]]* 0.05 + State.job_quality
        if job_rating > 10 :
            job_rating = 10
        elif job_rating < 0:
            job_rating = 0
        if job_rating >= 8:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (0, 10) or k in range (20, 30) )])
        elif job_rating >=7:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (10, 20) or k in range (50, 60) )])
        elif job_rating >= 5:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (30, 40))])
        else:
            temp = random.choice([k for k in sector_companies[State.sectors_selected[i]]\
             if (k in range (40, 50) )])
        State.company_selected.append(temp)
    calculate_salary()
    calculate_growth()
    return
        
def calculate_salary ():
    '''
    This function calculates the salary based on 
    pay score of the company, and the skill set of the user.
    Affected By:
    - Sector Score + (Booming Sector)
    - Company Pay Score
    - Job Quality
    '''
    for i in range (0,5) :
        State.salary.append(((base_dataset[State.company_selected[i]][0]/10 * 150000)) \
        *(0.6 + 0.025 * int(User.skills[State.sectors_selected[i]] / 5)+\
        (0.2*State.sector_score[i]/50)+0.2*(State.job_quality)/7.5))
    return

def calculate_growth ():
    '''
    This function calculates the growth rate of the user based on the 
    Growth score of the company.
    Affected By:
    - Years at the Company
    - Feedback
    - Sector Stability
    - Company Growth Score
    '''
    for i in range (0,5) :
        State.growth.append(math.floor(base_dataset[State.company_selected[i]][1]/2))
    return
