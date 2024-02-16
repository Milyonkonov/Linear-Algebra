import numpy as np

A = np.array([[0.7, 0.1, 0.3],
              [0.1, 0.6, 0.2],
              [0.2, 0.3, 0.5]])

even = np.array([[1 / 3],
                 [1 / 3],
                 [1 / 3]])

def vn(matrix, v0, recursions):
    nvector = v0
    for i in range(0, recursions):
        nvector = matrix@nvector
    return nvector

print(vn(A, even, 100000))

# Kan kontrollera att mängden bilar består
#print(vn(A, even, 100)[0][0] + vn(A, even, 100)[1][0] + vn(A, even, 100)[2][0])