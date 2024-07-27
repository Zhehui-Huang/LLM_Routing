import math
import itertools
from itertools import permutations
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

# City coordinates
cities = [
    (9, 93),  # City 0 - Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Function to calculate the Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the distance matrix
n = len(cities)
dist_matrix = [[euclidean_dist(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the list of edges and sort them based on distance
edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(i+1, n)]
edges.sort(key=lambda x: x[2])

# Function to find Hamiltonian path
def has_hamiltonian_path(c):
    # Create graph limited by c
    adj_matrix = [[0]*n for _ in range(n)]
    for i, j, d in edges:
        if d <= c:
            adj_matrix[i][j] = adj_matrix[j][i] = 1

    # Check if all vertices form a single connected component
    graph = csr_matrix(adj_matrix)
    num_components, labels = connected_components(csgraph=graph, directed=False)
    if num_components != 1:
        return False
    
    # Attempt to find a Hamiltonian path
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        valid = True
        for k in range(len(path) - 1):
            if adj_matrix[path[k]][path[k+1]] == 0:
                valid = False
                break
        if valid:
            return True
    return False

# Approximate using binary search
low, high = 0, max(max(dist_matrix))
best_c, best_path = None, None
while low <= high:
    mid = (low + high) / 2
    if has_hamiltonian_path(mid):
        best_path = mid
        high = mid - 1
    else:
        low = mid + 1

# Verify the tour and calculate cost details
def verify_tour(c):
    # Use any heuristic e.g. nearest neighbour enhanced with the threshold `c` for producing a valid tour
    tour, used_edges = [0], set()
    last_city = 0
    for _ in range(1, n):
        next_city = min((j for j in range(n) if (j not in tour and dist_matrix[last_city][j] <= c)),
                        key=lambda j: dist_matrix[last_city][j], default=None)
        if next_city is None:
            return None  # Not feasible to make a path
        tour.append(next_city)
        last_city = next_city
    tour.append(0)  # complete the tour back to the depot
    
    # Calculate total cost and max distance
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_dist = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_dist

# Finalizing the results
if best_path is not None:
    final_tour, total_cost, max_distance = verify_tour(best_path)
    print("Tour:", final_tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No feasible tour found.")