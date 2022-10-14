#!/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Sat Dec  8 22:14:34 2018

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,1,num=11)

for i in range(10):
    a[i] = i
    
print(a[10])