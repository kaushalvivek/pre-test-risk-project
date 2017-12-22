import random

class User ():
    networth = 5000
    time_at_job = 0
    skills = [0,0,0,0,0]
    risk = []
    gain = []
    current_company = []
    current_sector = []
    current_salary = []
    current_growth = []
    name = ''
    age = ''
    email = ''
    iq = ''
    pref = -1
    current_choice = -1

    def initiate_skills ():
        for i in range (0, 5):
            User.skills[i] += random.randint(5, 20)
        return

    def log (self):
        logfile = open ('log.txt','w+')
        logfile.write(str(User.name)+', '+str(User.age)+':\n$'+str(User.networth)+\
        '\nSkills:\n'+str(User.skills)+'\nRisk: '+str(User.risk)+'\nGain: '+str(User.gain)+"\nIQ:"+User.iq)
        return
