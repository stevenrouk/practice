from grids import GRID1, OFFLIMITS1, GRID2, OFFLIMITS2, GRID3, OFFLIMITS3

class Board:

    def __init__(self, grid, off_limits):
        self.grid = grid
        self.off_limits = off_limits
        self.goal = (self.grid[0] - 1, self.grid[1] - 1)
    
    def is_off_limits(self, point):
        return (point in self.off_limits) or (point[0] > self.grid[0] - 1) or (point[1] > self.grid[1] - 1)
    
    def is_goal(self, point):
        return point == self.goal

class Robot:

    def __init__(self, board):
        self.board = board
        self.paths_to_explore = ['R', 'D']
        self.failed_paths = set()
        self.successful_path = None
    
    def explore_next_path(self):
        if self.successful_path:
            return
        if not self.paths_to_explore:
            self.successful_path = 'F'
            return
        next_path = sorted(self.paths_to_explore, key=lambda x: len(x)).pop()
        if self.board.is_goal(self.path_ending_point(next_path)):
            self.successful_path = next_path + 'S'
            return
        right_path = next_path + 'R'
        down_path = next_path + 'D'
        if not self.board.is_off_limits(self.path_ending_point(right_path)) and right_path not in self.failed_paths:
            self.paths_to_explore.append(right_path)
        else:
            self.failed_paths.add(right_path)
        if not self.board.is_off_limits(self.path_ending_point(down_path)) and down_path not in self.failed_paths:
            self.paths_to_explore.append(down_path)
        else:
            self.failed_paths.add(down_path)
        if right_path in self.failed_paths and down_path in self.failed_paths:
            self.failed_paths.add(next_path)
            self.paths_to_explore.remove(next_path)
    
    def path_ending_point(self, path):
        i = path.count('D')
        j = path.count('R')

        return (i, j)

if __name__ == "__main__":
    board1 = Board(GRID1, OFFLIMITS1)
    robot1 = Robot(board1)
    while not robot1.successful_path:
        robot1.explore_next_path()
    print("Grid 1 path:", robot1.successful_path)
    
    board2 = Board(GRID2, OFFLIMITS2)
    robot2 = Robot(board2)
    while not robot2.successful_path:
        robot2.explore_next_path()
    print("Grid 2 path:", robot2.successful_path)

    board3 = Board(GRID3, OFFLIMITS3)
    robot3 = Robot(board3)
    while not robot3.successful_path:
        robot3.explore_next_path()
    print("Grid 3 path:", robot3.successful_path)
