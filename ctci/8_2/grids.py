import itertools
import random

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm

GRID1 = [4, 6]
OFFLIMITS1 = [
    (0, 5),
    (1, 1),
    (1, 2),
    (2, 4)
]

GRID2 = [4, 6]
OFFLIMITS2 = [
    (0, 5),
    (1, 1),
    (1, 2),
    (2, 4),
    (3, 3)
]

GRID3 = [4, 6]
OFFLIMITS3 = [
    (0, 5),
    (1, 1),
    (1, 2),
    (2, 4),
    (3, 3),
    (2, 5)
]

def create_random_offlimits(grid_size, probability_of_offlimits, random_seed=None):
    if random_seed:
        random.seed(random_seed)
    rows = grid_size[0]
    columns = grid_size[1]
    start_point = (0, 0)
    goal_point = (rows - 1, columns - 1)
    total_points = list(itertools.product(range(rows), range(columns)))
    num_points_to_return = round(len(total_points) * probability_of_offlimits)
    points_to_return = random.sample(total_points, num_points_to_return)

    return [p for p in points_to_return if p != goal_point and p != start_point]

def plot_grid(grid_size, offlimits):
    board = np.zeros(grid_size)
    for point in offlimits:
        board[point] = 1
    row_labels = range(grid_size[0])
    col_labels = range(grid_size[1])
    plt.matshow(board, cmap=cm.Greys)
    plt.xticks(range(grid_size[1]), col_labels)
    plt.yticks(range(grid_size[0]), row_labels)
    plt.tick_params(axis="x", bottom=True, top=False, labelbottom=True, labeltop=False)
    plt.title("Robot maze with {} rows, {} columns, and {} off-limits blocks".format(grid_size[0], grid_size[1], len(offlimits)))
    plt.show()
