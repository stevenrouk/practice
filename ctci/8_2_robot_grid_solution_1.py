from grids import GRID1, OFFLIMITS1, GRID2, OFFLIMITS2, GRID3, OFFLIMITS3

def find_path(grid, off_limits):
    goal = (grid[0] - 1, grid[1] - 1)
    if goal == (0, 1):
        return 'RS'
    if goal == (1, 0):
        return 'DS'
    
    if (1, 0) not in off_limits and grid[0] > 1:
        new_grid = [grid[0] - 1, grid[1]]
        new_off_limits = [(x[0] - 1, x[1]) for x in off_limits]
        potential_path = 'D' + find_path(new_grid, new_off_limits)
        if potential_path[-1] == 'S':
            return potential_path
    
    if (0, 1) not in off_limits and grid[1] > 1:
        new_grid = [grid[0], grid[1] - 1]
        new_off_limits = [(x[0], x[1] - 1) for x in off_limits]
        potential_path = 'R' + find_path(new_grid, new_off_limits)
        if potential_path[-1] == 'S':
            return potential_path

    return 'F'

if __name__ == "__main__":
    path1 = find_path(GRID1, OFFLIMITS1)
    print("Grid 1 path:", path1)
    path2 = find_path(GRID2, OFFLIMITS2)
    print("Grid 2 path:", path2)
    path3 = find_path(GRID3, OFFLIMITS3)
    print("Grid 3 path:", path3)
