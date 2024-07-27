import math
from itertools import permutations

# Coordinates of cities (city index: (x, y))
coordinates = {
    0: (16, 90), 
    1: (43, 99), 
    2: (80, 21), 
    3: (86, 92), 
    4: (54, 93), 
    5: (34, 73), 
    6: (6, 61), 
    7: (86, 69), 
    8: (30, 50), 
    9: (35, 73), 
    10: (42, 64), 
    11: (64, 30), 
    12: (70, 95), 
    13: (29, 64), 
    14: (32, 79)
}

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Generate all pairwise distances
num_cities = len(coordinates)
edges = [(i, j) for i in range(num_cities) for j in range(i+1, num_cities)]
edges_sorted_by_weight = sorted(edges, key=lambda edge: euclidean_distance(edge[0], edge[1]))

def find_minimal_bottleneck_hamiltonian_cycle():
    # Evaluate all permutations of city indices (excluding the depot, which is both start and end)
    best_cycle = None
    best_max_edge_weight = float('inf')
    
    for perm in permutations(range(1, num_cities)):
        full_cycle = [0] + list(perm) + [0]
        max_edge_weight = max(euclidean_distance(full_cycle[i], full_cycle[i+1]) for i in range(len(full_cycle)-1))
        
        if best_cycle is None or max_edge_weight < best_max_edge_weight:
            best_cycle = full_cycle
            best_max_edge_weight = max_edge_weight
    
    return best_cycle, best_max_max_edge_weight
  
# Execution
best_cycle, best_max_edge_weight = find_minimal_bottleneck_hamiltonian_cycle()
total_travel_cost = sum(euclidean_distance(best_cycle[i], best_cycle[i+1]) for i in range(len(best_cycle) - 1))
max_distance = best_max_edge_weight

print("Tour:", best_cycle)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)