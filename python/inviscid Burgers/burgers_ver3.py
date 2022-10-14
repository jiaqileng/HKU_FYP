# This is a 1-d inviscid burgers equation solver by the Lax-Friedrichs scheme.
# The initial data is a superposition of trig functions.

import numpy as np
import matplotlib.pyplot as plt

#set the mesh grid;
print("The spatial domain is set to be [0, 1].")
T = input("The time-lapse is set to be: ")
N1 = input("Please input the size of spatial discretization: ")
N2 = input("And the size of time discretization: ")

N1 = int(N1)
N2 = int(N2)
T = float(T)

#initialize the mesh grid:
x = np.linspace(0, 1, num=N1+1)
f = np.sin(2 * np.pi * x)
rand = np.random.normal(0, 0.1, (N2+1,N1+1))
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
    while j < N1:
        u[i+1, j] = (u[i, j-1] + u[i, j+1])/2 - dt *(np.power(u[i,j+1], 2) - np.power(u[i, j-1], 2))/(2 * dx) + rand[i,j-1]        
        j += 1
    j = 1
    i += 1
    

#plot the solutions and their ft;
t0 = int(N2/2)
a = np.fft.fft(u[0,])
b = np.fft.fft(u[t0,])
c = np.fft.fft(u[N2,])

fig, axs = plt.subplots(3, 1, constrained_layout=True)
axs[0].plot(x, u[0,], 'r-')
axs[0].plot(x, u[t0,], 'b-')
axs[0].plot(x, u[N2,], 'g-')
axs[0].set_title('Solution')
axs[0].set_xlabel('Spatial domain')
fig.suptitle('Solutions of inviscid Burgers equation and their Fourier transform', fontsize=12)

axs[1].plot(x, np.abs(a), 'r-')
axs[1].plot(x, np.abs(b), 'b-')
axs[1].plot(x, np.abs(c), 'g-')
axs[1].set_title('Fourier Transform')
axs[1].set_xlabel('Frequency domain')

axs[2].plot(x, np.log(np.abs(a)), 'r-')
axs[2].plot(x, np.log(np.abs(b)), 'b-')
axs[2].plot(x, np.log(np.abs(c)), 'g-')
axs[2].set_title('log-plot Fourier Transform')
axs[2].set_xlabel('Frequency domain')

plt.show()