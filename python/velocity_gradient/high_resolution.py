#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:10:43 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

# Input other values.
v = 0.001
T = 5
N1 = 400
N2 = 100000
dx = 1/N1
dt = T/N2
r = v*dt/np.power(dx,2)

print("The von Neumann coefficient is")
print(r)


# Initialize the mesh grid.

x = np.linspace(-1, 2, num=3*N1+1)
u0 = (np.sin(2*np.pi*x) - 7*np.sin(4*np.pi*x) + 3*np.cos(6*np.pi*x))/100
B0= (-np.cos(2* np.pi *x) + 7*np.cos(4* np.pi *x)/2 + np.sin(6*np.pi*x))/(200*np.pi)

u0g = 2*np.pi *(np.cos(2*np.pi*x) - 14*np.cos(4*np.pi*x) - 9*np.sin(6*np.pi*x))/100
f = np.exp(-B0/(2*v))

M = min(u0g)
print(M)
'''
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
with open("test1+.txt","w") as w:
    for i in range(101):
        for j in range(N1+1):
            w.write(str(u[1000*i][j]) + " ")
        w.write("\n")
'''
#read file
        
def get_matrix():
        A = []
        with open("test1+.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A

B = get_matrix()

grad_b = np.zeros((101, 399))

dx = 1/400

for i in range(101):
    for j in range(399):
        grad_b[i,j] = (B[i][j+2] - B[i][j])/(2*dx)

x = np.linspace(dx, 1-dx, num=399)

#plot the geadient velocity minimal
t = np.linspace(0, 5, num=101)
grad_min_b = np.zeros(101)

for i in range(101):
    grad_min_b[i] = min(grad_b[i,])


w = 1/M
t1 = np.linspace(0,-60*w/100, num = 101)
t2 = np.linspace(3, 5, num=101)
y = 1/(t1 + w)

l = grad_min_b[50]
C = l*np.exp(2.5)
z= C*np.exp(-t2)-0.6





fig, ax = plt.subplots()
ax.plot(t, grad_min_b, 'r-', label='min gradient')
ax.plot(t1, y, 'g-', label='1/(t-1/M)')
ax.plot(t2, z, 'b-', label='Cexp^(-t)-0.6')
legend = ax.legend(loc='lower right', shadow=True, fontsize='x-large')

plt.title('Test function1')
plt.show()