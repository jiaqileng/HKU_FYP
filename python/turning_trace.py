#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 02:26:40 2018

@author: lengjiaqi
"""
#this program traces the turning-point in the energy spectrum
#we use the refined log-log data in this program
import numpy as np
import matplotlib.pyplot as plt

def get_matrix():
        A = []
        with open("refine_logspec_5000.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A


S = get_matrix()

#check the shape of input
#the results should be 501*5001
print(len(S))
print(len(S[0]))

#turning-point tracing
#need to set a starting point, we choose logk = 4.5, i.e., logk[4075]
N = 5000
t = np.linspace(0, 0.5, num=501)
k = np.linspace(0,250, num=251)
logk = np.linspace(0, np.log(250), num=N+1)
delta_x = logk[2] - logk[0]
tr_freq = np.zeros(501)
counter = 4300

for i in range(501):
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
logturnfreq = np.zeros(501)
for i in range(501):
    n = int(tr_freq[i])
    logturnfreq[i] = logk[n]

time = 20
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
plt.plot([logk[r]], [S[time][r]], 'bo')
plt.xlabel('Logarithm of frequency')
plt.ylabel('Logarithm of Energy Spectrum')
plt.title('Check: turning point at t = 0.02')
plt.show()

