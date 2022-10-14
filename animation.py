#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:15 2019

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




fig2 = plt.figure()

x = np.linspace(0, 1, num=101)
A = np.zeros((101, 101))

for i in range(100):
    A[i] = (1-i/100)*np.sin(2*np.pi*x)


ims = []
for j in range(100):
    ims.append(plt.plot(x, A[j]))

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
                                   blit=True)
# To save this second animation with some metadata, use the following command:
# im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()