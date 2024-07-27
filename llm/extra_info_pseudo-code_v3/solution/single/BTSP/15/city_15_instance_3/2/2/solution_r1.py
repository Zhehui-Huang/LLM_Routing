import numpy as np
from itertools import permutations

# Define the city positions
cities = [
    (16, 90),  # City 0 - Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

def euclidean_distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5

# Create a matrix of distances
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Helper function to find all Hamiltonian paths that start and end at the depot city
def find_valid_paths(max_distance):
    path_list = []
    for order in permutations(range(1, n)):  # Exclude the depot initially for permutations
        valid = True
        max_edge_cost = 0
        
        # Include depot at the start and end
        order = (0,) + order + (0,)
        
        # Check for max distance constraint
        for i in range(len(order)-1):
            dist = distances[order[i]][order[i+1]]
            if dist > max_distance:
                valid = False
                break
            max_edge_cost = max(max_edge_cost, dist)
        
        if valid:
            path_list.append((order, max_edge_cost))
    
    return path_list

# Minimize the maximum distance between consecutive cities
min_max_distance = float('inf')
best_path = None

for edge in sorted(set(distances[i][j] for i in range(n) for j in range(n) if i != j)):
    possible_paths = find_valid_paths(edge)
    if possible_paths:
        for path, max_edge_cost in possible_sync_paths:
            if max_edge_cost < min_max_distance:
                min_max_distance = max_edge_cost
                best_path = path
        break  # Break as soon as the first set of valid paths is found

# Calculate total travel cost for the best path
if best_path:
    total_cost = sum(distances[best_path[i]][best_path[i + 1]] for i in range(len(best_path) - 1))
    print("Tour:", list(best_path))
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", min_max_distance)
else:
    print("No valid tour found")