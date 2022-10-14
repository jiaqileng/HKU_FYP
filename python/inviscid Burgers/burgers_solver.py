import numpy as np
import matplotlib.pyplot as plt


#let the user choose what method to utilize
choose = input("Choose a numerical scheme (1: up-wind non-convservative; 2: up-wind conservative; 3: Lax-Friedrichs): ")

#set the mesh grid;
print("The spatial domain is set to be [0, 1].")
T = input("The time-lapse is set to be: ")
N1 = input("Size of spatial discretization: ")
N2 = input("Size of time discretization: ")

N1 = int(N1)
N2 = int(N2)
T = float(T)

#initialize the mesh grid:
x = np.linspace(0, 1, num=N1+1)
#f = np.sin(2 * np.pi * x) - np.sin(4 * np.pi * x) + np.sin(8 * np.pi * x)
f = np.sin(2 * np.pi * x)
rand = np.random.normal(0, 0.1, N1+1)
dx = 1/N1
dt = T/N2


#input the initial data:
u = np.zeros((N2+1, N1+1))

j = 0
while j < N1+1:
    u[0, j] = f[j]
    j += 1

#perform the corresponding numerical scheme;
if choose == 1:
    i = 0; j = 1
    while i < N2:
        while j < N1:
            u[i+1, j] = u[i, j] - dt * u[i,j] *(u[i,j+1] - u[i, j-1])/(2 * dx)
            j += 1
        j = 1
        i += 1
    
elif choose == 2:
    i = 0; j = 1
    while i < N2:
        while j < N1:
            u[i+1, j] = u[i, j] - dt *(np.power(u[i,j+1], 2) - np.power(u[i, j-1], 2))/(4 * dx)
            j += 1
        j = 1
        i += 1

else:
    i = 0; j = 1
    while i < N2:
        while j < N1:
            u[i+1, j] = (u[i, j-1] + u[i, j+1])/2 - dt *(np.power(u[i,j+1], 2) - np.power(u[i, j-1], 2))/(2 * dx)
            j += 1
        j = 1
        i += 1



#2d-plot the initial function f and the solution at t=1;
t0 = int(N2/2)
plt.plot(x, u[0,], 'r-')
plt.plot(x, u[t0,], 'b-')
plt.plot(x, u[N2, ], 'g-')
plt.show()

