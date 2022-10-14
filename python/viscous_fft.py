#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:57:16 2018

@author: lengjiaqi
"""

#this program computes the Fourier transform of the solution of viscous burgers equation. 
#the data is obtained by viscous-splitting 

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


u = get_matrix()


spec = np.zeros((501,251))
logspec = np.zeros((501,251))

for i in range(501):
    spec[i,] = np.power(np.abs(np.fft.rfft(u[i])), 2)

logspec = np.log(spec)

t = np.linspace(0, 0.5, num=501)
k = np.linspace(0,250, num=251)

#spectrum plot 1


fig, ax = plt.subplots()

ax.plot(np.log(k), logspec[0], 'r', label='t = 0')
ax.plot(np.log(k), logspec[100], 'y', label='t = 0.1')
ax.plot(np.log(k), logspec[200], 'b', label='t = 0.2')
ax.plot(np.log(k), logspec[300], 'g', label='t = 0.3')
ax.plot(np.log(k), logspec[400], 'k', label='t = 0.4')


legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

plt.xlabel('Logarithm of frequency k')
plt.ylabel('Logarithm of energy spectrum E(t, k)')
plt.title('Energy spectrum within 0.4 unit of time')
plt.show()

#tail analysis: slope between log(33) and log(90)
l = np.log(90) - np.log(33)
slope = np.zeros(501)
for i in range(501):
    slope[i] = (logspec[i][90] - logspec[i][33])/l

plt.plot(t, slope)
plt.plot([0.4], [slope[400]], 'o')
plt.text(0.4, -3, r'$(0.4, -1.91)$')
plt.title('Two-point Slope Analysis (33, 90)')
plt.xlabel('time')
plt.ylabel('Slope in the log(k)-log(E) between freq 33 and 90')
plt.show()



#write the data/solution to a file.
with open("spectrum.txt","w") as w:
    for i in range(501):
        for j in range(251):
            w.write(str(spec[i][j]) + " ")
        w.write("\n")
