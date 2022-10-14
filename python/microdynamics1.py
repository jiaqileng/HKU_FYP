#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:55:26 2018

@author: lengjiaqi
"""

#this is the first part of the program: super_micro_dynamics
#this program aims to calculate the solution of viscous burgers equation within 0.03 unit of time
#to obtain high resolution, the time frame is divided into 30000 parts. 

import numpy as np
import matplotlib.pyplot as plt


#run the numerical scheme to generate 501*30001 solution matrix
v = 0.1
T = 0.03
N1 = 500
N2 = 60000
dx = 1/N1
dt = T/N2
r = v*dt/np.power(dx,2)
s = dt/dx

print("The von Neumann coefficient is")
print(r)

# Initialize the mesh grid.
x = np.linspace(0, 1, num=N1+1)
f = 1200*(x * (x-1/3) * (x-4/7) * (x-1) + 2/315)


# Define and input the initial data.
u = np.zeros((N2+1, N1+1))
j = 0
while j < N1+1:
    u[0, j] = f[j] 
    j += 1
    
    
#perform the corresponding numerical scheme;
i = 0; j = 1
    
while i < N2 - 1:
    #heat phase
    u[i+1, 0] = (1 - 4*r) * u[i, 0] + 2*r*(u[i,1] + u[i, N1-1])
    while j < N1-1:
        u[i+1, j] = (1 - 4*r) * u[i, j] + 2*r*(u[i,j+1] + u[i, j-1])
        j += 1
            
    u[i+1, j] = (1 - 4*r) * u[i, j] + 2*r*(u[i,0] + u[i, j-1])
    u[i+1, j+1] = u[i+1, 0]
    j = 1
    #inviscid phase
    u[i+2, 0] = u[i+1, 0]*(1 - s*(u[i+1,1] - u[i+1, N1-1]))
    while j < N1-1:
        u[i+2, j] = u[i+1, j]*(1 - s*(u[i+1,j+1] - u[i+1, j-1]))
        j += 1
            
    u[i+2, j] = u[i+1, j]*(1 - s*(u[i+1,0] - u[i+1, j-1]))
    u[i+2, j+1] = u[i+2, 0]
    j = 1
    i += 2
    
#plot the solutions & check
plt.plot(x, u[0,], "r-")
plt.plot(x, u[60000,],'b-')
plt.title("x-u plot: the solution")
plt.show()


#write the data/solution to a file.
#We only extract 1/100 data from the giant matrix. The output should be a 301*501 matrix.
#this resolution is 10 times than previous resolution 
with open("super_micro.txt","w") as w:
    for i in range(301):
        for j in range(N1+1):
            w.write(str(u[200*i][j]) + " ")
        w.write("\n")
