# This is a program that can plot the burgers flow at finite time. 
# The user can input the initial data, see f.
# There are three particles that can be traced, see p1, p2, and p3.

import numpy as np
import matplotlib.pyplot as plt


#let the user choose what method to utilize
print("The spatial domain is set to be [0, 1].")
T = input("The time-lapse is set to be: ")
N1 = input("Size of spatial discretization: ")
N2 = input("Size of time discretization: ")

N1 = int(N1)
N2 = int(N2)
T = float(T)
#initialize the mesh grid:
x = np.linspace(0, 1, num=N1+1)
f = np.sin(2 * np.pi * x)
rand = np.random.normal(0, 0.1, (N2+1, N1+1))
dx = 1/N1
dt = T/N2


#input the initial data:
u = np.zeros((N2+1, N1+1))

j = 0
while j < N1+1:
    u[0, j] = f[j]
    j += 1



i = 0; j = 1
while i < N2:
    while j < N1:
        u[i+1, j] = u[i, j] - dt *(np.power(u[i,j+1], 2) - np.power(u[i, j-1], 2))/(4 * dx) + 0.5 * rand[i,j-1]
        j += 1
    j = 1
    i += 1



#plot the flow
p1 = np.linspace(0, T, num=N2+1)
p1[0] = 0.2

p2 = np.linspace(0, T, num=N2+1)
p2[0] = 0.9

p3 = np.linspace(0, T, num=N2+1)
p3[0] = 0.45

k = 1
while k < N2 +1:
    a = int(p1[k-1]/dx)
    b = int(p2[k-1]/dx)
    c = int(p3[k-1]/dx)
    r1 = a%N1
    r2 = b%N1
    r3 = c%N1
    
    incre1 = u[k-1, r1] * dt
    incre2 = u[k-1, r2] * dt
    incre3 = u[k-1, r3] * dt
    p1[k] = p1[k-1] + incre1
    p2[k] = p2[k-1] + incre2
    p3[k] = p3[k-1] + incre3
    k += 1

    
fig, axs = plt.subplots(2, 1, constrained_layout=True)
axs[0].plot(x, u[0,], 'r-')
axs[0].set_title('Initial data')
axs[0].set_xlabel('Spatial domain')
fig.suptitle('Burgers Flow 3', fontsize=12)

axs[1].plot(p1)
axs[1].plot(p2)
axs[1].plot(p3)
axs[1].set_title('Burgers flow')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Spatial coordinate of the particle')

