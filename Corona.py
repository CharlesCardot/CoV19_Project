import pprint
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics 
import math
import datetime
import requests
from bs4 import BeautifulSoup
from scipy import optimize
from numpy import linalg as LA

URL = 'https://www.worldometers.info/coronavirus/country/us/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='col-md-12')
#print(list(soup.children))
sum = list(soup.children)[11]
sum = list(sum.children)[3]
listacle = soup.find_all('script')
item = (str(listacle[23]).split('{'))
print(item)
item2 = (item[15].split('['))
print(item2)
item3 = item2[1].split(',')

goal = []
#print(len(item3))
for i in range(len(item3)):
    if(i == 0):
        ignore = True
    elif(i == (len(item3) - 2)):
        num = item3[i][0:5]
        goal.append(float(num))
    elif(i < (len(item3) - 2)):
        num = item3[i]
        #print(num)
        goal.append(float(num))

#print(goal)

'''
arr = []
with open ("Corona.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        arr.append(temp)

for i in range(len(arr)):
    val = arr[i][1]
    arr[i] = [i,val]
'''

#Start of linear fit
stopnum = len(goal)
i = 0
while(i < (len(goal))):
    #print(i)
    if (goal[i] == 34517):
        goal = goal[i:len(goal)]
        i = stopnum
    i = i+1

#print(goal)

x = []
y = []
for i in range(len(goal)):
    x.append(i)
    y.append(goal[i])

#pprint.pprint(arr)

def test_func(x, m, b):
    return m*x+b

params, params_covariance = optimize.curve_fit(test_func, x, y, p0=[1, 1])
#pprint.pprint(params)
expec = params[1]/(-1 * params[0]) - len(x)
str1 = "Expected Number of Days remaining: " + str(expec)
print(str1)

end_date = datetime.date.today() + datetime.timedelta(days=expec)
str2 = "Expected End Date: " + str(end_date)
print(str2)

file1 = open("Corona.txt","w") 
L = [str1 + " \n", str2 + " \n"] 
file1.writelines(L) 
file1.close()

