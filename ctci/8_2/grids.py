import itertools
import random

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
