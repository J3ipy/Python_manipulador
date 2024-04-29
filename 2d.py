import numpy as np
import matplotlib.pyplot as plt

def calculate_joint_coordinates(lengths, angles):
    """
    Calcula as coordenadas X e Y das juntas do braço robótico.

    Parâmetros:
        lengths (list): Lista com os comprimentos dos elos do manipulador.
        angles (list): Lista com os ângulos das juntas do braço robótico (em radianos).

    Retorna:
        tuple: Tupla contendo as coordenadas X e Y das juntas (x, y).
    """

    num_joints = len(lengths)
    x = np.zeros(num_joints + 1)
    y = np.zeros(num_joints + 1)

    x[0] = 0
    y[0] = 0

    for i in range(num_joints):
        x[i + 1] = x[i] + lengths[i] * np.cos(np.sum(angles[:i + 1]))
        y[i + 1] = y[i] + lengths[i] * np.sin(np.sum(angles[:i + 1]))

    return x, y

def plot_robot_arm(lengths, angles, title="Braço Robótico", show_grid=True):
    """
    Plota a figura do braço robótico na tela.

    Parâmetros:
        lengths (list): Lista com os comprimentos dos elos do manipulador.
        angles (list): Lista com os ângulos das juntas do braço robótico (em radianos).
        title (str, opcional): Título da figura (padrão: "Braço Robótico").
        show_grid (bool, opcional): Exibir ou não a grade no gráfico (padrão: True).
    """

    x, y = calculate_joint_coordinates(lengths, angles)

    plt.figure(figsize=(6, 4))

    # Linhas dos elos do braço robótico (Colorindo)
    for i in range(len(lengths)):
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], 'bo-')

    # Marcando as juntas (Colorindo)
    for i in range(len(lengths) + 1):
        plt.plot(x[i], y[i], 'ro')

    # Configurações adicionais
    plt.axis('equal')
    plt.title(title)
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(show_grid)
    plt.show()

# Exemplo de uso
lengths = [1, 0.2]  # Comprimentos dos elos
angles = [np.pi/4, np.pi/3]  # Ângulos das juntas

plot_robot_arm(lengths, angles, title="Braço Robótico com 2 Elos")
