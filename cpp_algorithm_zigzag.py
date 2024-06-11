import numpy as np
import matplotlib.pyplot as plt

def zigzag_path(width, height, step):
    path = []
    x, y = 0, 0
    direction = 1

    while y < height:
        path.append((x, y))
        x += direction * step

        if x >= width or x < 0:
            direction *= -1
            x += direction * step
            y += step

    return path

def plot_path(path):
    path = np.array(path)
    plt.figure(figsize=(5, 4))
    plt.plot(path[:, 0], path[:, 1], marker='o')
    plt.title('Zigzag Path')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

width, height, step = 10, 5, 1
path = zigzag_path(width, height, step)
plot_path(path)
