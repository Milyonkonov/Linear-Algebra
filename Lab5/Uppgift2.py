import numpy as np
import numpy.linalg as LA

taskaB = np.array([[9, 5],
              [1, 5]])

taskbA = np.random.rand(500, 500)
taskbB = taskbA + taskbA.transpose()

def RayleighQuotient (B, b):
    if (LA.norm(b) != 1):
        #print ("b is not a unit vector! It has length {0}".format(LA.norm(b)))
        print("Converting b to unit vector...")
        b /= LA.norm(b)

    return b.transpose() @ B @ b

# Returns a tuple, first with the eigenvalue, then a nparray with the eigenvector
def PowerIteration(B, p):
    v = np.random.rand(B.shape[0], 1) # v0 = random vector
    lastRayleighQuotient = 81927389

    while (abs(lastRayleighQuotient - RayleighQuotient(B, v)) >= 10**-p):
        lastRayleighQuotient = RayleighQuotient(B, v)
        v = B @ v
        v /= LA.norm(v)
    
    eigenValue = LA.norm(B@v) / LA.norm(v)
    return (eigenValue, v)

# 2a)
#print(PowerIteration(taskaB, 100))
#print(LA.eig(taskaB))

# 2b)
ourEig = PowerIteration(taskbB, 100)
numpyEig = LA.eig(taskbB)
print("Our function eigenvalue: {0} | numpy eigenvalue: {1}".format(
    ourEig[0], numpyEig.eigenvalues[0]))

print(LA.norm((taskbA @ ourEig[1]) - ourEig[0] * ourEig[1]))