import numpy as np
import matplotlib.pyplot as plt

#set the mesh grid;
T = input("The spatial domain is set to be [0, 1], but you can set the time-lapse: ")
N1 = input("Please input the size of spatial discretization: ")
N2 = input("And the size of time discretization: ")

N1 = int(N1)
N2 = int(N2)
T = float(T)

#initialize the mesh grid:
x = np.linspace(0, 1, num=N1+1)
f = np.sin(2 * np.pi * x)
dx = 1/N1
dt = T/N2


#input the initial data:
u = np.zeros((N2+1, N1+1))

j = 0
while j < N1+1:
    u[0, j] = f[j]
    j += 1


#perform the numerical scheme;
i = 0
j = 1
while i < N2:
    while j < N1+1:
        u[i+1, j] = u[i, j] - dt *(np.power(u[i,j], 2) - np.power(u[i, j-1], 2))/(2 * dx)
        j += 1
    j = 1
    i += 1
    

#plot the initial function f and the solution at t=1;
t0 = int(N2/2)
plt.plot(x, u[0,])
plt.plot(x, u[t0,])
plt.plot(x, u[N2, ])
plt.show()

