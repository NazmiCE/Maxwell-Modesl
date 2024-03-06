import numpy as np
import matplotlib.pyplot as plt
beta = 15 # Time constant for 0.632 response (Process Control Knowledge)
t0 = 5*beta # Approximate time for full response
time_list = np.linspace(0,t0, t0+1)
time_list_2 = np.linspace(t0, t0*2, t0+2)
sigma = 100

E= 100
# Kelvin Model: Viscoelastic Model
e = sigma/E*(1 - np.exp(-time_list/beta))

e_a = sigma/E*(np.exp(-(time_list_2-t0)/beta) - np.exp(-time_list_2/beta))

plt.xlabel("Time")
plt.ylabel("Strain")

plt.plot(time_list,e)
plt.plot(time_list_2,e_a)
plt.show()

plt.xlabel("Strain")
plt.ylabel("Sigma")

plt.plot(e, [0] + [100 for i in range(75)])
plt.plot(e_a, [100] + [0 for i in range(75)])
plt.show()

