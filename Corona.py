import pprint
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics 
import math
import datetime
from scipy import optimize
from numpy import linalg as LA


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

x = []
y = []
for i in range(len(arr)):
    x.append(arr[i][0])
    y.append(arr[i][1])

#pprint.pprint(arr)

def test_func(x, m, b):
    return m*x+b

params, params_covariance = optimize.curve_fit(test_func, x, y, p0=[1, 1])
#pprint.pprint(params)
expec = params[1]/(-1 * params[0]) - len(x)
pprint.pprint("Expected Number of Days remaining: " + str(expec))

end_date = datetime.date.today() + datetime.timedelta(days=expec)
print("Expected End Date: " + str(end_date))