#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:25:01 2019

@author: lengjiaqi
"""
import numpy as np
import matplotlib.pyplot as plt
from MHD_68 import get_matrix
from scipy import stats
import operator
import matplotlib.animation as animation

N = 100
M = 1000
dx = 1/N
l = np.arange(0, N/2 + 1,1) #(0, ..., N/2)



_u = get_matrix("t8_u.txt")
_b = get_matrix("t8_b.txt")

u = np.zeros((101,100))
b = np.zeros((101,100))

for i in range(101):
    for j in range(100):
        u[i,j] = _u[i][j]
        b[i,j] = _b[i][j]
        
        
n = int(N/2 + 1)
x = np.arange(0, 1, dx)


g = 13/5

plt.plot(x, u[0]+b[0], 'r--')
#plt.plot(x, u[25]+b[25], 'c-')
plt.plot(x,  u[50]+b[50], 'b-')
plt.plot(x, u[100] +b[100], 'g-')
plt.plot([0.5+0.05*g, 0.5+0.1*g], [3,3], 'ro')
plt.show()

plt.plot(x, u[0] - b[0], 'r--')
#plt.plot(x, u[25] - b[25], 'c-')
plt.plot(x,  u[50] - b[50], 'b-')
plt.plot(x, u[100] - b[100], 'g-')
plt.plot([0.5+0.05*g, 0.5+0.1*g], [1,1], 'ro')
plt.show()

plt.plot(x,  u[100]+b[100], 'b--')
plt.plot(x,  u[100] - b[100], 'b-')

plt.show()
'''
plt.plot(x, np.sqrt(3)*u[0]+b[0] , 'r--')
plt.plot(x, np.sqrt(3)*u[20]+b[20] , 'c-')
plt.plot(x,  np.sqrt(3)*u[40]+b[40] , 'b-')
plt.plot(x, np.sqrt(3)*u[60]+b[60] , 'g-')
plt.plot(x, np.sqrt(3)*u[100]+b[100], 'k-')
plt.show()

plt.plot(x, np.sqrt(3)*u[0]-b[0] , 'r--')
plt.plot(x, np.sqrt(3)*u[20]-b[20] , 'c-')
plt.plot(x,  np.sqrt(3)*u[40]-b[40] , 'b-')
plt.plot(x, np.sqrt(3)*u[60]-b[60] , 'g-')
plt.plot(x, np.sqrt(3)*u[100]-b[100], 'k-')
plt.show()


plt.plot(u[0], b[0], 'r--')
plt.plot(u[5], b[5], 'c--')
plt.plot(u[20],b[20], 'c-')
plt.plot(u[50],b[50], 'b-')
plt.plot(u[70],b[70], 'g-')
plt.plot(u[100],b[100], 'k-')
plt.show()


ax = plt.subplot(121)
ax.plot(np.log(l), np.log(E[0][0:n]), 'r--', label='initial data')
ax.plot(np.log(l), np.log(E[10][0:n]), 'm-', label='t = 0.1')
ax.plot(np.log(l), np.log(E[30][0:n]), 'b-', label='t = 0.3')
ax.plot(np.log(l), np.log(E[50][0:n]), 'g-', label='t = 0.5')
ax.set_title('log(k) - log(E_u(k,t)) plot')

legend = ax.legend(loc='best', shadow=True, fontsize='small')


ax1 = plt.subplot(122)

ax1.plot(np.log(l), np.log(E1[0][0:n]), 'r--', label='initial data')
ax1.plot(np.log(l), np.log(E1[10][0:n]), 'm-', label='t = 0.1')
ax1.plot(np.log(l), np.log(E1[30][0:n]), 'b-', label='t = 0.3')
ax1.plot(np.log(l), np.log(E1[50][0:n]), 'g-', label='t = 0.5')
ax1.set_title('log(k) - log(E_b(k,t)) plot')

legend = ax1.legend(loc='best', shadow=True, fontsize='small')
plt.show()


z = np.linspace(3, 5, num=10)

_X = np.linspace(20, 199,num=180)
X = np.log(_X)
Y = np.linspace(20, 199,num=180)

time = 100
for j in range(180):
    Y[j] = np.log(E1[time][j+20])


slope, intercept, r, p_val, std_err = stats.linregress(X, Y)
print(slope)
plt.plot(z, z*slope+intercept, 'k-')
plt.plot(X, Y, 'g-')
plt.show()

fig2 = plt.figure()

x = np.linspace(0, 1, num=101)
A = np.zeros((101, 101))


ims = []
for k in range(100):
    ims.append(plt.plot(u[k],  b[k]))

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
                                   blit=True)
# To save this second animation with some metadata, use the following command:
# im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()
'''