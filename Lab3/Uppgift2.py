import numpy as np

A = np.array([[0.7, 0.1, 0.3],
              [0.1, 0.6, 0.2],
              [0.2, 0.3, 0.5]])

# Returnerar vektorn n = Matrix * vektorn (n - 1) och vektorn 0 = v0.
def vn(matrix, v0, n):
    nvector = v0 # n = 0 => vektorn n = vektorn 0
    for i in range(0, n):
        nvector = matrix@nvector # Egentligen vektorn i = A * vektorn (i - 1)
    return nvector # i = n => vektorn i = nvector = vector n

# Skriver bara ut vn efter vid vissa veckorintervall, självförklarande
def WeekVectorSequence(v0):
    print("Efter 1 vecka: ")
    print(vn(A, v0, 1))

    print("Efter 10 veckor: ")
    print(vn(A, v0, 10))

    print("Efter 100 veckor: ")
    print(vn(A, v0, 100))

    print("Efter 1000 veckor: ")
    print(vn(A, v0, 1000))

    print("Efter 10000 veckor: ")
    print(vn(A, v0, 10000))

    print("Efter 100000 veckor: ")
    print(vn(A, v0, 100000))


even = np.array([[1 / 3],
                 [1 / 3],
                 [1 / 3]])

allCentral = np.array([ [1],
                        [0],
                        [0]])

allLandvetter = np.array([  [0],
                            [1],
                            [0]])

allRented = np.array([  [0],
                        [0],
                        [1]])

print("\nMed jämnt antal bilar på varje station i vecka 0:")
WeekVectorSequence(even)

print("\nMed alla bilar på Centralen i vecka 0:")
WeekVectorSequence(allCentral)

print("\nMed alla bilar på Landvetter i vecka 0:")
WeekVectorSequence(allLandvetter)

print("\nMed alla bilar redan uthyrda i vecka 0:")
WeekVectorSequence(allRented)

# Kan kontrollera att mängden bilar består
#print(vn(A, even, 100)[0][0] + vn(A, even, 100)[1][0] + vn(A, even, 100)[2][0])