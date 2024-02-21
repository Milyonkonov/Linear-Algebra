from scipy import linalg as LA
import sympy
import numpy as np
import time

A = sympy.Matrix( [[1, 2, 1, -1, 2],
             [3, 4, 5, 2, 0],
             [2, 2, 1, 0, 2]])

zero = sympy.Matrix([[0], [0], [0]])

s = A.rref()[0].col(3) * -1
s = s.row_insert(3, sympy.Matrix([1]))
s = s.row_insert(4, sympy.Matrix([0]))

t = A.rref()[0].col(4) * -1
t = t.row_insert(3, sympy.Matrix([0]))
t = t.row_insert(4, sympy.Matrix([1]))

print("2a)")
print("x = s * {0} + t * {1}".format(s, t))
print()

timeBeforeRand = time.time()
print(sympy.Matrix(np.random.rand(100, 101)).rref())
print(time.time() - timeBeforeRand)
timeBeforeRand = time.time()
print(sympy.Matrix(np.random.randint(5, size=(100, 101))).rref())
print(time.time() - timeBeforeRand)