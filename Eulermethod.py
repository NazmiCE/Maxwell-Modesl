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
    return sigma

# Ramp
# de/dt + e/B = sigma/n
E = 75
n = 100
B = n/E
e = 0
a = 1
creep_data = [[0,0,0]]
for t in np.arange(0, 36.5, 0.5):
    sigma = ramp_assign_sigma(t, 18, a)
    de = sigma/n - e/B # de is de/dt term
    e += de*0.5
    #print(de)
    creep_data.append([sigma, e, t])
    print([sigma,e])


plt.plot(np.array(creep_data)[:,1], np.array(creep_data)[:,0])
plt.title("EulerMethod Ramp Function E = 200 unit, n = 100 unit")
plt.xlabel("Strain")
plt.ylabel("Sigma")
plt.show()

