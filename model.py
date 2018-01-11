'''
MODEL

The data centre of the application.
Contains all data points of the app,
common throughout the application.

Imported by main, view and controller.
'''

from numpy import genfromtxt
import random

company = ['Google Inc.','Apple Inc.','Facebook Inc.','Microsoft','Amazon',\
'PayPal','Adobe','Intel','Oracle','Samsung','Yahoo','IBM','Nintendo','Blackberry',\
'Twitter','Cisco','Electronic Arts','Nvidia','Dell Technologies','HTC','AirBnB',\
'Uber','Netflix','Palantir','WeWork','SpaceX','Dropbox','Snap Inc.','Xiaomi',\
'Pinterest','Flipkart','PayTM','Snapdeal','Swiggy','Ola','Bigbasket','Hike Messenger',\
'OYORooms','Zomato','Quikr','Infosys','Wipro','TCS','Congnizant','Tech Mahindra',\
'HCL Technologies','L&T Infotech','Capgemini','Accenture ','Honeywell','VISA','DBS',\
'Morgan Stanley','Tower Research','UBS','McKinsey and Company','Bain and Company',\
'DE Shaw & Co','Goldman Sachs','Ernst & Young LLP']

high_co = [i for i in range(0,9)] + [i for i in range(20,29)] + [i for i in range(50,59)]
low_co = [i for i in range(10,19)] + [i for i in range(30,49)]

base_dataset = genfromtxt('dataset.csv', delimiter=',')

#Arrays of Environment Variables
hj_sal = []
lj_sal = []
hj_req = []
lj_req = []
hj_co = []
lj_co = []
cutoff_score = []
salary = []

#Environment Variables
iteration = 0
mode = -1
scenario = -1
choice = -1
net_salary = 0
fired_count = 0

#Data Variables
name = ""
email = ""
age = ""
branch = ""

#Flags
co_flag = 0
fired_flag = 0