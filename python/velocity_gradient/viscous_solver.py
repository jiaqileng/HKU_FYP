#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 19:23:25 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

# Input other values.
v = 0.005
T = 1
N1 = 200
N2 = 100000
dx = 1/N1
dt = T/N2
r = v*dt/np.power(dx,2)

print("The von Neumann coefficient is")
print(r)


# Initialize the mesh grid.
x = np.linspace(-1, 2, num=3*N1+1)
u0 = np.sin(2* np.pi *x)
B0= np.cos(2* np.pi *x)/(-2*np.pi)


f = np.exp(-B0/(2*v))
boundary = f[0]

# Define and input the initial data.
H = np.zeros((N2+1, 3*N1+1))

for j in range(3*N1+1):
    H[0, j] = f[j] 
    j += 1
    
    
#perform the corresponding numerical scheme;
i = 0; j = 1
    
for i in range(N2):
    H[i+1, 0] = (1 - 2*r) * H[i, 0] + r*(H[i,1] + H[i, 3*N1-1])
    for j in range(3*N1):
        H[i+1, j] = (1 - 2*r) * H[i, j] + r*(H[i,j+1] + H[i, j-1])
            
    H[i+1, 3*N1] = (1 - 2*r) * H[i, 3*N1] + r*(H[i,1] + H[i, 3*N1-1])


#derive the viscous solution from heat equation
p = - v/dx

u = np.zeros((N2+1, N1+1))

    
for i in range(N2+1):
    for j in range(N1+1):
        u[i, j] = p*(H[i, j+N1+1] - H[i, j+N1-1])/H[i,j+N1]

x_new = np.linspace(0,1, N1+1)
#plot the solutions & check
plt.plot(x_new, u[0,], "r-")
plt.plot(x_new, u[10000,],'g-')
plt.plot(x_new, u[30000,],'b-')
plt.title("x-u plot: the solution")
plt.show()

#write the data/solution to a file.
#We only extract 1/1000 data from the giant matrix. The output should be a 501*501 matrix.
with open("sin_v_0.005.txt","w") as w:
    for i in range(101):
        for j in range(N1+1):
            w.write(str(u[1000*i][j]) + " ")
        w.write("\n")
