import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def conv(a,b):
    N = a.shape[0]
    vec = np.zeros(2*N-1, dtype=complex)
    vec = signal.convolve(a,b)
    mid = vec[N-1]
    _vec = np.delete(vec, N-1)
    ls = np.split(_vec, 2)
    
    return np.append(ls[0]+ls[1], mid)



N = 200
M = 50000
T = 0.5
dt = T/M
dx = 1/N
s = dt/dx
r = dt/dx**2
v = 0.003


k = np.arange(0, N,1) #(0, ..., N-1)
l = np.arange(0, N/2 + 1,1) #(0, ..., N/2)
x = np.arange(0, 1, dx)
sin = np.sin(2*np.pi*k/N)
cos = np.cos(2*np.pi*k/N)
linear = 1+ 2*v*r*(cos-1)
'''
uhat_real = np.zeros(N)
uhat_imag = np.zeros(N)
alpha = 0.75

for j in range(1,6):
    uhat_real[j] = uhat_real[N-j] = 40 + 5*np.random.rand(1)
    uhat_imag[j] = uhat_imag[N-j] = 50 + 6*np.random.rand(1)


for i in range(6,int(N/2+1)):
    uhat_real[i] = uhat_real[N-i] = 223/np.power(i,alpha)
    uhat_imag[i] = uhat_imag[N-i] = 176/np.power(i,alpha)
    
'''
f = np.sin(2*np.pi*x)


F = np.zeros((M+1, N), dtype=complex)

F[0] = np.fft.fft(f)/N
#F[0] = uhat_real/N

for i in range(M):
    F[i+1] = F[i] * linear - 1j*s*conv(F[i], sin*F[i])
'''    
    if (i%1000 == 0):
       plt.plot(k, (F[i+1]).imag, 'r--')
       plt.plot(k, np.abs(conv(F[i], sin*F[i])), 'b--')
       plt.show()
'''    

E = np.abs(F)**2

n = int(N/2 + 1)

plt.plot(np.log(l), np.log(E[0, 0:n]), 'r--')
#plt.plot(np.log(l), np.log(E[1000, 0:n]), 'b-')
#plt.plot(np.log(l), np.log(E[3000, 0:n]), 'g-')
plt.plot(np.log(l), np.log(E[50000, 0:n]), 'c-')
plt.title('log(k)-log(E) plot, new method')
plt.show()
'''
plt.plot(l, np.log(E[0, 0:n]), 'r--')
plt.plot(l, np.log(E[1000, 0:n]), 'b-')
plt.plot(l, np.log(E[3000, 0:n]), 'g-')
plt.plot(l, np.log(E[5000, 0:n]), 'c-')
plt.show()
'''

'''
plt.plot(x, np.fft.ifft(N*F[0]), 'r--')
plt.plot(x, np.fft.ifft(N*F[10000]), 'b-')
plt.plot(x, np.fft.ifft(N*F[30000]), 'g-')
plt.plot(x, np.fft.ifft(N*F[50000]), 'c-')
plt.show()

ims1 = []
ims2 = []

fig1 = plt.figure()

for j in range(500):
    ims1.append(plt.plot(x, np.fft.ifft(N*F[40*j]), 'b-'))

im_ani = animation.ArtistAnimation(fig1, ims1, interval=50, repeat_delay=3000,
                                   blit=True)
plt.title('Evolution in physical space')
im_ani.save('physical_space.mp4', metadata={'artist':'Guido'})
plt.show()



fig2 = plt.figure()

for p in range(500):
    ims2.append(plt.plot(np.log(l), np.log(E[40*p, 0:n]), 'r-'))

im_ani2 = animation.ArtistAnimation(fig2, ims2, interval=50, repeat_delay=3000,
                                   blit=True)

plt.title('Evolution in frequency space')
im_ani2.save('frequency_space.mp4', metadata={'artist':'Guido'})
plt.show()

'''

