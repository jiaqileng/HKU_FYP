#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:56:08 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

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

def get_matrix_005():
        A = []
        with open("sin_v_0.05.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A005 = get_matrix_005()


def get_matrix_010():
        A = []
        with open("sin_v_0.1.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A010 = get_matrix_010()



def get_matrix_010():
        A = []
        with open("sin_v_0.1.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A010 = get_matrix_010()



def get_matrix_020():
        A = []
        with open("sin_v_0.2.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A020 = get_matrix_020()

def get_matrix_030():
        A = []
        with open("sin_v_0.3.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

A030 = get_matrix_030()



grad001 = np.zeros((101, 199))
grad005 = np.zeros((101, 199))
grad010 = np.zeros((101, 199))
grad020 = np.zeros((101, 199))
grad030 = np.zeros((101, 199))

dx = 1/200

for i in range(101):
    for j in range(199):
        grad001[i,j] = (A001[i][j+2] - A001[i][j])/(2*dx)
        grad005[i,j] = (A005[i][j+2] - A005[i][j])/(2*dx)
        grad010[i,j] = (A010[i][j+2] - A010[i][j])/(2*dx)
        grad020[i,j] = (A020[i][j+2] - A020[i][j])/(2*dx)
        grad030[i,j] = (A030[i][j+2] - A030[i][j])/(2*dx)

x = np.linspace(dx, 1-dx, num=199)

#plot the geadient velocity minimal
t = np.linspace(0, 1, num=101)
grad_min_001 = np.zeros(101)
grad_min_005 = np.zeros(101)
grad_min_010 = np.zeros(101)
grad_min_020 = np.zeros(101)
grad_min_030 = np.zeros(101)

for i in range(101):
    grad_min_001[i] = min(grad001[i,])
    grad_min_005[i] = min(grad005[i,])
    grad_min_010[i] = min(grad010[i,])
    grad_min_020[i] = min(grad020[i,])
    grad_min_030[i] = min(grad030[i,])
    
laplace_010 = np.zeros((101,199))

for i in range(101):
    for j in range(199):
        laplace_010[i,j] = (A010[i][j+2] - 2*A010[i][j+1] + A010[i][j])/np.power(dx,2)

x1 = np.linspace(2*dx, 1-2*dx, num=197)

u_xxx = np.zeros((101, 197))

for i in range(101):
    for j in range(197):
        u_xxx[i, j] = (laplace_010[i, j+2] - laplace_010[i, j])/(2*dx)
        
u_xxx_min = np.zeros(101)
for i in range(101):
    u_xxx_min[i] = max(u_xxx[i,])

'''
fig, ax = plt.subplots()
ax.plot(t, grad_min_001, "r-", label='v=0.01')
ax.plot(t, grad_min_005, "y-", label='v=0.05')
ax.plot(t, grad_min_010, "g-", label='v=0.1')
ax.plot(t, grad_min_020, "b-", label='v=0.2')
ax.plot(t, grad_min_030, "k-", label='v=0.3')

legend = ax.legend(loc='lower right', shadow=True, fontsize='x-large')

plt.title('Minimal velocity gradient plot')
plt.show()
'''

plt.plot(t, 0.01*u_xxx_min)
plt.plot(t, grad_min_010, "r-", label='v=0.01')
plt.show()

'''
#log-log plot
fig, ax = plt.subplots()
ax.plot(np.log(t), np.log(abs(grad_min_001)), "r-", label='v=0.01')
ax.plot(np.log(t), np.log(abs(grad_min_005)), "y-", label='v=0.05')
ax.plot(np.log(t), np.log(abs(grad_min_010)), "g-", label='v=0.1')
ax.plot(np.log(t), np.log(abs(grad_min_020)), "b-", label='v=0.2')
ax.plot(np.log(t), np.log(abs(grad_min_030)), "k-", label='v=0.3')

legend = ax.legend(loc='lower left', shadow=True, fontsize='x-large')

plt.title('Minimal velocity gradient log-log plot')
plt.show()
'''