#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 00:41:22 2018

@author: lengjiaqi
"""

#norm check, not go to energy level

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:57:16 2018

@author: lengjiaqi
"""

#this program computes the Fourier transform of the solution of viscous burgers equation. 
#the data is obtained by viscous-splitting 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=10001)
y = np.erf(x) + 1
z = np.exp(-x*x)
g = y/z

'''
f = 1/(1 + y/z)
h = x*f
plt.plot(x, h)
plt.show()


fhat = np.fft.rfft(f)
fhat1 = abs(fhat)
k = np.linspace(0, 5000, num=5001)
plt.plot(np.log(k), np.log(fhat1))
plt.plot([np.log(33)], [np.log(fhat1[33])], 'o')
plt.plot([np.log(70)], [np.log(fhat1[70])], 'o')
dy = np.log(fhat1[70]) - np.log(fhat1[33])
dx = np.log(70) - np.log(33)
slope = dy/dx
plt.show()
print(slope)


hhat = np.fft.rfft(h)
hhat1 = abs(hhat)
k = np.linspace(0, 5000, num=5001)
plt.plot(np.log(k), np.log(hhat1))
plt.plot([np.log(33)], [np.log(hhat1[33])], 'o')
plt.plot([np.log(70)], [np.log(hhat1[70])], 'o')
dy = np.log(hhat1[70]) - np.log(hhat1[33])
dx = np.log(70) - np.log(33)
slope = dy/dx
plt.show()
print(slope)
'''

x1 = np.linspace(1, 100, num=1000)
decay = 1/(1 + x1 + np.power(x1, 2))
plt.plot(np.log(x1), np.log(decay))
plt.show()

