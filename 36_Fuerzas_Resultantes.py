import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Valores calculados
F1_x = 114.6
F1_y = 0
F1_z = 80.3

F2_x = 0
F2_y = 0
F2_z = 60

F3_x = -115.2
F3_y = 0
F3_z = 111.2

R_x = -0.6
R_y = 0
R_z = 251.5

# Creamos el diagrama 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujamos las fuerzas
ax.quiver(0, 0, 0, F1_x, F1_y, F1_z, color='r', label='F1 (140 N)')
ax.quiver(0, 0, 0, F2_x, F2_y, F2_z, color='g', label='F2 (60 N)')
ax.quiver(0, 0, 0, F3_x, F3_y, F3_z, color='b', label='F3 (160 N)')

# Dibujamos la resultante
ax.quiver(0, 0, 0, R_x, R_y, R_z, color='k', linestyle='dashed', label='Resultante')

# Ajustamos los límites del gráfico
ax.set_xlim([-200, 200])
ax.set_ylim([-200, 200])
ax.set_zlim([-50, 300])

# Añadimos leyenda y títulos
ax.legend()
ax.set_title('Diagrama de fuerzas en 3D')
ax.set_xlabel('Componente X (N)')
ax.set_ylabel('Componente Y (N)')
ax.set_zlabel('Componente Z (N)')

# Mostramos el gráfico
plt.show()