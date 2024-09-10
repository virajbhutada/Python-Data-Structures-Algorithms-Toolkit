def bellman_ford(vertices, edges, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in edges:
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            return "Graph contains negative weight cycle"

    return distance

# Test
vertices = ['A', 'B', 'C']
edges = [('A', 'B', 1), ('B', 'C', 3), ('A', 'C', 10)]
print(bellman_ford(vertices, edges, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 4}
