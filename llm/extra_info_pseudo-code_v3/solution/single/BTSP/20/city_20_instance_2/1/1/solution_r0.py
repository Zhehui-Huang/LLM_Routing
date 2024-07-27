import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def can_form_hamiltonian_path(graph, V):
    # Trying all permutations to check for Hamiltonian path
    for perm in permutations(range(1, V)):
        valid = True
        for i in range(1, len(perm)):
            if not graph[perm[i-1]][perm[i]]:
                valid = False
                break
        if valid:
            return [0] + list(perm) + [0]
    return None


def bottleneck_tsp(coordinates):
    V = len(coordinates)
    edges = []
    graph = [[0]*V for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((dist, i, j))
            graph[i][j] = dist
            graph[j][i] = dist
    
    edges.sort()  # Sort edges by distance

    for cutoff, u, v in edges:
        # Create graph with edges not exceeding the current cutoff distance
        subgraph = [[0]*V for _ in range(V)]
        for dist, i, j in edges:
            if dist > cutoff:
                break
            subgraph[i][j] = 1
            subgraph[j][i] = 1
        
        hamiltonian_path = can_form_hamiltonian_path(subgraph, V)
        if hamiltonian_path:
            # Calculate total cost and max distance
            total_cost = sum(graph[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(V))
            max_distance = max(graph[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(V))
            return {
                'Tour': hamiltonian_path,
                'Total travel cost': total_cost,
                'Maximum distance between consecutive cities': max_distance
            }

# City coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
    (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

result = bottleneck_tsp(coordinates)
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel cost'])
print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive cities'])