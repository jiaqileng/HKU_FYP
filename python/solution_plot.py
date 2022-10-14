#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:56:57 2018

@author: lengjiaqi
"""

#This program plots the two solutions given by distincy schemes.
#It includes a 2-d plot and a 3-d plot. The 3-d is only avaible for viscous-splitting.

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def get_matrix1():
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

def get_matrix2():
        A = []
        with open("hopf_cole.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

#check the input size 
H1 = get_matrix1()
H2 = get_matrix2()
print(len(H1))
print(len(H1[0]))
print(len(H2))
print(len(H2[0]))
#the test result should be all 501.

u1 = np.zeros((501,501))
for i in range(501):
    for j in range(501):
        u1[i,j] = H1[i][j]
       
u2 = np.zeros((501,501))
for i in range(501):
    for j in range(501):
        u2[i,j] = H2[i][j]
        
        
#2-d plot the solutions by viscous-splitting method
x = np.linspace(0,1, num=501)

fig, ax = plt.subplots()
ax.plot(x, u1[0], 'r', label='t = 0')
ax.plot(x, u1[50], 'b', label='t = 0.05')
ax.plot(x, u1[250], 'g', label='t = 0.25')
ax.plot(x, u1[500], 'k', label='t = 0.5')

legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

plt.xlabel('x')
plt.ylabel('u')
plt.title('Solution by viscous-splitting method')
plt.show()

#2-d plot the solutions by hopf-cole method
fig, ax = plt.subplots()
ax.plot(x, u2[0], 'r', label='t = 0')
ax.plot(x, u2[50], 'b', label='t = 0.05')
ax.plot(x, u2[250], 'g', label='t = 0.25')
ax.plot(x, u2[500], 'k', label='t = 0.5')

legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

plt.xlabel('x')
plt.ylabel('u')
plt.title('Solution by Hopf-Cole method')
plt.show()
'''
#3-d plot of the surface
fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.linspace(0,0.5, num=501)
x, t = np.meshgrid(x, t)
Z = u
surf = ax.plot_surface(x, t, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)


# Customize the z axis.
ax.set_zlim(-15, 12)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
'''