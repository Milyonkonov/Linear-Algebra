import numpy as np
import matplotlib.pyplot as plt

ex = np.array([[1], [0]])
egg = np.array([[0.58], [-0.82]])

A1 = np.array([[0, 0],
               [0, 0.16]])

A2 = np.array([[0.85, 0.04],
               [-0.04, 0.85]])

A3 = np.array([[0.2, -0.26],
               [0.23, 0.22]])

A4 = np.array([[-0.15, 0.28],
               [0.26, 0.24]])

A_matrices = [A1, A2, A3, A4]

b1 = np.array([[0], [0]])
b2 = np.array([[0], [1.6]])
b3 = np.array([[0], [1.6]])
b4 = np.array([[0], [0.44]])

b_translations = [b1, b2, b3, b4]

def nVector(n, v0, a_matrix, translation):
    vn = v0
    for i in range(1, n+1):
        vn = a_matrix@vn + translation
    
    return vn

def prettyColor ():
    for i in range (0, 1000):
        testVector = nVectorRandom(i, egg)
        plt.scatter(testVector[0], testVector[1])

def generateIndex ():
    r = np.random.rand(1)[0]
    if (r < 0.01):
        return 0
    elif (r > 0.01 and r <= 0.86):
        return 1
    elif (r > 0.86 and r <= 0.93):
        return 2
    elif (r > 0.93):
        return 3
    else:
        return 0

def nVectorRandom(n, v0):
    vn = v0
    for i in range(1, n+1):
        index = generateIndex()
        vn = A_matrices[index]@vn + b_translations[index]
    
    return vn

prettyColor()
plt.show()