#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:20:56 2019

@author: lengjiaqi
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, num= 201)
k = np.arange(0, 101, 1)
f = np.sin(100*np.pi*x)

for i in range(10):
    print(i)
    
    for j in range(11):
        print(i+j)
    print('----')
        