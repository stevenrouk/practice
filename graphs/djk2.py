"""Solution from Rosetta Code."""

from collections import namedtuple, deque

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])


class Graph:

    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbors = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbors[start].add((end, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbors[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

if __name__ == "__main__":
    graph = Graph([
        ('a', 'b', 7), ('a', 'c', 9), ('a', 'f', 14), ('b', 'c', 10),
        ('b', 'd', 15), ('c', 'd', 11), ('c', 'f', 2), ('d', 'e', 6),
        ('e', 'f', 9)
    ])
    print(graph.dijkstra('a', 'e'))
