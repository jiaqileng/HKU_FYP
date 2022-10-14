

import numpy as np
import matplotlib.pyplot as plt
from MHD_68 import get_matrix
from scipy import stats

x = np.linspace(0, 1, num=1001)
k = np.linspace(0, 200, num=201)


u = get_matrix("t1_u.txt")
b = get_matrix("t1_b.txt")


#compute the energy spectra
E = np.zeros((101, 400))
E1 = np.zeros((101,400))



for i in range(101):
    E[i] = np.abs(np.fft.fft(u[i])/1000)**2
    E1[i] = np.abs(np.fft.fft(b[i])/1000)**2
    

plt.plot(np.log(k), np.log(E[0, 0:201]), 'r--')
plt.plot(np.log(k), np.log(E[60, 0:201]), 'b-')
plt.plot(np.log(k), np.log(E[100, 0:201]), 'g-')
plt.show()
    
    
'''
#figure 1: u
ax = plt.subplot(121)
ax.plot(x, u1[0], 'r--', label='initial data')
ax.plot(x, u1[10], 'm-', label='t=0.05')
ax.plot(x, u1[50], 'g-', label='t=0.25')
ax.plot(x, u1[90], 'c-', label='t=0.45')
ax.set_title('u(x,t) with b_0')

ax1 = plt.subplot(122)
ax1.plot(x, u0[0], 'r--', label='initial data')
ax1.plot(x, u0[10], 'm-', label='t=0.05')
ax1.plot(x, u0[50], 'g-', label='t=0.25')
ax1.plot(x, u0[90], 'c-', label='t=0.45')
ax1.set_title('u(x,t) without b_0')

legend = ax1.legend(loc='best', shadow=True, fontsize='x-small')
plt.show()



#figure 2: b

fig, ax2 = plt.subplots()
ax2.plot(x, b1[0], 'r--', label='initial data')
ax2.plot(x, b1[10], 'm-', label='t = 0.05')
ax2.plot(x, b1[50], 'b-', label='t = 0.25')
ax2.plot(x, b1[90], 'g-', label='t = 0.45')
ax2.set_title('magnetic field b(x,t)')
legend = ax2.legend(loc='best', shadow=True, fontsize='small')

plt.show()

#figure 3: k - log E_u, t = 0.05 & 0.25

X = np.linspace(50, 100,num=51)
Y0 = np.linspace(50, 100,num=51)
Y1 = np.linspace(50, 100,num=51)

_X = np.linspace(10, 50,num=41)
_Y0 = np.linspace(10, 50,num=41)
_Y1 = np.linspace(10, 50,num=41)


for i in range(51):
    Y0[i] = np.log(E_u0[10,i+50])
    Y1[i] = np.log(E_u1[10,i+50])
    
for j in range(41):
    _Y0[j] = np.log(E_u0[50,j+10])
    _Y1[j] = np.log(E_u1[50,j+10])

slope0, intercept, r0, p_val, std_err = stats.linregress(X, Y0)
slope1, intercept, r1, p_val, std_err = stats.linregress(X, Y1)

_slope0, intercept, _r0, p_val, std_err = stats.linregress(_X, _Y0)
_slope1, intercept, _r1, p_val, std_err = stats.linregress(_X, _Y1)

ax3 = plt.subplot(221)
ax3.plot(k, np.log(E_u1[0]), 'r--')
ax3.plot(k, np.log(E_u1[10]), 'm-')
ax3.plot(X, X*slope1, 'k-')
ax3.text(100, -5, 'slope = %.3f' %(slope1))
ax3.text(100, -8, 'r-squared = %.3f' %(r1**2))

ax3.set_title('k-log(E_u), with b_0')

ax4 = plt.subplot(222)
ax4.plot(k, np.log(E_u0[0]), 'r--', label='initial data')
ax4.plot(k, np.log(E_u0[10]), 'm-', label="t = 0.1")
ax4.plot(X, X*slope0, 'k-')
ax4.text(100, -10, 'slope = %.3f' %(slope0))
ax4.text(100, -14, 'r-squared = %.3f' %(r0**2))
ax4.set_title('k-log(E_u), without b_0')

ax5 = plt.subplot(223)
ax5.plot(k, np.log(E_u1[0]), 'r--')
ax5.plot(k, np.log(E_u1[50]), 'b-')
ax5.plot(X, X*_slope1 + 5, 'k-')
ax5.text(100, -13, 'slope = %.3f' %(_slope1))
ax5.text(100, -16, 'r-squared = %.3f' %(_r1**2))


ax6 = plt.subplot(224)
ax6.plot(k, np.log(E_u0[0]), 'r--', label='initial data')
ax6.plot(k, np.log(E_u0[50]), 'b-', label="t = 0.5")
ax6.plot(X, X*_slope0 + 15, 'k-')
ax6.text(100, -15, 'slope = %.3f' %(_slope0))
ax6.text(100, -20, 'r-squared = %.3f' %(_r0**2))

legend = ax6.legend(loc='best', shadow=True, fontsize='small')
legend = ax4.legend(loc='best', shadow=True, fontsize='small')

plt.show()


#figure 4: k - log E_b, t = 0.1 & 0.5
fig, ax7 = plt.subplots()
ax7.plot(k, np.log(E_b1[0]), 'r--', label='initial data')
ax7.plot(k, np.log(E_b1[10]), 'm-', label="t = 0.1")
ax7.plot(k, np.log(E_b1[50]), 'b-', label="t = 0.1")
ax7.set_title('k-log(E_b)')

legend = ax7.legend(loc='best', shadow=True, fontsize='large')
plt.show()




#figure 5: logk - log E_u, t = 0.1 & 0.5
z = np.linspace(2.3, 4, num=10)

_Xpre = np.linspace(10, 50,num=41)
_Xl = np.log(_Xpre)
_Y0l = np.linspace(10, 50,num=41)
_Y1l = np.linspace(10, 50,num=41)
    
for j in range(41):
    _Y0l[j] = np.log(E_u0[50,j+10])
    _Y1l[j] = np.log(E_u1[50,j+10])


_slope0l, intercept, _r0l, p_val, std_err = stats.linregress(_Xl, _Y0l)
_slope1l, intercept, _r1l, p_val, std_err = stats.linregress(_Xl, _Y1l)

ax8 = plt.subplot(221)
ax8.plot(np.log(k), np.log(E_u1[0]), 'r--')
ax8.plot(np.log(k), np.log(E_u1[10]), 'm-')
ax8.set_title('log(k)-log(E_u), with b_0')

ax9 = plt.subplot(222)
ax9.plot(np.log(k), np.log(E_u0[0]), 'r--', label='initial data')
ax9.plot(np.log(k), np.log(E_u0[10]), 'm-', label="t = 0.1")
ax9.set_title('log(k)-log(E_u), without b_0')

ax10 = plt.subplot(223)
ax10.plot(np.log(k), np.log(E_u1[0]), 'r--')
ax10.plot(np.log(k), np.log(E_u1[50]), 'b-')
ax10.plot(z, z*_slope1l + 15, 'k-')
ax10.text(0, -20, 'slope = %.3f' %(_slope1l))
ax10.text(0, -23, 'r-squared = %.3f' %(_r1l**2))


ax11 = plt.subplot(224)
ax11.plot(np.log(k), np.log(E_u0[0]), 'r--', label='initial data')
ax11.plot(np.log(k), np.log(E_u0[50]), 'b-', label="t = 0.5")
ax11.plot(z, z*_slope0l + 8, 'k-')
ax11.text(0, -25, 'slope = %.3f' %(_slope0l))
ax11.text(0, -28, 'r-squared = %.3f' %(_r0l**2))

legend = ax11.legend(loc='best', shadow=True, fontsize='small')
legend = ax9.legend(loc='best', shadow=True, fontsize='small')

plt.show()
'''