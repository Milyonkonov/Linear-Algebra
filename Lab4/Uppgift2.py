import sympy
import numpy as np
import time

# 2a)--------------------------------------------------------------------------------------------------------------
print("2a)")

# A är ekvationssystemets matris
A = sympy.Matrix(  [[1, 2, 1, -1, 2, 0],
                    [3, 4, 5, 2, 0, 0],
                    [2, 2, 1, 0, 2, 0]])

# x4 = s, s-vektorn är vektorn som multipliceras med parametern s i den parametriska formeln för x.
sVector = A.rref()[0].col(3) * -1                   # Den tredje kolumnen i matrisen på reducerad trappstegsform ger en riktningsvektor till spannet.
sVector = sVector.row_insert(3, sympy.Matrix([1]))  # Om s = x4 medför det att s-vektorns fjärde komponent är 1
sVector = sVector.row_insert(4, sympy.Matrix([0]))  # x5 = t så den har ingen korrelation till s-vektorn

# x5 = t
tVector = A.rref()[0].col(4) * -1             # Ännu en riktningsvektor till spannet, t-vektorn. Dessa två vektorer bildar ett plan.
tVector = tVector.row_insert(3, sympy.Matrix([0]))  # x4 = s så ingen korrelation till t-vektorn
tVector = tVector.row_insert(4, sympy.Matrix([1]))  # Om t = x5 medför det att t-vektorns fjärde komponent är 1

print("x = s * {0} + t * {1}".format(sVector, tVector))
print() # Blankrad

# 2b)--------------------------------------------------------------------------------------------------------------
print("2b)")

# Skriver ut tiden det tog att utföra rref() på matrisen med storlek m=n=mSize genererad med random.rand()
def PrintTimeForRand(mSize):
    timeBeforeRand = time.time()
    sympy.Matrix(np.random.rand(mSize, mSize+1)).rref()
    print("Tid för random.rand med matrisstorlek {0}: {1} sekunder.".format(mSize, time.time() - timeBeforeRand))

# Skriver ut tiden det tog att utföra rref() på matrisen med storlek m=n=mSize genererad med random.randint()
def PrintTimeForRandint(mSize, maxint):
    timeBeforeRand = time.time()
    sympy.Matrix(np.random.randint(maxint, size=(mSize, mSize+1))).rref()
    print("Tid för random.randint med matrisstorlek {0}: {1} sekunder.".format(mSize, time.time() - timeBeforeRand))


# Vi märkte att random.rand-metoden tog ungefär 61 sekunder på vår dator. Vilket visas av följande:
PrintTimeForRand(100)

# Men att random.randint-metoden aldrig blev klar...
# Följande kod ökar successivt matrisstorleken så det går att märka när randint inte längre blir klar
# För oss skedde detta vid en 25x25 matris.

# Öka matrisstorleken succesivt
for i in range(1, 100):
    PrintTimeForRand(i)
    PrintTimeForRandint(i, 3) # Ni skrev att vi skulle använda randint men inte i vilket span, vi valde 0-3.
    print() # Blankrad