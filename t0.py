#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:04:18 2019

@author: lengjiaqi
"""
import numpy as np
import matplotlib.pyplot as plt
from MHD_68 import MHD_solver

x = np.linspace(0, 1, num=1001)
f0 = np.sin(2*np.pi*x) +  3*np.cos(4*np.pi*x) + 5*np.sin(16*np.pi*x) - 7*np.cos(24*np.pi*x)
g0 = 0*x


u0, b0 = MHD_solver(0.01, 0, 0.5, 1000, 100000, f0, g0)

#plot u(t,x)
fig, ax = plt.subplots()
ax.plot(x, u0[0], 'r--', label='initial data')
ax.plot(x, u0[1000], 'm-', label='t = 0.1')
ax.plot(x, u0[3000], 'b-', label='t = 0.1')
ax.plot(x, u0[5000], 'g-', label='t = 0.5')
ax.plot(x, u0[8000], 'k-', label='t = 0.8')

legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

plt.show()


#write the data/solution to a file.
with open("t0_u.txt","w") as w:
    for i in range(101):
        for j in range(1001):
            w.write(str(u0[1000*i][j]) + " ")
        w.write("\n")
