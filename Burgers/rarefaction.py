#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:44:03 2019

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(1, 100, num = 10001)
t = np.sqrt(2)+1

d = 8*np.power(np.pi,4)*t*np.power(k,4)
wave = (1-np.cos(2*np.pi*k*t))/d

plt.plot(np.log(k), np.log(wave))
plt.show()

wave_bar = np.zeros(10001)

for i in range(10, 8000):
    indices = [i-10, i-8, i-6, i-4, i-2, i, i+2, i+4, i+6, i+8, i+10]
    wave_bar[i] = wave[indices].sum()/11
    
plt.plot(np.log(k), np.log(wave_bar))
plt.show()

