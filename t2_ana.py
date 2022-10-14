#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:36:14 2019

@author: lengjiaqi
"""

import numpy as np
import matplotlib.pyplot as plt
from MHD_68 import get_matrix
from scipy import stats


x = np.linspace(0, 1, num=1001)
k = np.linspace(0, 500, num=501)


u = get_matrix("t2_u.txt")
b = get_matrix("t2_b.txt")
u_bur = get_matrix("t2_u_burgers1.txt")

#compute the energy spectra
_u = np.zeros((101, 501))
_b = np.zeros((101,501))
_u_bur = np.zeros((101,501))


for i in range(101):
    _u[i] = np.abs(np.fft.rfft(u[i])/1000)**2
    _b[i] = np.abs(np.fft.rfft(b[i])/1000)**2
    _u_bur[i] = np.abs(np.fft.rfft(u_bur[i])/1000)**2
            

#figure 1: u & b
ax = plt.subplot(121)
ax.plot(x, u[0], 'r--', label='initial data')
ax.plot(x, u[10], 'm-', label='t=0.05')
ax.plot(x, u[50], 'b-', label='t=0.25')
ax.plot(x, u[90], 'c-', label='t=0.45')
ax.set_title('u(x,t)')

ax1 = plt.subplot(122)
ax1.plot(x, b[0], 'r--', label='initial data')
ax1.plot(x, b[10], 'm-', label='t=0.05')
ax1.plot(x, b[50], 'b-', label='t=0.25')
ax1.plot(x, b[90], 'c-', label='t=0.45')
ax1.set_title('b(x,t)')

legend = ax1.legend(loc='best', shadow=True, fontsize='large')
plt.show()

#figure 2: k - log E_u/log E_b, t = 0.1

ax3 = plt.subplot(121)
ax3.plot(k, np.log(_u[0]), 'r--')
ax3.plot(k, np.log(_u[20]), 'm-')
ax3.set_title('k-log(E_u), t=0.1')

ax4 = plt.subplot(122)
ax4.plot(k, np.log(_b[0]), 'r--', label='initial data')
ax4.plot(k, np.log(_b[10]), 'm-', label="t = 0.1")
ax4.set_title('k-log(E_b), t=0.1')

legend = ax4.legend(loc='best', shadow=True, fontsize='large')
plt.show()



#figure 3: k - log E_u/log E_b, t = 0.3
ax5 = plt.subplot(121)
ax5.plot(k, np.log(_u[0]), 'r--')
ax5.plot(k, np.log(_u[60]), 'b-')
ax5.set_title('k-log(E_u), t=0.3')

ax6 = plt.subplot(122)
ax6.plot(k, np.log(_b[0]), 'r--', label='initial data')
ax6.plot(k, np.log(_b[60]), 'b-', label="t = 0.3")
ax6.set_title('k-log(E_b), t=0.3')

legend = ax6.legend(loc='best', shadow=True, fontsize='large')

plt.show()



#figure 4: logk - log E_u, t = 0.1 & 0.4

z = np.linspace(2.3, 4, num=10)

Xpre = np.linspace(10, 54,num=45)
X = np.log(Xpre)
Y1 = np.linspace(10, 54,num=45)
Y2 = np.linspace(10, 54,num=45)
    
for j in range(45):
    Y1[j] = np.log(_u[20,j+10])
    Y2[j] = np.log(_u[80,j+10])


slope1, intercept1, r1, p_val, std_err = stats.linregress(X, Y1)
slope2, intercept2, r2, p_val, std_err = stats.linregress(X, Y2)


ax7 = plt.subplot(121)
ax7.plot(np.log(k), np.log(_u[0]), 'r--', label='initial data')
ax7.plot(np.log(k), np.log(_u[20]), 'm-', label='t=0.1')
ax7.plot(z, slope1*z+intercept1, 'k--')
ax7.text(0, -25, 'slope = %.3f' %(slope1))
ax7.text(0, -28, 'r-squared = %.3f' %(r1**2))
ax7.text(4, -15, 'initial')
ax7.text(4, -17, 'slope = -3')
ax7.set_title('log(k)-log(E_u), t=0.1')

ax8 = plt.subplot(122)
ax8.plot(np.log(k), np.log(_u[60]), 'y-', label='t=0.3')
ax8.plot(np.log(k), np.log(_u[80]), 'g-', label="t=0.4")
ax8.plot(z, slope2*z+intercept2, 'k--')
ax8.text(0, -25, 'slope = %.3f' %(slope2))
ax8.text(0, -28, 'r-squared = %.3f' %(r2**2))
ax8.set_title('log(k)-log(E_u), t=0.4')

legend = ax7.legend(loc='best', shadow=True, fontsize='medium')
legend = ax8.legend(loc='best', shadow=True, fontsize='medium')
plt.show()

#figure 5: u_burgers, for reference
ax9 = plt.subplot(121)
ax9.plot(k, np.log(_u_bur[0]), 'r--', label = 'initial data')
ax9.plot(k, np.log(_u_bur[20]), 'm-', label = 't=0.1')
ax9.plot(k, np.log(_u_bur[60]), 'b-', label = 't=0.3')
ax9.plot(k, np.log(_u_bur[80]), 'g-', label = 't=0.4')
ax9.set_title('k-log(E_u), with zero b')
legend = ax9.legend(loc='best', shadow=True, fontsize='medium')

ax10 = plt.subplot(122)
ax10.plot(np.log(k), np.log(_u_bur[0]), 'r--', label = 'initial data')
ax10.plot(np.log(k), np.log(_u_bur[20]), 'm-', label = 't=0.1')
ax10.plot(np.log(k), np.log(_u_bur[60]), 'b-', label = 't=0.3')
ax10.plot(np.log(k), np.log(_u_bur[80]), 'g-', label = 't=0.4')
ax10.set_title('log(k)-log(E_u), with zero b')
legend = ax10.legend(loc='best', shadow=True, fontsize='medium')
plt.show()
