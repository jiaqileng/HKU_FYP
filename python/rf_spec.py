#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:19:05 2019

@author: lengjiaqi
"""
import numpy as np
import matplotlib.pyplot as plt

t = 0.1

x = np.arange(0,1000+0.001, 0.001)
f1 = 1/np.power(np.pi*x, 2)
f2 = np.sin(2*np.pi*x*t)/(2*t*np.power(np.pi*x, 3))
f3 = (1-np.cos(2*np.pi*x*t))/(8*t*t*np.power(np.pi*x, 4))
f = f1 - f2+ f3


plt.plot(np.log(x), np.log(f), 'k-')
plt.title('log-log plot when t = 0.1')
plt.show()


