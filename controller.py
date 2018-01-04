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
    
    pass

def process () :
    '''
    Generates Performance Score as per mode
    '''
    pass

def propose () :
    choose_jobs()
    view.print_progress()
    view.print_jobs()
    view.take_input()
    process()
    return