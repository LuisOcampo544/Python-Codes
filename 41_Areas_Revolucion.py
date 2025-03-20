import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definición de la curva paramétrica
def x(t):
    return 4 * np.cos(t)

def y(t):
    return 8 * np.sin(8 * t)

# Derivadas de x(t) y y(t)
def dx_dt(t):
    return -4 * np.sin(t)

def dy_dt(t):
    return 64 * np.cos(8 * t)

# Longitud diferencial ds
def ds(t):
    return np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)

# Integrando para calcular la superficie de revolución
def integrand(t):
    return x(t) * ds(t)

# Calcular la superficie de revolución
surface, _ = quad(lambda t: 2 * np.pi * integrand(t), 0, 2 * np.pi)

# Graficar la curva paramétrica
t_vals = np.linspace(0, 2 * np.pi, 1000)
x_vals = x(t_vals)
y_vals = y(t_vals)

plt.plot(x_vals, y_vals, label="Curva C(t)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Curva paramétrica y superficie de revolución")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()

print(f"Superficie de revolución: {surface:.2f}")
