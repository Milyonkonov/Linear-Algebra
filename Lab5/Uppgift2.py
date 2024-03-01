import numpy as np
import numpy.linalg as LA

# Returnerar ett tal, rayleighkvoten av angiven matris och vektor.
def RayleighQuotient (B, b):

    # Säkerställning att b är en enhetsvektor
    if (B.shape[0] == b.shape[0] and abs(1 - LA.norm(b)) <= 0.001):
        return b.transpose() @ B @ b    # Returnera rayleighkvoten
    else:
        print("Argument till rayleighkvot-funktion är ogiltiga!")
        exit()

# Returnerar en tuple med (största egenvärde, tillhörande egenvektor)
def PowerIteration(B, p):
    v = np.random.rand(B.shape[0], 1)   # v0 = random vector
    v /= LA.norm(v)                     # v0 måste också vara normaliserad

    while (True):
        oldRayleighQuotient = RayleighQuotient(B, v) # Spara rayleighkvoten av iterationen före, för precisionsjämförning senare.
        v = B @ v       
        v /= LA.norm(v)

        # Avbryt loopen ifall rayleighkvoten är precis nog.
        if (abs(oldRayleighQuotient - RayleighQuotient(B, v)) <= 10**-p):
            break
    
    eigenValue = LA.norm(B@v) / LA.norm(v) # lambda * v = Bv => lambda = |Bv| / |v|
    return (eigenValue, v)

# 2a)
print("2a)")
B = np.array([ [9, 5],
                    [1, 5]])

ourEig = PowerIteration(B, 10)
numpyEig = LA.eig(B)

print("Vårt beräknade egenvärde: {0} | numpys egenvärde: {1} \n".format(ourEig[0], numpyEig.eigenvalues[0]))

# 2b)
print("2b)")
A = np.random.rand(500, 500)
B = A + A.transpose()

ourEig = PowerIteration(B, 10)
print("Vårt beräknade egenvärde: {0}\n".format(ourEig[0]))

print("Av - (lambda)v = {0}".format(LA.norm((A @ ourEig[1]) - ourEig[0] * ourEig[1])))