import math
from itertools import permutations

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(cities):
    """Calculate distances between each pair of cities."""
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_tsp_tour(cities):
    """Find the TSP tour that minimizes the longest distance between any two consecutive cities."""
    n = len(cities)
    distances = calculate_distances(cities)
    
    # Use permutations to find the optimal route (not viable for large n, but will demonstrate idea)
    min_max_edge = float('inf')
    best_tour = None
    for perm in permutations(range(1, n)):  # start from city 0
        current_tour = [0] + list(perm) + [0]
        max_edge_in_tour = max(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour)-1))
        if max_edge_in_tour < min_max_edge:
            min_max_edge = max_edge_in_tour
            best_tour = current_tour
            
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    
    return best_tour, total_cost, min_max of edge

# Solve the problem
tour, total_cost, max_dist = find_tsp_tour(cities)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)