'''
MAIN

This is the state machine of the application.
'''

import os
import controller
import view
import model
import gui

os.system ("clear")
view.print_initiate()
# gui.print_initiate()
view.print_data_collect()

for i in range (0,10):
    controller.propose()
    model.iteration+=1

view.print_final()