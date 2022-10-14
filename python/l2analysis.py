#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:57:16 2018

@author: lengjiaqi
"""

#this program computes the energy decay in viscous burgers equation.
#the data is from viscous-splitting method.
import numpy as np
import matplotlib.pyplot as plt

def get_matrix():
        A = []
        with open("vis_split.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A



#check the input size 
u = get_matrix()
print(len(u))
print(len(u[0]))
#the test result should be 501*501

#L2 analysis wrt time, E is the energy. 
A = np.zeros(501)
E = np.zeros(501)
for i in range(501):
    for j in range(501):
        A[j] = np.power(u[i][j],2) * 0.001
    E[i] = np.sum(A)



t = np.linspace(0, 0.5, num=501)

#plot the L2 analysis
plt.plot(t, E)
plt.title('Energy decay')
plt.xlabel('time t')
plt.ylabel('Energy E(t)')
plt.show()



#slope of the log plot
logE = np.log(E)
slope1 = np.zeros(501)
slope2 = np.zeros(501)

slope1[0] = (logE[1] - logE[0])/0.001

for i in range(1, 500):
    slope1[i] = (logE[i+1] - logE[i-1])/0.002
    
slope1[500] = slope1[499]


#slope of the log-log plot

slope2[0] = (logE[1] - logE[0])/(np.log(t[1]) - np.log(t[0]))

for i in range(1, 500):
    slope2[i] = (logE[i+1] - logE[i-1])/(np.log(t[i+1]) - np.log(t[i-1]))
    
slope2[500] = (logE[500] - logE[499])/(np.log(t[500]) - np.log(t[499]))


#plot
plt.subplot(2, 2, 1)
plt.plot(t, logE, 'k-')
plt.title('t-log(E) plot and its slope')
plt.ylabel('log(E)')

plt.subplot(2, 2, 2)
plt.plot(np.log(t), logE, 'b-')
plt.title('log(t)-log(E) plot and its slope')


plt.subplot(2, 2, 3)
plt.plot(t, slope1, 'k-')
plt.xlabel('time')
plt.ylabel('Slope of log(E)')

plt.subplot(2, 2, 4)
plt.plot(np.log(t), slope2, 'b-')
plt.xlabel('log(time)')
plt.show()


t_zoom = np.linspace(0.2, 0.5, num=301)
slope1_zoom = np.zeros(301)

for i in range(301):
    slope1_zoom[i] = slope1[i+200]
    
plt.plot(t_zoom, slope1_zoom, 'k')
plt.xlabel('time')
plt.ylabel('Slope of log(E)')
plt.title('Slope of t-log(E)')
plt.show()