import numpy as np
import matplotlib.pyplot as plt

# Input other values.
v = 0.005
T = 0.5
N1 = 100
N2 = 50000
dx = 1/N1
dt = T/N2
r = v*dt/np.power(dx,2)

print("The von Neumann coefficient is")
print(r)


# Initialize the mesh grid.
x = np.linspace(0, 1-dx, num=N1)
f = np.sin(2*np.pi*x) + 3*np.sin(4*np.pi*x) 


# Define and input the initial data.
u = np.zeros((N2+1, N1))

u[0] = f

#perform the corresponding numerical scheme;
    
for i in range(N2):
    for j in range(N1):
        m_r = (j+1)%N1
        u[i+1,j] = u[i,j] - dt*u[i,j]*(u[i, m_r] - u[i,j-1])/(2*dx) + r*(u[i, m_r] + u[i,j-1] - 2*u[i,j])
        


#plot the solutions & check
plt.plot(x, u[0,], "r--")
plt.plot(x, u[10000,],'b-')
plt.plot(x, u[50000,],'g-')
plt.title("x-u plot: the solution")
plt.show()

uhat = np.zeros((N2+1, N1), dtype=complex)
E = np.zeros((N2+1, N1))
l = np.arange(0, N1/2 + 1,1)


for r in range(N2+1):
    uhat[r] = np.fft.fft(u[r])/N1
    
E = np.abs(uhat)**2

n = int(N1/2 + 1)

plt.plot(np.log(l), np.log(E[0, 0:n]), 'r--')
plt.plot(np.log(l), np.log(E[10000, 0:n]), 'b-')
plt.plot(np.log(l), np.log(E[30000, 0:n]), 'g-')
plt.plot(np.log(l), np.log(E[50000, 0:n]), 'c-')
plt.title('log(k)-log(E) plot, traditional method')
plt.show()



'''
#write the data/solution to a file.
#We only extract 1/1000 data from the giant matrix. The output should be a 501*501 matrix.
with open("hopf_cole.txt","w") as w:
    for i in range(501):
        for j in range(N1+1):
            w.write(str(u[1000*i][j]) + " ")
        w.write("\n")
'''