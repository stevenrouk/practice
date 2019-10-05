from collections import defaultdict
import math

# example graph from here: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
graph_triplets = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 7, 11),
    (1, 2, 8),
    (7, 6, 1),
    (7, 8, 7),
    (2, 8, 2),
    (8, 6, 6),
    (2, 3, 7),
    (6, 5, 2),
    (5, 3, 14),
    (5, 4, 10),
    (3, 4, 9)
]


class Dijkstra:

    def __init__(self, triplets, directed=False):
        self.directed = directed
        graph, distances = self._create_graph(triplets)
        self.graph = graph
        self.distances = distances
        self.previous = {}
        self.remaining = list(set(x[0] for x in triplets) | set(x[1] for x in triplets))
        self.remaining = [(self.distances[n], n) for n in self.remaining]

    def _create_graph(self, triplets):
        graph = defaultdict(list)
        distances = {}
        for t in triplets:
            graph[t[0]].append((t[1], t[2]))
            distances[t[0]] = math.inf
            distances[t[1]] = math.inf
        if not self.directed:
            graph[t[1]].append((t[0], t[2]))

        return graph, distances

    def _generate_path(self, node):
        path_list = [node]
        while self.previous[node] is not None:
            node = self.previous[node]
            path_list.append(node)
        
        return ''.join([str(i) for i in path_list[::-1]])

    def find_shortest_path(self, start, end):
        """Returns: path_length, path."""
        self.distances[start] = 0
        self.previous[start] = None
        seen = set()
        for i, r in enumerate(self.remaining):
            if r[1] == start:
                self.remaining[i] = (0, start)
                continue
        # path_dist, node = [x for x in self.remaining if x[1]==start][0]
        # self.remaining.remove((path_dist, node))
        while len(self.remaining) > 0:
            path_dist, node = min(self.remaining)
            self.remaining.remove((path_dist, node))
            if path_dist is math.inf or node == end:
                break
            for n, edge_weight in self.graph[node]:
                if n in seen:
                    pass
                elif path_dist + edge_weight < self.distances[n]:
                    self.distances[n] = path_dist + edge_weight
                    self.previous[n] = node
                    seen.add(n)
                    for i, r in enumerate(self.remaining):
                        if r[1] == n:
                            self.remaining[i] = (self.distances[n], n)
                            continue
        
        path = self._generate_path(end)
        return self.distances[end], path


if __name__ == "__main__":
    d = Dijkstra(graph_triplets)
    print(d.find_shortest_path(0, 4))
