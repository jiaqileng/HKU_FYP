#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 18:12:59 2018

@author: lengjiaqi
"""
#this is the second part of the program: super_micro_dynamics
#this program aims to compute the energy spectrum and trace the turning point within 0.03 unit of time

import numpy as np
import matplotlib.pyplot as plt

def get_matrix():
        A = []
        with open("super_micro.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A


R = get_matrix()

#also compute the energy spectrum
spec = np.zeros((301, 251))
logspec = np.zeros((301, 251))
for i in range(301):
    spec[i] = np.power(np.abs(np.fft.rfft(R[i])), 2)
    
#rescale the log-log plot
logspec = np.log(spec)

N = 5000
dx = np.log(250)/N
frq = 2
lb = np.log(frq-1)
ub = np.log(frq)
re_logspec = np.zeros((501, N+1))


for i in range(301):
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
t = np.linspace(0, 0.03, num=301)
k = np.linspace(0,250, num=251)
logk = np.linspace(0, np.log(250), num=N+1)

plt.plot(np.log(k), logspec[252], 'r')
plt.show()

plt.plot(logk, re_logspec[252], 'b')
plt.show()


plt.plot(np.log(k), logspec[300], 'r')
plt.show()

plt.plot(logk, re_logspec[300], 'b')
plt.show()

#turning point tracing
delta_x = logk[2] - logk[0]
tr_freq = np.zeros(301)
counter = 4300
S = re_logspec

for i in range(301):
    counter = 4300
    while counter < 5001:
        delta_y = S[i][counter+1] - S[i][counter-1]
        test = delta_y/delta_x
        d = np.abs(1.9 + test)
        if d > 0.7:
            tr_freq[i] = counter
            break
        else:
            counter -= 1
            continue

#plot the tracing
logturnfreq = np.zeros(301)
for i in range(301):
    n = int(tr_freq[i])
    logturnfreq[i] = logk[n]
    
time = 200
plt.plot(t, logturnfreq)
plt.plot([t[time]],[logturnfreq[time]],'bo')
plt.plot([t[1]],[logturnfreq[1]],'ro')
plt.xlabel('time')
plt.ylabel('logarithm of the turning frequency')
plt.title('The Turning Point Tracing')
plt.show()

#check the tracing by eyes
plt.plot(logk, S[time])
r = int(tr_freq[time])
plt.plot([logk[r]], [S[time][r]], 'o')
plt.show()


slope = np.zeros(5001)
for l in range(4000, 5000):
    dy = S[time][l+1] - S[time][l-1]
    slope[l] = dy/delta_x
    
plt.plot(logk, slope)