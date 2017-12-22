import os
import time
from user import User
from state import State
from model import *
from view import *
from events import *
from job import *

os.system("tput reset")
print ('\n'+'*'*50+"\nWelcome to the prototype of this Career Simulator!\n"+'*'*50+'\n')
User.name = input('\nEnter Your Name:\n')
User.age = input('\nEnter Your Age:\n')
User.email = input('\nEnter Your E-Mail Address:\n')
User.iq = input ("\nEnter Score:\n")
print ("\nProfiles:\n\n1. "+WEB+"\n2. "+DEV+"\n3. "+INV+"\n4. "+SYS+"\n5. "+DAT)
User.pref = input("\nAmong these, what will you prefer to be? Enter the S.No.\n")
User.initiate_skills()
User.skills[int(User.pref)-1] = 20
os.system("tput reset")
print ("\nHello "+User.name+", you just graduated from college and \
have the following 5 job offers, choose one to start your career!\n")

initiate_sectors()
generate_placement_events()
generate_placement()
# print_status()
print_placement_offers()
print_basic_data()
print_choice_prompt()
print_job_details()
print_status()
update_user(0)
print_after_job()
print_basic_data()
temp = input("Press Enter to see the jobs available right now.\n")

while (State.state < 10):
    State.state+=1
    print_status()
    generate_job_events()
    # if feedback == 0: 
    #     fire()
    #     print_fire()
    generate_jobs()
    print_jobs(State.state)
    print_basic_data()
    print_choice_prompt()

    if (int(User.current_choice) != 0):
        update_user(State.state)
        print_job_details()

    else:
        continue_user(State.state)
        print_job_continued()

    print_after_job()
    print_basic_data()
    temp = input("Press Enter to see the jobs available right now.\n")
User.log()
os.system("tput reset")
print ("\n\t\t\t\t\t\t\tnGAME OVER\n")
print ("Risk:" + str(User.risk)+ "\n\t\t"+str(sum(User.risk))+"\n")
print ("Gain:" + str(User.gain)+ "\n\t\t"+str(sum(User.gain))+"\n")
print ("NetWroth:" + "{:,}".format(int(User.networth)))