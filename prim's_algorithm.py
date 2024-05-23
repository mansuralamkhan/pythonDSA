


def prim(graph, start_vertex):
    mst = []
    visited = set([start_vertex])

    edges = [
        (weight, start_vertex, to)
        for to, weight in graph[start_vertex].item()
    ]

    while edges:

        edges.sort()
        weight, frm , to = edges.pop(0)

        if to not in visited:
            visited.add(to)
            mst.append(frm, to, weight)

            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    edges.apped(weight, to, to_next)

    return mst

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 5, 'C': 3}
}

mst = prim(graph, 'A')
print("Edges in the MST:", mst)