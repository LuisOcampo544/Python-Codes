import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir parámetros de la elipse (huevo)
a = 5  # semieje mayor
b = 3  # semieje menor

# Funciones para el cálculo de superficies de revolución
# 1. Orientación vertical
def integrand_vertical(t):
    return a * np.cos(t) * np.sqrt((a**2) * (np.sin(t))**2 + (b**2) * (np.cos(t))**2)

# 2. Orientación horizontal
def integrand_horizontal(t):
    return b * np.sin(t) * np.sqrt((b**2) * (np.sin(t))**2 + (a**2) * (np.cos(t))**2)

# Integración numérica en el intervalo [0, 2pi]
S_vertical, _ = quad(integrand_vertical, 0, 2 * np.pi)
S_horizontal, _ = quad(integrand_horizontal, 0, 2 * np.pi)

# Superficies de revolución
S_vertical *= 2 * np.pi
S_horizontal *= 2 * np.pi

print("Superficie de revolución en orientación vertical:", S_vertical)
print("Superficie de revolución en orientación horizontal:", S_horizontal)

# Graficar la elipse en ambas orientaciones y su revolución
fig = plt.figure(figsize=(12, 6))

# Gráfico en orientación vertical
ax1 = fig.add_subplot(121, projection='3d')
t = np.linspace(0, 2 * np.pi, 100)
x_vert = a * np.cos(t)
y_vert = b * np.sin(t)
ax1.plot(x_vert, y_vert, zs=0, zdir='z', label="Perfil de la elipse (vertical)", color='b')

# Revolución en orientación vertical
theta = np.linspace(0, 2 * np.pi, 100)
T, Theta = np.meshgrid(t, theta)
X = a * np.cos(T) * np.cos(Theta)
Y = a * np.cos(T) * np.sin(Theta)
Z = b * np.sin(T)
ax1.plot_surface(X, Y, Z, color='cyan', alpha=0.5)
ax1.set_title("Superficie de revolución en orientación vertical")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# Gráfico en orientación horizontal
ax2 = fig.add_subplot(122, projection='3d')
x_hor = b * np.cos(t)
y_hor = a * np.sin(t)
ax2.plot(x_hor, y_hor, zs=0, zdir='z', label="Perfil de la elipse (horizontal)", color='g')

# Revolución en orientación horizontal
X = b * np.cos(T) * np.cos(Theta)
Y = b * np.cos(T) * np.sin(Theta)
Z = a * np.sin(T)
ax2.plot_surface(X, Y, Z, color='lightgreen', alpha=0.5)
ax2.set_title("Superficie de revolución en orientación horizontal")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

plt.show()
