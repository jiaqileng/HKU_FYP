#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:31:00 2019

@author: lengjiaqi
"""
x = np.linapce()
fig = plt.figure()
fig.plot(np.log(l), np.log(E[0, 0:n]), 'r--')
fig.plot(np.log(l), np.log(E[10000, 0:n]), 'b-')
fig.plot(np.log(l), np.log(E[30000, 0:n]), 'g-')
fig.plot(np.log(l), np.log(E[50000, 0:n]), 'c-')
fig.title('log(k) - log(E_u(k,t)) plot')

legend = fig.legend(loc='best', shadow=True, fontsize='large')
plt.show()