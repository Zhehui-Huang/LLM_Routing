import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def has_hamiltonian_path(graph, start_node):
    """ A simple DFS based approach to find if there is a Hamiltonian path. """
    V = len(graph)
    visited = [False] * V

    def dfs(vertex, depth):
        visited[vertex] = True
        if depth == V - 1:
            return True
        result = False
        for i in range(V):
            if graph[vertex][i] and not visited[i]:
                if dfs(i, depth + 1):
                    return True
        visited[vertex] = False
        return result

    return dfs(start_node, 0)

def bottleneck_tsp(coordinates):
    V = len(coordinates)
    edges = []
    graph = [[0] * V for _ in range(V)]

    # Generating the matrix and edge list
    for i in range(V):
        for j in range(i + 1, V):
            distance = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((distance, i, j))
            graph[i][j] = graph[j][i] = distance
            
    # Sort edges by their length
    edges.sort()

    for cutoff, _, _ in edges:
        # Generate graph with maximum edge weight cutoff
        bottleneck_graph = [[1 if graph[i][j] <= cutoff else 0 for j in range(V)] for i in range(V)]
        
        # Check if the bounded graph has a Hamiltonian path starting from the depot
        if has_hamiltonian_path(bottleneck_graph, 0):
            # Generate the path from the bottleneck graph
            for perm in permutations(range(1, V)):
                path = [0] + list(perm) + [0]
                # Verify path against cutoff
                if all(bottleneck_graph[path[i]][path[i+1]] for i in range(len(path)-1)):
                    total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
                    max_distance = max(graph[path[i]][path[i+1]] for i in range(len(path)-1))
                    return {
                        'Tour': path,
                        'Total travel cost': total_cost,
                        'Maximum distance between consecutive cities': max_distance
                    }
    return None

# City coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
    (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

result = bottleneck_tsp(coordinates)
if result:
    print("Tour:", result['Tour'])
    print("Total travel cost:", result['Total travel length'])
    print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive cities'])
else:
    print("No Hamiltonian cycle found that fits the criteria.")