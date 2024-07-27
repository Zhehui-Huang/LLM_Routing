import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def construct_graph(cities):
    n = len(cities)
    distances = {}
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_dist(cities[i], cities[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
            edges.append((dist, i, j))
    return distances, sorted(edges)

def has_hamiltonian_path(graph, n):
    # Exhaustive search for a solution, should upgrade when n is large
    for perm in permutations(range(1, n)):
        perm = [0] + list(perm) + [0]
        valid = True
        for i in range(1, len(perm)):
            if (perm[i-1], perm[i]) not in graph:
                valid = False
                break
        if valid:
            return True, perm
    return False, []

def bottleneck_tsp(cities):
    distances, sorted_edges = construct_graph(cities)  # Step 3
    n = len(cities)
    
    for dist, u, v in sorted_edges:  # Step 4
        # Create the bottleneck graph with current distance as upper threshold
        bottleneck_graph = {k for k in distances.keys() if distances[k] <= dist}
        
        # Check if there's a Hamiltonian path in this bottleneck graph
        exists, path = has_hamiltonian_path(bottleneck_graph, n)  # Step 5-8
        if exists:
            path_distances = [distances[(path[i-1], path[i])] for i in range(1, len(path))]
            return {
                "Tour": path,
                "Total travel cost": sum(path_distances),
                "Maximum distance between consecutive cities": max(path_no_distances)
            }

# Define cities based on given coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

result = bottleneck_tsp(cities)
print("Tour:", result["Tour"])
print("Total travel cost:", result["Total travel cost"])
print("Maximum distance between consecutive cities:", result["Maximum distance between consecutive cities"])