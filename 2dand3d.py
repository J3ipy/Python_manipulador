import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from tkinter import Tk, Label, Button, Scale, Frame, colorchooser
import time

# Global variables for visualization options
link_color = 'green'  # Default color for elos
joint_color = 'black'  # Default color for joints
marker_size = 10  # Default size for joint markers
link_width = 8  # Default width for lines representing elos

# Funções para calcular coordenadas 2D e 3D
def calculate_joint_coordinates_2d(lengths, angles):
    num_joints = len(lengths)
    x = np.zeros(num_joints + 1)
    y = np.zeros(num_joints + 1)

    x[0] = 0
    y[0] = 0

    for i in range(num_joints):
        x[i + 1] = x[i] + lengths[i] * np.cos(np.sum(angles[:i + 1]))
        y[i + 1] = y[i] + lengths[i] * np.sin(np.sum(angles[:i + 1]))

    return x, y

def calculate_joint_coordinates_3d(lengths, angles):
    num_joints = len(lengths)
    joints = []

    joints.append((0, 0, 0))  # Primeira junta (origem)

    for i in range(num_joints):
        x = joints[-1][0] + lengths[i] * np.cos(np.sum(angles[:i + 1]))
        y = joints[-1][1] + lengths[i] * np.sin(np.sum(angles[:i + 1]))
        z = 0  # Assumindo movimento no plano XY (ajuste se necessário)

        joints.append((x, y, z))  # Adicionar nova junta

    return joints

# Funções para plotar o braço robótico em 2D e 3D
def plot_robot_arm_2d(lengths, angles, title="", show_grid=True):
    x, y = calculate_joint_coordinates_2d(lengths, angles)

    plt.figure(figsize=(6, 4))

    # Linhas representando os elos do braço robótico
    for i in range(len(lengths)):
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], link_color, linewidth=link_width)

    # Marcando as juntas
    for i in range(len(lengths) + 1):
        plt.plot(x[i], y[i], joint_color, markersize=marker_size, marker="o")

    # Configurações adicionais
    plt.axis('equal')
    plt.title(title)
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(show_grid)
    plt.show()

def plot_robot_arm_3d(lengths, angles, title="", show_grid=True):
    joints = calculate_joint_coordinates_3d(lengths, angles)

    # Criar lista de linhas para os elos
    lines = []
    for i in range(len(lengths)):
        lines.append(go.Scatter3d(x=[joints[i][0], joints[i + 1][0]],
                             y=[joints[i][1], joints[i + 1][1]],
                             z=[joints[i][2], joints[i + 1][2]],
                             mode='lines',
                             line=dict(color=link_color, width=link_width)))

    # Criar marcadores para as juntas
    markers = []
    for i in range(len(joints)):
        markers.append(go.Scatter3d(x=[joints[i][0]],
                                    y=[joints[i][1]],
                                    z=[joints[i][2]],
                                    mode='markers',
                                    marker=dict(size=marker_size, color=joint_color)))

    # Criar layout da figura
    layout = go.Layout(title=title,
                      scene=dict(xaxis=dict(showgrid=show_grid),
                                 yaxis=dict(showgrid=show_grid),
                                 zaxis=dict(showgrid=show_grid)),
                      showlegend=False)

    # Plotar a figura 3D
    fig = go.Figure(data=lines+markers, layout=layout)
    fig.show()

# Exemplo de uso:
lengths = [3, 2, 1.5]  # Comprimentos dos elos
angles = np.deg2rad([30, 45, -60])  # Ângulos dos elos em radianos

plot_robot_arm_2d(lengths, angles, title="Braço Robótico 2D")
plot_robot_arm_3d(lengths, angles, title="Braço Robótico 3D")
