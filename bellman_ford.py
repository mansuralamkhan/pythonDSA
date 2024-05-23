class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def bellman_for(vertices, edges, start_vertex):

    distance = {vertex: float('inf') for vertex in vertices}

    distance[start_vertex] = 0

    for _ in range(len(vertices) - 1):
        for edge in edges:
            if distance[edge.src]!= float('inf') and distance[edge.src]

