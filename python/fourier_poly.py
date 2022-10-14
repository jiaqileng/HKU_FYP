#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 19:42:48 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

#real fft
N = 10000
x = np.linspace(-10,10,num=N+1)
'''
y = x*(x-1)*(x-1/2)

xrhat = np.abs(np.fft.rfft(x))
yrhat = np.fft.rfft(y)
yrhat_abs = abs(yrhat)

plt.plot(y)
plt.title('Function f(x) on [0,1]')
plt.show()

k = np.linspace(0, 500, num=501)
plt.plot(np.log(k), np.log(yrhat_abs),'k')
plt.title('log(k)-log(f_hat) plot, N = 1,000')
plt.show()


#fft
xhat = np.abs(np.fft.rfft(x))
yhat = np.fft.fft(y)
yhat_abs = abs(yhat)

plt.plot(y)
plt.title('Function f(x) on [0,1]')
plt.show()

k = np.zeros(N+1)
n = int(N/2)
for i in range(n+1):
    k[i] = i

for i in range(n+1, N+1):
    k[i] = N - i

plt.plot(np.log(k), np.log(yhat_abs),'k')
plt.title('log(k)-log(f_hat) plot, N = 10,000')
plt.show()
'''
y = 1/(x*x + 1)
plt.plot(x, y)
plt.show()

f = abs(np.fft.rfft(y))
k = np.linspace(0, 5000, num=5001)
plt.plot(np.log(k), np.log(f))
plt.show()