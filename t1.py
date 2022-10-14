#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:31:39 2019

@author: lengjiaqi
"""

from MHD_68 import MHD_solver
import numpy as np
import matplotlib.pyplot as plt

N = 1000
M = 50000
x = np.linspace(0, 1-1/N, num=N)

f1 = np.sin(2*np.pi*x) +  3*np.cos(4*np.pi*x) + 5*np.sin(16*np.pi*x) - 7*np.cos(24*np.pi*x)
g1 = 10*np.sin(4*np.pi*x) - np.cos(14*np.pi*x)

u1, b1 = MHD_solver(0.003, 0.003/100, 0.5, N, M, f1, g1)


#plot u(t,x)
fig, ax = plt.subplots()
ax.plot(x, u1[0], 'r--', label='initial data')
ax.plot(x, u1[10000], 'm-', label='t = 0.1')
ax.plot(x, u1[30000], 'b-', label='t = 0.3')
ax.plot(x, u1[50000], 'g-', label='t = 0.5')

legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

plt.show()

#plot b(t,x)
fig, ax = plt.subplots()
ax.plot(x, b1[0], 'r--', label='initial data')
ax.plot(x, b1[10000], 'm-', label='t = 0.1')
ax.plot(x, b1[30000], 'b-', label='t = 0.1')
ax.plot(x, b1[50000], 'g-', label='t = 0.5')

legend = ax.legend(loc='lower left', shadow=True, fontsize='x-large')

plt.show()



#write the data/solution to a file.
with open("t1_u.txt","w") as w:
    for i in range(101):
        for j in range(1000):
            w.write(str(u1[500*i][j]) + " ")
        w.write("\n")
        
with open("t1_b.txt","w") as w:
    for i in range(101):
        for j in range(1000):
            w.write(str(b1[500*i][j]) + " ")
        w.write("\n")
