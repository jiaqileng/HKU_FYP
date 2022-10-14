#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:09:03 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

def get_matrix_0001():
        A = []
        with open("sin_v_0.001.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A0001 = get_matrix_0001()


def get_matrix_0005():
        A = []
        with open("sin_v_0.005.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A0005 = get_matrix_0005()



def get_matrix_001():
        A = []
        with open("sin_v_0.01.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A001 = get_matrix_001()

grad0001 = np.zeros((101, 199))
grad0005 = np.zeros((101, 199))
grad001 = np.zeros((101, 199))


dx = 1/200

for i in range(101):
    for j in range(199):
        grad0001[i,j] = (A0001[i][j+2] - A0001[i][j])/(2*dx)
        grad0005[i,j] = (A0005[i][j+2] - A0005[i][j])/(2*dx)
        grad001[i,j] = (A001[i][j+2] - A001[i][j])/(2*dx)
        

x = np.linspace(dx, 1-dx, num=199)

#plot the geadient velocity minimal
t = np.linspace(0, 1, num=101)
grad_min_0001 = np.zeros(101)
grad_min_0005 = np.zeros(101)
grad_min_001 = np.zeros(101)

grad_max_0001 = np.zeros(101)

for i in range(101):
    grad_min_0001[i] = min(grad0001[i,])
    grad_min_0005[i] = min(grad0005[i,])
    grad_min_001[i] = min(grad001[i,])
    grad_max_0001[i] = max(grad0001[i,])
    
'''
#formation of pre-shock    
pt1 = (1/(2*np.pi), 1/(2*np.pi))
pt2 = (-450, 0)

fig, ax = plt.subplots()
ax.plot(t, grad_min_0001, "y-", label='v=0.001')
ax.plot(t, grad_min_0005, "b-", label='v=0.005')
ax.plot(t, grad_min_001, "g-", label='v=0.01')
ax.plot(pt1, pt2, 'r-', label='pre-shock')
legend = ax.legend(loc='lower right', shadow=True, fontsize='x-large')

plt.title('Minimal velocity gradient plot (vanishing viscosity)')
plt.show()
'''
init = 1/(2*np.pi)
y = 1/(t+ init)

plt.plot(t, grad_max_0001)
plt.plot(t, y, 'g-')
plt.show()