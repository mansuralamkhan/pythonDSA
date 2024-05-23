def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    previous_nodes = {vertex: None for vertex in graph}
    visited = set()

    while len(visited) < len(graph):
        min_distance_vertex = None
        for vertex in graph:
            if vertex not in visited:
                if min_distance_vertex is None or distances[vertex] < distances[min_distance_vertex]:
                    min_distance_vertex = vertex

        if min_distance_vertex is None:
            break

        visited.add(min_distance_vertex)

        for neighbour, weight in graph[min_distance_vertex].items():
            distance = distances[min_distance_vertex] + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                previous_nodes[neighbour] = min_distance_vertex

    return distances, previous_nodes

def get_shortest_path(previous_nodes, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous_nodes[target]
    path.reverse()
    return path

# Define the graph and source vertex
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 6},
    'D': {'B': 1, 'C': 4, 'E': 8, 'F': 2},
    'E': {'C': 6, 'D': 8, 'F': 7},
    'F': {'D': 2, 'E': 7}
}
source_vertex = 'A'
shortest_distances, previous_nodes = dijkstra(graph, source_vertex)
print("Shortest distances: ", shortest_distances)
print("Shortest path from A to F: ", get_shortest_path(previous_nodes, 'F'))
