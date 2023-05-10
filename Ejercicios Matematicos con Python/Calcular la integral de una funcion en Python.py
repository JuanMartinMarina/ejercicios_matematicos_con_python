## Este código calcula la integral de la función f(x) = x^2 en el intervalo [0, 2] y muestra un gráfico de la función y su integral. 
## La integral se calcula usando la función trapz de NumPy, que implementa el método del trapecio para aproximar la integral.

import numpy as np
import matplotlib.pyplot as plt
plt.interactive(False)


# Pedimos al usuario que ingrese los límites de integración
a = float(input("Ingrese el límite inferior de integración: "))
b = float(input("Ingrese el límite superior de integración: "))

# Definimos la función a integrar
def f(x):
    return x**2

# Calculamos la integral usando la función trapz de numpy
resultado = np.trapz([f(x) for x in np.linspace(a, b, 1000)], dx=0.001)


# Mostramos el resultado
print(resultado)

# Graficamos la función y su integral
x = np.linspace(a, b, 1000)
y = [f(xx) for xx in x]

plt.plot(x, y)
plt.fill_between(x, y, color='gray', alpha=0.5)
plt.show()