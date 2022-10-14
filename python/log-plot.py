#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:51:56 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, num=100)
y = np.log(x)
z = x * y

plt.plot(x, y)
plt.plot(x, z)
plt.show()