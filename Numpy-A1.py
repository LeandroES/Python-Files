import numpy as np

#Actividad #1 numpy
A = np.array([np.random.uniform(0.0, 1.0) for i in range(24)]).reshape(6,4)
np.savetxt('Actividad1-Numpy.csv', A, delimiter=',', header = 'a, b, c, d')
data = np.genfromtxt('Actividad1-Numpy.csv', delimiter=',', names = True)
#print("Imprimiendo informacion - Actividad numpy 1: ", data)

B = np.arange(24).reshape(3,8)

def sigmoid(x):
  return (1 / (1 + np.exp(-x)))

C = np.array(sigmoid(B)).ravel()
L = []
#for i in range(len(C)):
for j in C:
    if j > 0.5 in C:
        L.append(j)
        T = tuple(L)

print("Valores mayores a 0.5 del Array C",T)