import numpy as np
import matplotlib.pyplot as plt
import math
# All parameters are implemented to have a quick understanding
# Ramp Function
beta = 15 # Time constant for 0.632 response (Process Control Knowledge)
t0 = 5*beta # Approximate time for full respons # E/n n is viscosity (Dashpot)
sigma = 0 # Constant Stress (For simplicity linear increase can easily be modeled by 
            # using laplace transform check notes in your lab notebook) (Take suggestions to include forces not stresses)
E = 75 # Elastic Modulus of Cells Spring Elastic Property
n = 100
a = 2
K = a/E
step = 0.5
# 1D motion
cell_size = 100
cell_center = 50 # Center in x direction
strain = 0
drawing_data = [] # Every ten iteration the center data will be taken for illustration

for i in np.arange(0,9.5,step): # Number of iterations (t=i) for Migration

    # Kelvin Model: Viscoelastic Model
    # Straining (Back place is constant front elongates)
    e = K*i - K*n/E + K*n/E*math.exp(-E/n*i)
    sigma = a*i
    drawing_data.append([sigma, e])

emax = e
print(emax, "*********")

for i in np.arange(9.5,18.5,step): # Number of iterations (t=i) for Migration

    # Kelvin Model: Viscoelastic Model
    # Straining (Back place is constant front elongates)
    e = emax + (-K*(i-9.5) + K*n/E - K*n/E*math.exp(-E/n*(i-9.5)))
    
    sigma = sigma - a*step
    drawing_data.append([sigma, e])

print(drawing_data)

arrayy = np.array(drawing_data)
plt.plot(arrayy[:,1], arrayy[:,0])
plt.title("Laplace Transform Ramp E = 400, n = 100")
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.show()
