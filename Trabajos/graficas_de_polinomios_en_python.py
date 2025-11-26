#hola otra vez profe igual voy a intentarlo con polinomios propios :)
import numpy as np
import matplotlib.pyplot as plt

#definir el rango de la funcion
x = np.linspace(-10, 10, 50)

#definir polinomio 1
y = x**2 - 50

#graficar
plt.grid(True)
plt.plot(x, y)
plt.show()


#definir polinomio 2
y = x**3 - x**2 + x - 500

#graficar
plt.grid(True)
plt.plot(x, y)
plt.show()

#definir polinomio 2
y = x + 70

#graficar
plt.grid(True)
plt.plot(x, y)
plt.show()