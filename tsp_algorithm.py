import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt


def tsp_solver(coordinates):
    dist_matrix = distance_matrix(coordinates, coordinates)

    G = nx.from_numpy_array(dist_matrix)

    tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)

    return tsp_path, [coordinates[i] for i in tsp_path]


def plot_tsp_path(coordinates, path, tsp_path):
    coordinates = np.array(coordinates)
    path = np.array(path)

    plt.figure(figsize=(5, 4))
    plt.scatter(coordinates[:, 0], coordinates[:, 1], color='red', s=100)  # 크기 키움

    for i in range(len(tsp_path) - 1):
        plt.plot([coordinates[tsp_path[i], 0], coordinates[tsp_path[i + 1], 0]],
                 [coordinates[tsp_path[i], 1], coordinates[tsp_path[i + 1], 1]],
                 color='blue', alpha=0.7)
        plt.annotate(f'{i + 1}', ((coordinates[tsp_path[i], 0] + coordinates[tsp_path[i + 1], 0]) / 2,
                                  (coordinates[tsp_path[i], 1] + coordinates[tsp_path[i + 1], 1]) / 2),
                     fontsize=12, color='blue')

    plt.plot([coordinates[tsp_path[-1], 0], coordinates[tsp_path[0], 0]],
             [coordinates[tsp_path[-1], 1], coordinates[tsp_path[0], 1]],
             color='blue', alpha=0.7)
    plt.annotate(f'{len(tsp_path)}', ((coordinates[tsp_path[-1], 0] + coordinates[tsp_path[0], 0]) / 2,
                                      (coordinates[tsp_path[-1], 1] + coordinates[tsp_path[0], 1]) / 2),
                 fontsize=12, color='blue')

    for i in range(len(tsp_path) - 1):
        plt.arrow(coordinates[tsp_path[i], 0], coordinates[tsp_path[i], 1],
                  coordinates[tsp_path[i + 1], 0] - coordinates[tsp_path[i], 0],
                  coordinates[tsp_path[i + 1], 1] - coordinates[tsp_path[i], 1],
                  head_width=0.3, length_includes_head=True, color='blue', alpha=0.5)

    plt.arrow(coordinates[tsp_path[-1], 0], coordinates[tsp_path[-1], 1],
              coordinates[tsp_path[0], 0] - coordinates[tsp_path[-1], 0],
              coordinates[tsp_path[0], 1] - coordinates[tsp_path[-1], 1],
              head_width=0.3, length_includes_head=True, color='blue', alpha=0.5)

    plt.title('TSP Path')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend(['Points', 'TSP Path'], loc='upper left')
    plt.show()


coordinates = [[1, 2], [2, 4], [3, 1], [6, 5], [7, 8]]
tsp_path, path = tsp_solver(coordinates)
print(f"최단 경로: {path}")
plot_tsp_path(coordinates, path, tsp_path)
