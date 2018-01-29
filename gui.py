import os
import random
import model
import tkinter as tk

root = tk.Tk()
root.geometry('{}x{}'.format(800, 600))
root.resizable(width=False, height=False)

v = tk.StringVar()

v.set("\nHello, thank you for participating in this project.\n"+"\n"+
    "INSTRUCTIONS:-\n"+"\n"+
    "1. There will be a total of ten turns."+"\n"+
    "2. You'll be given two job choices in each turn, you have to choose one."+"\n"+
    "3. You'll be given a one year contract for each job."+"\n"+
    "4. The goal is to earn as much money as possible at the end of ten turns."+"\n"+
    "5. Each job choice given will have the following:"+"\n"+
    " "*3+"~ Name of Company"+"\n"+
    " "*3+"~ Annual Salary"+"\n"+
    " "*3+"~ Performace Required"+"\n"+
    "6. After each turn, you'll be alloted a performance score."+"\n"+
    "7. If the performance score is below the requirement of your previous job, you'll be fined $200,000."+"\n"+
    "8. Best of luck. 3:)\n")


def print_data_collect () :
    '''
    User information collected, and mode-scenario specified.
    '''
    # os.system("clear")
    # print ("#"*158+"\n")
    # model.name =     input ("Enter Your Name            : ")
    # model.email =    input ("Enter Your email Address   : ")
    # model.age =      input ("Enter Your Age             : ")
    # model.branch =   input ("Enter Your Branch          : ")
    # print("")
    # model.mode =     int(input ("Enter mode as told     : "))
    # model.scenario = int(input ("Enter scenario as told : "))
    # text1 = "Check"
    # w = tk.Label(root,text=text1).pack()
    v.set("New Test")
    return

def print_initiate() :

    frame = tk.Frame(root)
    intro = tk.Frame (root, height='500',width='600')
    intro.pack()
    intro.pack_propagate(False)
    w = tk.Label(intro,textvariable=v).pack()
    frame.pack()
    button = tk.Button(frame, text="QUIT", command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text="Continue", command=print_data_collect)
    slogan.pack(side=tk.LEFT)
    root.mainloop()
    return
