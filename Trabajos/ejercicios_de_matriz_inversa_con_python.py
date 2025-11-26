import numpy as np

#declaracion de matrices
matriz_1 = np.array([
    [4, 7],
    [2, 6]
])

matriz_2 = np.array([
    [3, 1],
    [4, 2]
])

matriz_3 = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

matriz_4 = np.array([
    [2, 5, 1],
    [4, 2, 3],
    [1, 3, 0]
])

#calcular la inversa y escribirla
inv_1 = np.linalg.inv(matriz_1)
print("Inversa Matriz 1:\n",inv_1)

inv_2 = np.linalg.inv(matriz_2)
print("\nInversa Matriz 2:\n",inv_2)

inv_3 = np.linalg.inv(matriz_3)
print("\nInversa Matriz 3:\n",inv_3)

inv_4 = np.linalg.inv(matriz_4)
print("\nInversa Matriz 4:\n",inv_4)
