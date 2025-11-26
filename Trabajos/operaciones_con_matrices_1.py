#hola profe la verdad no tome nota de las matrices en clase pero igual voy a intentar con matrices propias :)
import numpy as np

#definir matrices
matriz1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

matriz2 = np.array([
    [9, 42, 7],
    [13, 4, 25],
])

matriz3 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

#suma
resultado = matriz1 + matriz2
print("suma: \n",resultado)

#resta
resultado = matriz1 - matriz2
print("resta: \n",resultado)

#multiplicacion
resultado = np.dot(matriz1, matriz3)
print("multiplicacion: \n",resultado)