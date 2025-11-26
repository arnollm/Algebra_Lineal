import numpy as np

matriz1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 0, 1]
])

#calcular matriz pseudoinversa
matriz1_pseudo = np.linalg.pinv(matriz1)

#mostrar la matriz original y la pseudoinversa
print("matriz original:\n",matriz1)
print("matriz pseudoinversa:\n",matriz1_pseudo)

#ejecutar la comprobacion
comprobacion = matriz1.dot(matriz1_pseudo).dot(matriz1)

#mostrar la comprobacion :)
print("comprobacion:\n",comprobacion)