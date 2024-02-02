import numpy

s = 0
for i in range(0, 100, 1):
    s += pow(-1, i) / (2*i + 1)
print(s*4)
