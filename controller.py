'''
CONTROLLER

The logical centre of the application, contains
all decision making functions.
All functions here are either interanally called or
called by main.

Imported in main and view.
'''

import random
import model
import view

def choose_sal() :
    '''
    Choose salary in accordance with the mode and scenario.
    Presently, the prototype takes a random educated guess.
    '''
    model.lj_sal.append(round(random.randint(80000+model.iteration*5000,90000+model.iteration*5000),-3))
    model.hj_sal.append(round(random.randint(130000+model.iteration*5000,140000+model.iteration*5000),-3))
    return

def choose_req():
    '''
    Repace random by factoring by company score in company mode.
    It remains in the random range though.
    '''
    model.hj_req.append(random.randint(6,8))
    model.lj_req.append(random.randint(2,3))
    return

def choose_co():
    '''
    Choose company as per scenario
    '''
    model.hj_co.append(random.choice(model.high_co))
    model.lj_co.append(random.choice(model.low_co))
    return

def choose_jobs () :
    '''
    Rich Companies:
    0-9, 20-29, 50-59

    Other Companies:
    10-19, 30-39, 40-49 
    '''
    choose_sal()
    choose_req()
    choose_co()
    return

def generate_cutoff () :
    '''
    Generates Performance Score as per mode
    Modes:
    1. Random Positive Negative
    2. All Positive
    3. All Negative
    4. First Five Positive, then Negative
    5. First Five Negative, then Positive
    6. Alternative Positive Negative
    7. Couple Positive, Couple Negative
    '''
    if model.mode == 1 :
        model.cutoff_score.append(random.randint(1,10))
    elif model.mode == 2:
        model.cutoff_score.append(random.randint(6,10))
    elif model.mode == 3:
        model.cutoff_score.append(random.randint(1,5))
    elif model.mode  == 4:
        if model.iteration < 5:
            model.cutoff_score.append(random.randint(6,10))
        else:
            model.cutoff_score.append(random.randint(1,5))
    elif model.mode == 5:
        if model.iteration < 5:
            model.cutoff_score.append(random.randint(1,5))
        else:
            model.cutoff_score.append(random.randint(6,10))
    elif model.mode == 6:
        if model.iteration % 2 == 0:
            model.cutoff_score.append(random.randint(6,10))
        else:
            model.cutoff_score.append(random.randint(1,5))
    elif model.mode == 7:
        if model.iteration % 3 == 0 or model.iteration % 4 == 0:
            model.cutoff_score.append(random.randint(6,10))
        else:
            model.cutoff_score.append(random.randint(1,5))
    else:
        print("LOL")
    return

def process () :
    if model.choice == 1:
        if model.lj_req[-1] <= model.cutoff_score[model.iteration] :
            model.net_salary += model.lj_sal[-1]
        else:
            model.net_salary -= 200000
            model.fired_count +=1
            model.fired_flag = 1
    else :
        if model.hj_req[-1] <= model.cutoff_score[model.iteration] :
            model.net_salary += model.hj_sal[-1]
        else:
            model.net_salary -= 200000
            model.fired_count +=1
            model.fired_flag = 1
    return

def propose () :
    '''
    Umbrella function for all tasks done when a new couple offer is proposed.
    '''
    choose_jobs()
    view.print_progress()
    view.print_jobs()
    generate_cutoff()
    view.take_input()
    process()
    view.print_feedback()
    return

def log () :
    '''
    Logs data
    '''
    pass