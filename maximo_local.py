import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear un rango de valores para x e y
x = np.linspace(-10, 15, 100)  # Ajusta los límites para una buena visualización
y = np.linspace(-10, 15, 100)
x, y = np.meshgrid(x, y)

# Definir la función f(x, y)
z = -y**2 - (3/4)*x**2 + 11*x + 18*y - 70

# Coordenadas del punto crítico
x_critical = 22 / 3
y_critical = 9
z_critical = -y_critical**2 - (3/4)*x_critical**2 + 11*x_critical + 18*y_critical - 70

# Crear la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie de la función
surface = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

# Marcar el punto crítico
ax.scatter(x_critical, y_critical, z_critical, color='red', s=50, label='Máximo Local')

# Añadir las etiquetas de datos en la gráfica
text_str = (
    f"Punto Crítico:\n"
    f"x = {x_critical:.2f}\n"
    f"y = {y_critical:.2f}\n"
    f"z = {z_critical:.2f}\n"
    
)
ax.text2D(-0.10, 0.95, text_str, transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle="round", alpha=0.5))

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')

# Cambiar el ángulo de vista
elev = 45  # Elevación
azim = 120  # Rotación
ax.view_init(elev=elev, azim=azim)  # Ajusta elevación y rotación de la cámara

# Título
ax.set_title('Gráfico de la función f(x, y) y el Máximo Local')

# Leyenda
ax.legend()

# Guardar la gráfica como imagen
plt.savefig("/home/decker/Documentos/Carpeta.py/grafico_maximo_local.png")

# Mostrar la gráfica
plt.show()
