import numpy as np
import matplotlib.pyplot as plt

# a) X(t) = e^t, y(t) = cos(t)
def curve_a(t):
    return np.exp(t), np.cos(t)

def tangent_a(t):
    x0, y0 = np.exp(np.pi/4), np.cos(np.pi/4)
    slope = (-np.sqrt(2)/2) / np.exp(np.pi/4)
    return x0 + t, y0 + slope * (t)

# b) X(t) = 3t^2, y(t) = t^3
def curve_b(t):
    return 3 * t**2, t**3

def tangent_b(t):
    x0, y0 = 12, 8
    slope = 1
    return x0 + t, y0 + slope * (t)

# c) X(t) = sin(t), y(t) = 4t
def curve_c(t):
    return np.sin(t), 4 * t

def tangent_c(t):
    x0, y0 = 1, 2 * np.pi
    return np.full_like(t, 1), y0 + 4 * (t)

# d) X(t) = t^2, y(t) = e^2
def curve_d(t):
    return t**2, np.full_like(t, np.exp(2))

def tangent_d(t):
    x0, y0 = 1, np.exp(2)
    return x0 + t, np.full_like(t, y0)

# Graficar curvas y tangentes
t_vals = np.linspace(0, 4, 400)

# a)
x_a, y_a = curve_a(t_vals)
x_tan_a, y_tan_a = tangent_a(t_vals - np.pi/4)

plt.plot(x_a, y_a, label="Curva a")
plt.plot(x_tan_a, y_tan_a, label="Tangente a", linestyle="--")
plt.title("Curva a y Tangente")
plt.legend()
plt.grid(True)
plt.show()

# b)
x_b, y_b = curve_b(t_vals)
x_tan_b, y_tan_b = tangent_b(t_vals - 2)

plt.plot(x_b, y_b, label="Curva b")
plt.plot(x_tan_b, y_tan_b, label="Tangente b", linestyle="--")
plt.title("Curva b y Tangente")
plt.legend()
plt.grid(True)
plt.show()

# c)
x_c, y_c = curve_c(t_vals)
x_tan_c, y_tan_c = tangent_c(t_vals - np.pi/2)

plt.plot(x_c, y_c, label="Curva c")
plt.plot(x_tan_c, y_tan_c, label="Tangente c", linestyle="--")
plt.title("Curva c y Tangente")
plt.legend()
plt.grid(True)
plt.show()

# d)
x_d, y_d = curve_d(t_vals)
x_tan_d, y_tan_d = tangent_d(t_vals - 1)

plt.plot(x_d, y_d, label="Curva d")
plt.plot(x_tan_d, y_tan_d, label="Tangente d", linestyle="--")
plt.title("Curva d y Tangente")
plt.legend()
plt.grid(True)
plt.show()
