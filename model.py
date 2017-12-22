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

def get_sector(var):
    if var == 0 :
        sector_selected = WEB
    elif var == 1 :
        sector_selected = DEV
    elif var == 2 :
        sector_selected = INV
    elif var == 3 :
        sector_selected = SYS
    else :
        sector_selected = DAT
    return sector_selected



base_dataset = genfromtxt('dataset.csv', delimiter=',')
sector_dataset = genfromtxt('dataset2.csv', delimiter=',')

sector_companies = [[],[],[],[],[]]
for i in range (0,60):
    for j in range (0,5):
        if (sector_dataset[i][j] == 1):
            sector_companies[j].append(i)


# recession_flag = 0
# recession_count = 0
# recession_probability = 10
# recession_sector = -1

# job_quality = 5
# current_booming = [random.randint(0,4)]
# sectors_selected = []
# company_selected = []
# salary = []
# growth = []
# sector_score = []

# fired_flag = 0

feedback_array = [2,3,2,1,0,2,4,3,1,0,3]

feedback_statement = [["Your performance has been extremely poor, you need to work harder to stay.",\
"You have been performing extremely below par, you should probably consider working elsewhere.",\
"My grandmother could have done a better job, you need to get your life together."],\
["You have performed poorly, more was expected from a recruit of your stature.",\
"Your performance has been below par, you need to work harder.",\
"You are walking on thin ice, you should work harder."],\
["Your performance can ben deemed satisfactory.",\
"An okay job done. Not bad at all.",\
"You are okay. Not good. Not bad. Okay. Okay people don't get a huge raise, you know."],\
["Good job, we could use more people like you.",\
"You are good at what you do, we respect that.",\
"You are a valuable member of our team, keep up the good work."],\
["You are indispensabe.",\
"You are essential to us, enjoy the huge raise.",\
"You are the best we have."]]

WEB = "Web Developer"
DEV = "Software Developer"
INV = "Investment Analyst"
SYS = "Systems Architect"
DAT = "Data Analyst"

