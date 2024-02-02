import numpy as np
import matplotlib.pyplot as plt

point = [np.pi, np.e, 1]
#normal = [1, 1, 1]
#u = [1, 1, 0]
#v = [0, -1, 0]
normal1 = [1, 1, 1]
normal2 = [3, 3, 3] # detta är fullkomligt korkat


#A = normal[0]
#B = normal[1]
#C = normal[2]

#def x1(y, z): return (-B*y - C*z) / A
#def y1(x, z): return (-A*x - C*z) / B
def z1(x, y, n): return (-n[0]*x - n[1]*y) / n[2]

def projectionOfPoint(p, n):
    projectionOnNormal = (np.dot(p, n) / np.dot(n, n)) * n

    return p - projectionOnNormal

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, z1(X, Y, normal1), color='red', alpha=0.5)
ax.plot_surface(X, Y, z1(X, Y, normal2), color='red', alpha=0.5)

ax.plot(point[0], point[1], point[2], color="blue", marker="o")

t = projectionOfPoint(point, normal1)
ax.plot(t[0], t[1], t[2], color="blue", marker="o")

t = projectionOfPoint(point, normal2)
ax.plot(t[0], t[1], t[2], color="blue", marker="o")

plt.show()

