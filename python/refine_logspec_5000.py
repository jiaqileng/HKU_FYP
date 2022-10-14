#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:05:17 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

def get_matrix():
        A = []
        with open("spectrum.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A


S = get_matrix()

#check the shape
print(len(S))
print(len(S[0]))

#initialize the log-spec
spec = np.zeros((501,251))
logspec = np.zeros((501,251))

for i in range(501):
    spec[i] = S[i]

logspec = np.log(spec)

#refine the resolution in the log-log plot
N = 5000
dx = np.log(250)/N
frq = 2
lb = np.log(frq-1)
ub = np.log(frq)
re_logspec = np.zeros((501, N+1))


for i in range(501):
    frq = 2
    for j in range(N+1):
        counter = j*dx
        if (counter <= ub):
            lb = np.log(frq-1)
            ub = np.log(frq)
            delta_x = ub - lb
            delta_y = logspec[i][frq] - logspec[i][frq-1]
            slope = delta_y/delta_x
            re_logspec[i][j] = logspec[i][frq-1] + slope * (counter - lb)
            
        else: 
            frq += 1
            lb = np.log(frq-1)
            ub = np.log(frq)
            delta_x = ub - lb
            delta_y = logspec[i][frq] - logspec[i][frq-1]
            slope = delta_y/delta_x
            re_logspec[i][j] = logspec[i][frq-1] + slope * (counter - lb)


#plot & check
t = np.linspace(0, 0.5, num=501)
k = np.linspace(0,250, num=251)
logk = np.linspace(0, np.log(250), num=N+1)

plt.plot(np.log(k), logspec[352], 'r')
plt.show()

plt.plot(logk, re_logspec[352], 'b')
plt.show()


plt.plot(np.log(k), logspec[500], 'r')
plt.show()

plt.plot(logk, re_logspec[500], 'b')
plt.show()


#write the data/solution to a file.
with open("refine_logspec_5000.txt","w") as w:
    for i in range(501):
        for j in range(N+1):
            w.write(str(re_logspec[i][j]) + " ")
        w.write("\n")