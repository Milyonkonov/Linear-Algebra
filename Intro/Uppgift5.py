import numpy

s = 0
i = 0
while abs(4*s - numpy.pi) >= 0.5*pow(10, -5):
    s += pow(-1, i) / (2*i + 1)
    i += 1
print(f"{s} med {i-1} termer!")