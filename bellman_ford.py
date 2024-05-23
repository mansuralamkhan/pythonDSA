def bellman_ford(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}


    distances[source] = 0


    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbour, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbour]:
                    distances[neighbour] = distances[vertex] + weight
                    predecessors[neighbour] = vertex


    for vertex in graph:
        for neighbour, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbour]:
                raise ValueError("Graph contains a negative weight cycle")
            
    return distances, predecessors

def get_shortest_path(predecessors, target):
    path = []
    while target is not None:
        path.append(target)
        target = predecessors[target]
    path.reverse()
    return path


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 1},
    'C': {'D': 4, 'E': 6},
    'D': {'F': 2},
    'E': {'F': 7},
    'F': {}
}

source_vertex = 'A'
try:
    shortest_distances, predecessors = bellman_ford(graph, source_vertex)
    print("Shortest distances: ", shortest_distances)


    for vertex in graph:
        if vertex == source_vertex:
            continue
        path = get_shortest_path(predecessors, vertex)
        print(f"Shortest path from {source_vertex} to {vertex}: ", path)
except ValueError as e:
    print(e)
