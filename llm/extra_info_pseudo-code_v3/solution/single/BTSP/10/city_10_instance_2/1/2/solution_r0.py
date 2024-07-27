import math
import itertools
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components


def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def assess_hamiltonian_path(bottleneck_graph, n):
    # Computing the MST over the bottleneck graph
    mst = minimum_spanning_tree(bottleneck_graph).toarray().astype(float)
    # Checking if all vertices have degree <= 2 and finding connected components
    if connected_components(mst)[0] == 1:
        degrees = (mst > 0).sum(axis=0) + (mst > 0).sum(axis=1)
        if all(degree <= 2 for degree in degrees):
            return True
    return False


# Input coordinates of the cities (depot index 0)
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Compute distances between every pair of cities
n = len(cities)
distances = [[compute_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Get sorted list of unique distances
edge_distances = sorted(set(itertools.chain.from_iterable(distances)))

# Algorithm to find the Hamiltonian cycle with minimum bottleneck value
best_path = None
best_max_distance = float('inf')

for d in edge_distances:
    bottleneck_matrix = [[0 if distances[i][j] <= d else float('inf') for j in range(n)] for i in range(n)]
    
    # Check for Hamiltonian path in this graph
    if assess_hamiltonian_path(bottleneck_matrix, n):
        # If such a Hamiltonian cycle exists, use a method to find it; here we use a simple DFS
        graph = [(i, j) for i in range(n) for j in range(n) if i != j and distances[i][j] <= d]
        
        # Find Hamiltonian cycle using a simple approximation heuristic
        # Using brute-force or MST+DFS could be better for small cases but may not scale
        # This is just example using brute-force due to problem scale
        for perm in itertools.permutations(range(1, n)):
            path = [0] + list(perm) + [0]
            max_edge = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
            if max_edge == d:  # Checking if this permutation satisfies conditions
                total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
                if max_edge < best_max_distance:
                    best_max_distance = max_edge
                    best_path = path
                    best_total_cost = total_cost
                    break
        if best_path:
            break

# Output the results
if best_path:
    print("Tour:", best_path)
    print("Total travel cost:", round(best_totalassistan_cost, 2))
    print("Maximum distance between consecutive cities:", round(best_max_distance, 2))
else:
    print("No valid Hamiltonian cycle found.")