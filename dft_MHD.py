import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def conv(a,b):
    N = a.shape[0]
    vec = np.zeros(2*N-1, dtype=complex)
    vec = signal.convolve(a,b)
    mid = vec[N-1]
    _vec = np.delete(vec, N-1)
    ls = np.split(_vec, 2)
    
    return np.append(ls[0]+ls[1], mid)



N = 1000
M = 100000
T = 0.1
dt = T/M
dx = 1/N
s = dt/dx
r = dt/dx**2
v = 0.0005
lbd = 0

k = np.arange(0, N,1) #(0, ..., N-1)
l = np.arange(0, N/2 + 1,1) #(0, ..., N/2)
x = np.arange(0, 1, dx)
sin = np.sin(2*np.pi*k/N)
cos = np.cos(2*np.pi*k/N)
linear1 = 1+ 2*v*r*(cos-1)
linear2 = 1+ 2*lbd*r*(cos-1)



step = np.ones(N)
step *= 2
for q in range(500):
    step[q] += 3

step2 = np.ones(N)
step2 *= 3
for r in range(500):
    step2[r] -= 2

    
e1 = step
e2 = step2

f = (e1 + e2)/2
g = (e1 - e2)/2

F = np.zeros((M+1, N), dtype=complex)
G = np.zeros((M+1, N), dtype=complex)

F[0] = np.fft.fft(f)/N
G[0] = np.fft.fft(g)/N

#F[0] = uhat_real/N

for i in range(M):
    if (i%1000==0):
        print(100*i/M)
    F[i+1] = F[i] * linear1 - 1j*s*(conv(F[i], sin*F[i]) - conv(G[i], sin*G[i]))
    G[i+1] = G[i] * linear2 - 1j*s*(conv(F[i], sin*G[i]) - conv(G[i], sin*F[i]))
    
    
u = np.zeros((M+1, N))
b = np.zeros((M+1, N))

for j in range(M+1):
    u[j] = np.fft.ifft(F[j]*N).real
    b[j] = np.fft.ifft(G[j]*N).real
    

#E = np.abs(F)**2
#E1 = np.abs(G)**2
#n = int(N/2 + 1)


i = j = 0
#write the data/solution to a file.
with open("t8_u.txt","w") as w:
    for i in range(101):
        for j in range(100):
            w.write(str(u[1000*i][10*j]) + " ")
        w.write("\n")
        
        
with open("t8_b.txt","w") as w:
    for i in range(101):
        for j in range(100):
            w.write(str(b[1000*i][10*j]) + " ")
        w.write("\n")

  
        
