import numpy as np
import matplotlib.pyplot as plt

def spiral_path(radius, step):
    path = []
    x, y = 0, 0
    angle = 0

    while radius > 0:
        path.append((x, y))
        angle += step
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        radius -= step / (2 * np.pi)

    return path

def plot_path(path):
    path = np.array(path)
    plt.figure(figsize=(5, 4))
    plt.plot(path[:, 0], path[:, 1], marker='o')
    plt.title('Spiral Path')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

radius, step = 10, 0.1
path = spiral_path(radius, step)
plot_path(path)
