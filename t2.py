import numpy as np
import matplotlib.pyplot as plt
from MHD_68 import MHD_solver

x = np.linspace(0,1,num=1001)

#construct u-hat
uhat_real = np.zeros(1001)
uhat_imag = np.zeros(1001)
alpha = 1
beta = 1

for k in range(6):
    uhat_real[k] = uhat_real[1000-k] = 40 + 5*np.random.rand(1)
    uhat_imag[k] = uhat_imag[1000-k] = 50 + 6*np.random.rand(1)


for i in range(6,501):
    uhat_real[i] = uhat_real[1000-i] = 223/np.power(i,alpha)
    uhat_imag[i] = uhat_imag[1000-i] = 176/np.power(i,alpha)
    
uhat = uhat_real +1j * uhat_imag


#construct b-hat
bhat_real = np.zeros(1001)
bhat_imag = np.zeros(1001)

for l in range(4):
    bhat_real[l] = bhat_real[1000-l] = 87 + 10*np.random.rand(1)
    bhat_imag[l] = bhat_imag[1000-l] = 93 + 13*np.random.rand(1)


for j in range(4,501):
    bhat_real[j] = bhat_real[1000-j] = 472/np.power(j,beta)
    bhat_imag[j] = bhat_imag[1000-j] = 430/np.power(j,beta)
    
bhat = bhat_real +1j * bhat_imag


f = np.fft.ifft(uhat)
g = np.fft.ifft(bhat)
h = 0*x

u, b = MHD_solver(0.01, 0.01/100, 0.5, 1000, 100000, f, h)

#plot u(t,x)
fig, ax = plt.subplots()
ax.plot(x, u[0], 'r--', label='initial data')
ax.plot(x, u[10000], 'b-', label='t = 0.1')
ax.plot(x, u[50000], 'g-', label='t = 0.5')
ax.plot(x, u[70000], 'k-', label='t = 0.7')

legend = ax.legend(loc='best', shadow=True, fontsize='small')

plt.show()

#plot b(t,x)
fig, ax = plt.subplots()
ax.plot(x, b[0], 'r--', label='initial data')
ax.plot(x, b[30000], 'b-', label='t = 0.3')
ax.plot(x, b[50000], 'g-', label='t = 0.5')
ax.plot(x, b[70000], 'k-', label='t = 0.7')
legend = ax.legend(loc='best', shadow=True, fontsize='small')
plt.show()



#write the data/solution to a file.
with open("t2_u_burgers1.txt","w") as w:
    for i in range(101):
        for j in range(1001):
            w.write(str(u[1000*i][j]) + " ")
        w.write("\n")
