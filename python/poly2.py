#Initial data of the type single sine curve & t-uhat plot.
import numpy as np
import matplotlib.pyplot as plt

# Input other values.
v = 0.1
T = 0.05
N1 = 300
N2 = 10000
dx = 1/N1
dt = T/N2
r = v*dt/np.power(dx,2)
b = 2*dt/dx

print("The von Neumann coefficient is")
print(r)

# Initialize the mesh grid.
x = np.linspace(0, 1, num=N1+1)
u0 = 2600*(x*(x-1/3)*(x-2/5)*(x-6/7)*(x-13/17)*(x-1)*(x-2) - 373/299880)
B0 = 2600*(np.power(x, 8)/8 - 9559*np.power(x, 7)/12495 + 6571*np.power(x, 6)/3570 - 4049*np.power(x, 5)/1785 + 365*np.power(x, 4)/238 - 2956*np.power(x, 3)/5355 + 52*np.power(x, 2)/595 - 373*x/299880)
f = np.exp(-B0/(2*v))


# Define and input the initial data.
H = np.zeros((N2+1, N1+1))
j = 0
while j < N1+1:
    H[0, j] = f[j] 
    j += 1
    
    
#perform the corresponding numerical scheme;
i = 0; j = 1
    
while i < N2:
    H[i+1, 0] = (1 - 2*r) * H[i, 0] + r*(H[i,1] + H[i, N1-1])
    while j < N1-1:
        H[i+1, j] = (1 - 2*r) * H[i, j] + r*(H[i,j+1] + H[i, j-1])
        j += 1
            
    H[i+1, j] = (1 - 2*r) * H[i, j] + r*(H[i,0] + H[i, j-1])
    H[i+1, j+1] = H[i+1, 0]
    j = 1
    i += 1
    

#derive the viscous solution from heat equation

p = - v/dx

u = np.zeros((N2+1, N1+1))

i = 0; j = 1
    
while i < N2+1:
    u[i, 0] = 2*p*(H[i, 1] - H[i,0])/H[i,0]
    while j < N1:
        u[i, j] = p*(H[i, j+1] - H[i, j-1])/H[i,j]
        j += 1
    
    u[i,j] = u[i, j-1]
    j = 1
    i += 1


#plot the viscous solutions
plt.plot(x, H[0,], "r-")
plt.plot(x, H[5000,],'b-')
plt.title("x-H plot: the solution")
plt.show()

#plot the viscous solutions
plt.plot(x, u[0,], "r-")
plt.plot(x, u[5000,],'b-')
plt.title("x-u plot: the solution")
plt.show()

y = np.linspace(0, 151, num=151)

#plot the viscous solutions
A = np.abs(np.fft.rfft(u[1000,]))
B = np.abs(np.fft.rfft(u[3000,]))


plt.plot(np.log(y), np.log(np.fft.rfft(u[0,])), "r-")
plt.plot(np.log(y), np.log(A),'b-')
plt.plot(np.log(y), np.log(B),'g-')
plt.plot(np.log(y), np.log(np.fft.rfft(u[4000,])),'k-')
plt.title("kogx-kogu plot: the solution")
plt.show()



