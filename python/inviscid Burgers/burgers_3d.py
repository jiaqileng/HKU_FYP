from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')


# Make the data
##set the mesh grid;
T = input("The spatial domain is set to be [0, 1], but you can set the time-lapse: ")
N1 = input("Please input the size of spatial discretization: ")
N2 = input("And the size of time discretization: ")

N1 = int(N1)

N2 = int(N2)
T = float(T)

##initialize the mesh grid:
x = np.linspace(0, 1, num=N1+1)
f = np.sin(2 * np.pi * x)
dx = 1/N1
dt = T/N2


##input the initial data:
u = np.zeros((N2+1, N1+1))

j = 0
while j < N1+1:
    u[0, j] = f[j]
    j += 1


##perform the numerical scheme;
i = 0
j = 1
while i < N2:
    while j < N1+1:
        u[i+1, j] = u[i, j] - dt *(np.power(u[i,j], 2) - np.power(u[i, j-1], 2))/(2 * dx)
        j += 1
    j = 1
    i += 1

# Plot the surface.
X = np.arange(0, 1+dx, dx)
Y = np.arange(0, T+dt, dt)
X, Y = np.meshgrid(X, Y)
Z = u
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
