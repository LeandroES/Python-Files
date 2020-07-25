import numpy
#Actividad #2 numpy

AP = np.array([np.random.uniform(10, 50) for i in range(24)]).reshape(6,4)
np.savetxt('AP-Actividad2-Numpy.csv', AP, delimiter=',', header = 'a, b, c, d')

AR = np.array([np.random.uniform(10, 50) for i in range(24)]).reshape(6,4)
np.savetxt('AR-Actividad2-Numpy.csv', AR, delimiter=',', header = 'a, b, c, d')

data = np.genfromtxt('AP-Actividad2-Numpy.csv', delimiter=',', names = True)
#print("Imprimiendo informacion - Actividad numpy 2 AP: ", data)

data = np.genfromtxt('AR-Actividad2-Numpy.csv', delimiter=',', names = True)
#print("Imprimiendo informacion - Actividad numpy 2 AR: ", data)

def rmse(predicted, actual):
    return np.sqrt(((predicted - actual) ** 2).mean())

rmse_val = rmse(AP, AR)
print("RMSE: ", (rmse_val))