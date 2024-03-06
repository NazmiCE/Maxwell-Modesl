import numpy as np
import matplotlib.pyplot as plt


def creep_assign_sigma(t, to):
    if t < to:
        sigma = 100
    else:
        sigma = 0
    return sigma

def ramp_assign_sigma(t, to, a):
    if t < to:
        sigma = a*t
    else:
        sigma = a*to - a*(t-to)


# Creep
# de/dt + e/B = sigma/n
E = 100
n = 1500
B = n/E
e = 0
creep_data = [[e,0,0]]
for t in range(0, 150):
    sigma = creep_assign_sigma(t, 75)
    de = sigma/n - e/B # de is de/dt term
    e += de
    creep_data.append([e, t+1,sigma])


plt.plot(np.array(creep_data)[:,0], np.array(creep_data)[:,2])
plt.xlabel("Strain")
plt.ylabel("Sigma")
plt.show()

