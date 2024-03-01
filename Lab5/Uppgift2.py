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
    
    newRayleighQuotient = RayleighQuotient(B, v) # Deklarera variabel innan loop.
    newRayleighQuotient = 7272 # TODO WTF

    # Fortsätt loopen så länge rayleighkvoten inte är precis nog.
    while (abs(newRayleighQuotient - RayleighQuotient(B, v)) >= 10**-p):
        newRayleighQuotient = RayleighQuotient(B, v)
        v = B @ v
        v /= LA.norm(v)
    
    eigenValue = LA.norm(B@v) / LA.norm(v) # lambda * v = Bv => lambda = |Bv| / |v|
    return (eigenValue, v)

# 2a)
print("2a)")
taskaB = np.array([ [9, 5],
                    [1, 5]])

ourEig = PowerIteration(taskaB, 300)
numpyEig = LA.eig(taskaB)
print(ourEig[1])
print(numpyEig.eigenvectors)
print("Vårt beräknade egenvärde: {0} | numpys egenvärde: {1} \n".format(
    ourEig[0], numpyEig.eigenvalues[0]))

# 2b)
print("2b)")
taskbA = np.random.rand(500, 500)
taskbB = taskbA + taskbA.transpose()

ourEig = PowerIteration(taskbB, 100)
print("Vårt beräknade egenvärde: {0}\n".format(ourEig[0]))

print(LA.norm((taskbA @ ourEig[1]) - ourEig[0] * ourEig[1]))