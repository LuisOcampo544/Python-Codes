import numpy as np
import matplotlib.pyplot as plt

# Definir los rangos de t
t = np.linspace(0, 2 * np.pi, 1000)

def plot_curve(x, y, title):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# 1. Circunferencia
r = 1
x_circ = r * np.cos(t)
y_circ = r * np.sin(t)
plot_curve(x_circ, y_circ, "Circunferencia")

# 2. Cicloide
x_cicloide = r * (t - np.sin(t))
y_cicloide = r * (1 - np.cos(t))
plot_curve(x_cicloide, y_cicloide, "Cicloide")

# 3. Hipocicloide
R = 5  # Radio de la rueda fija
r_h = 3  # Radio de la rueda móvil
x_hipo = (R - r_h) * np.cos(t) + r_h * np.cos((R - r_h) / r_h * t)
y_hipo = (R - r_h) * np.sin(t) - r_h * np.sin((R - r_h) / r_h * t)
plot_curve(x_hipo, y_hipo, "Hipocicloide")

# 4. Astroide
x_astroide = r * np.cos(t)**3
y_astroide = r * np.sin(t)**3
plot_curve(x_astroide, y_astroide, "Astroide")

# 5. Lemniscata de Bernoulli
a = 1
x_lemniscata = a * np.cos(t) / (1 + np.sin(t)**2)
y_lemniscata = a * np.sin(t) * np.cos(t) / (1 + np.sin(t)**2)
plot_curve(x_lemniscata, y_lemniscata, "Lemniscata")

# 6. Cardioide
x_cardioide = a * (1 - np.cos(t)) * np.cos(t)
y_cardioide = a * (1 - np.cos(t)) * np.sin(t)
plot_curve(x_cardioide, y_cardioide, "Cardioide")
