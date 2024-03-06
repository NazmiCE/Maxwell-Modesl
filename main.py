import numpy as np
import matplotlib.pyplot as plt

# All parameters are implemented to have a quick understanding

beta = 15 # Time constant for 0.632 response (Process Control Knowledge)
t0 = 5*beta # Approximate time for full respons # E/n n is viscosity (Dashpot)
sigma = 1 # Constant Stress (For simplicity linear increase can easily be modeled by 
            # using laplace transform check notes in your lab notebook) (Take suggestions to include forces not stresses)
E = 100 # Elastic Modulus of Cells Spring Elastic Property



# 1D motion
cell_size = 100
cell_center = 50 # Center in x direction
strain = 0
drawing_data = [] # Every ten iteration the center data will be taken for illustration

for i in range(100): # Number of iterations for Migration
    time_list = np.linspace(0, t0, t0+1)
    time_list_2 = np.linspace(t0 + 1, t0*2 + 1, t0+1)

    # Kelvin Model: Viscoelastic Model
    # Straining (Back place is constant front elongates)
    e = sigma/E*(1 - np.exp(-time_list/beta))
    cell_size_deformed = (cell_size + cell_size*e)
    cell_center += cell_size*e[-1]/2
    # Relaxation (Front is constant back shortens)
    e_a = sigma/E*(np.exp(-(time_list_2-t0)/beta) - np.exp(-time_list_2/beta))
    cell_size_deformed_a = (cell_size + cell_size*e_a)
    cell_center += cell_size*e_a[0]/2
    
    if i % 10 == 0:
        drawing_data.append([cell_center, i*2*t0])


plt.plot(np.array(drawing_data)[:,1], np.array(drawing_data)[:,0])
plt.xlabel("Time")
plt.ylabel("Cell Center")
plt.show()
