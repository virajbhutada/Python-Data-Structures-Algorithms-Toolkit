from collections import defaultdict, deque

def topological_sort(vertices, edges):
    adj_list = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)
        for neighbor in adj_list[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order if len(topo_order) == len(vertices) else "Cycle detected"

# Test
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
print(topological_sort(vertices, edges))  # Output: ['A', 'B', 'C', 'D']
