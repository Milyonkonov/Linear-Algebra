import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def wave(w):
    q = w**2 - np.cos(w)
    return q

x=np.linspace(-1.5,1.5)
y=wave(x)
plt.plot(x,y)
plt.grid("on")

a = fsolve(wave, 3)
b = fsolve(wave, -1)

plt.plot(a, wave(a),"o")
plt.plot(b, wave(b),"o")

plt.show()