import random

class State () :
    
    state = 0

    recession_flag = 0
    recession_count = 0
    recession_probability = 10
    recession_sector = -1

    job_quality = 5
    current_booming = [random.randint(0,4)]
    sectors_selected = []
    company_selected = []
    salary = []
    growth = []
    sector_score = []

    fired_flag = 0
