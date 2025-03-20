import numpy as np
import matplotlib.pyplot as plt

# Definimos las funciones paramétricas
def curva_a(t):
    x = 2 * np.cos(t)
    y = 2 * np.sin(t)
    return x, y

def curva_b(t):
    x = np.ones_like(t)  # x = 1 en todo el intervalo
    y = 3 * t**2
    z = t**3
    return x, y, z

def curva_c(t):
    x = np.sin(3*t)
    y = np.cos(3*t)
    z = 2 * t**(3/2)
    return x, y, z

# Corregimos la curva d: (t, t, t^2)
def curva_d(t):
    x = t
    y = t
    z = t**2
    return x, y, z

# Corregimos la curva e: (t, t*sin(t), t*cos(t))
def curva_e(t):
    x = t
    y = t * np.sin(t)
    z = t * np.cos(t)
    return x, y, z

# Rango de valores de t para cada curva
t_a = np.linspace(0, 2*np.pi, 400)
t_b = np.linspace(0, 1, 400)
t_c = np.linspace(0, 1, 400)
t_d = np.linspace(1, 2, 400)
t_e = np.linspace(0, np.pi, 400)

# Graficar cada curva
fig = plt.figure(figsize=(10, 8))

# Curva a
x_a, y_a = curva_a(t_a)
plt.subplot(231)  # Subplot 2 filas, 3 columnas, 1a posición
plt.plot(x_a, y_a, label='Curva a')
plt.title('Curva a: (2cos(t), 2sen(t))')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# Curva b
x_b, y_b, z_b = curva_b(t_b)
ax = fig.add_subplot(232, projection='3d')
ax.plot(x_b, y_b, z_b, label='Curva b')
ax.set_title('Curva b: (1, 3t^2, t^3)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Curva c
x_c, y_c, z_c = curva_c(t_c)
ax = fig.add_subplot(233, projection='3d')
ax.plot(x_c, y_c, z_c, label='Curva c')
ax.set_title('Curva c: (sin(3t), cos(3t), 2t^(3/2))')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Curva d corregida
x_d, y_d, z_d = curva_d(t_d)
ax = fig.add_subplot(234, projection='3d')
ax.plot(x_d, y_d, z_d, label='Curva d')
ax.set_title('Curva d: (t, t, t^2)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Curva e corregida
x_e, y_e, z_e = curva_e(t_e)
ax = fig.add_subplot(235, projection='3d')
ax.plot(x_e, y_e, z_e, label='Curva e')
ax.set_title('Curva e: (t, t*sin(t), t*cos(t))')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.tight_layout()
plt.show()
