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

class Path:

    def __init__(self, path_str, board):
        self.path_str = path_str
        self.ending_point = self.get_ending_point(self.path_str)
        self.board = board
        self.is_goal_path = self.board.is_goal(self.ending_point)
    
    def __eq__(self, p):
        return self.path_str == p.path_str
    
    def __repr__(self):
        return self.path_str
    
    def __str__(self):
        return self.path_str
    
    def __len__(self):
        return len(self.path_str)
    
    def __lt__(self, p):
        return len(self) < len(p)
    
    def __hash__(self):
        return hash(repr(self))
    
    def get_ending_point(self, path_str):
        i = path_str.count('D')
        j = path_str.count('R')

        return (i, j)
    
    def right_path(self):
        right_path_str = self.path_str + 'R'
        right_path_ending_point = self.get_ending_point(right_path_str)
        if self.board.is_off_limits(right_path_ending_point):
            return None
        else:
            return Path(self.path_str + 'R', self.board)
    
    def down_path(self):
        down_path_str = self.path_str + 'D'
        down_path_ending_point = self.get_ending_point(down_path_str)
        if self.board.is_off_limits(down_path_ending_point):
            return None
        else:
            return Path(self.path_str + 'D', self.board)

class Robot:

    def __init__(self, board):
        self.board = board
        self.paths_to_explore = [Path('R', self.board), Path('D', self.board)]
        self.failed_paths = set()
        self.successful_path = None
    
    def explore_next_path(self):
        if self.successful_path:
            return
        if not self.paths_to_explore:
            self.successful_path = 'F'
            return
        next_path = sorted(self.paths_to_explore, key=lambda x: len(x)).pop()
        if next_path.is_goal_path:
            self.successful_path = next_path
            return

        right_path = next_path.right_path()
        down_path = next_path.down_path()
        if right_path and right_path not in self.failed_paths:
            self.paths_to_explore.append(right_path)
        else:
            self.failed_paths.add(right_path)
        if down_path and down_path not in self.failed_paths:
            self.paths_to_explore.append(down_path)
        else:
            self.failed_paths.add(down_path)

        if right_path in self.failed_paths and down_path in self.failed_paths:
            self.failed_paths.add(next_path)
            self.paths_to_explore.remove(next_path)
    
    def find_path(self):
        while not self.successful_path:
            self.explore_next_path()


if __name__ == "__main__":
    board1 = Board(GRID1, OFFLIMITS1)
    robot1 = Robot(board1)
    robot1.find_path()
    print("Grid 1 path:", robot1.successful_path)
    
    board2 = Board(GRID2, OFFLIMITS2)
    robot2 = Robot(board2)
    robot2.find_path()
    print("Grid 2 path:", robot2.successful_path)

    board3 = Board(GRID3, OFFLIMITS3)
    robot3 = Robot(board3)
    robot3.find_path()
    print("Grid 3 path:", robot3.successful_path)
