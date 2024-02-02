import numpy as np
import matplotlib.pyplot as plt

point = [np.pi, np.e, 1]
normal = [1, 1, 1]
u = [1, 1, 0]
v = [0, -1, 0]
normal = np.cross(u, v)

A = normal[0]
B = normal[1]
C = normal[2]

#def x1(y, z): return (-B*y - C*z) / A
#def y1(x, z): return (-A*x - C*z) / B
def z1(x, y): return (-A*x - B*y) / C

def projectionOfPoint(p, n):
    projectionOnNormal = (np.dot(p, n) / np.dot(n, n)) * n

    return p - projectionOnNormal

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, z1(X, Y), color='red', alpha=0.5)
ax.plot(point[0], point[1], point[2], color="blue", marker="o")
t = projectionOfPoint(point, normal)
ax.plot(t[0], t[1], t[2], color="blue", marker="o")

plt.show()

