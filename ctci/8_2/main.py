from grids import create_random_offlimits, plot_grid, GRID1, OFFLIMITS1, GRID2, OFFLIMITS2, GRID3, OFFLIMITS3
from solution_1 import find_path as find_path_solution_1
from solution_2 import Board as Board_solution_2, Robot as Robot_solution_2
from solution_3 import Board as Board_solution_3, Robot as Robot_solution_3, Path as Path_solution_3

def plot_random_grid():
    """Example of plotting robot maze."""
    grid = [15, 25]
    offlimits = create_random_offlimits(grid, 1/5, random_seed=42)
    plot_grid(grid, offlimits)

def generate_blocked_grid(nrows, ncols):
    nrows = 150
    ncols = 250
    grid = [nrows, ncols]
    offlimits = [(nrows-1, ncols-2), (nrows-2, ncols-1)]

    return grid, offlimits

if __name__ == "__main__":
    for i in range(20):
        print(i)
        grid = [10+i, 20+i]
        offlimits = create_random_offlimits(grid, 1/10, random_seed=42)

        # Solution 1
        print(find_path_solution_1(grid, offlimits))

        # Solution 2
        board = Board_solution_2(grid, offlimits)
        robot = Robot_solution_2(board)
        while not robot.successful_path:
            robot.explore_next_path()
        print(robot.successful_path)

        # Solution 3
        board = Board_solution_3(grid, offlimits)
        robot = Robot_solution_3(board)
        robot.find_path()
        print(robot.successful_path)
