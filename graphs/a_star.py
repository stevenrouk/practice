"""Unfinished / In Progress -- A Star path-finding algorithm."""

from collections import defaultdict
import math


def euclidean_distance(x, y):
    return math.sqrt(x**2 + y**2)

class AStar:

    def __init__(self, grid_size, blocked_list=[]):
        self.grid_size = grid_size
        self.blocked_list = blocked_list
        self.previous = {}
        self.remaining = [
            (math.inf, i, j) \
            for i in range(grid_size[0]) \
            for j in range(grid_size[1]) \
            if (i, j) not in self.blocked_list
        ]
        self.distances = {(i, j): math.inf for _, i, j in self.remaining}
        self.heuristic_func = euclidean_distance
        self.heuristics = None

    def _generate_path(self, node):
        path_list = [node]
        while self.previous[node] is not None:
            node = self.previous[node]
            path_list.append(node)
        
        return ''.join([str(i) for i in path_list[::-1]])

    def _get_neighbors(self, n):
        neighbors = []
        for i in (n[0]-1, n[0], n[0]+1):
            for j in (n[1]-1, n[1], n[1]+1):
                if i > 0 and j > 0 and n != (i, j):
                    neighbors.append((i, j))

        return neighbors

    def find_shortest_path(self, start, end):
        """Returns: path_length, path."""
        self.distances[start] = 0
        self.previous[start] = None
        seen = set()
        for i, r in enumerate(self.remaining):
            if r[1] == start:
                self.remaining[i] = (0, start)
                continue
        while len(self.remaining) > 0:
            path_dist, *node = min(self.remaining)
            node = tuple(node)
            self.remaining.remove((path_dist, *node))
            if path_dist is math.inf or node == end:
                break
            for n in self._get_neighbors(node):
                if n in seen:
                    continue
                if path_dist + 1 < self.distances[n]:
                    self.distances[n] = path_dist + 1
                    self.previous[n] = node
                    seen.add(n)
                    for i, r in enumerate(self.remaining):
                        if r[1] == n:
                            self.remaining[i] = (self.distances[n], n)
                            continue

        path = self._generate_path(end)
        return self.distances[end], path


if __name__ == "__main__":
    a = AStar(grid_size=(10, 10), blocked_list=[(3, 3), (3, 4), (3, 5)])
    print(a.find_shortest_path((0, 0), (8, 8)))
