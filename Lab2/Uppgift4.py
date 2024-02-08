import numpy as np
import matplotlib.pyplot as plt

#-----Definitioner-----
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
#----------------------

#-----funktioner-----
# Returnerar ett slumpmässigt index f.o.m. 0 t.o.m. 3 med olika sannolikhet
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

# Returnerar vn där { n = 0 => vn = v0 & n > 0 => vn = Av(n-1) + b } där A och b tillhör någon av 4 affina avbildningar.
def nVectorRandom(n, v0):
    vn = v0
    for i in range(1, n+1):         # Vi vill börja på index 1, men n=1 ska ändå köra loopen 1 gång, därför: range(1, n+1)
        index = generateIndex()     # Generera ett index som väljer en av de fyra affina avbildningarna.
        vn = A_matrices[index]@vn + b_translations[index]   # vi = A*v(i-1) + b     (Men där A och b är slumpmässigt valt av möjliga.)
    return vn   # vn innehåller inte den n:te vektorn förrän sista steget i loopen är utfört, men aja.
#--------------------

#-----Huvudkod-----
someVector = np.array([[1],[0]]) # Det visar sig att ursprungsvektorn inte spelar så stor roll för höga iterationer...

# En loop som ritar alla vektorer v0 till vn på figuren, där vi valt n=800 (extremt oeffektivt)
for i in range (0, 800):
    testVector = nVectorRandom(i, someVector)
    plt.scatter(testVector[0], testVector[1])
plt.show()
#------------------