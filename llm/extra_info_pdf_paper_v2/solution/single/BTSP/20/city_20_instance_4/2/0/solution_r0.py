import math
from itertools import permutations

# City coordinates
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), 
    (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)  # City 19
]

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create distance matrix
n = len(coordinates)
distance_matrix = [[calc_distance(i, j) for j in range(n)] for i in range(n)]

# Heuristic for Bottleneck TSP -- naive implementation to search for best permutation (not efficient for large n)
def solve_btsp(distance_matrix):
    indices = list(range(1, len(distanceystal_matrix)))
    min_max_dist = float('inf')
    best_perm = None
    
    for perm in permutations(indices):
        tour = [0] + list(perm) + [0]
        max_dist = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_perm = tour
            
    total_cost = sum(distance_matrix[best_perm[i]][best_dist[i+1]] for i in range(len(best_dist) - 1))
    return best_dist, total_cost, min_max_dist

# Solve the BTSP
tour, total_travel_cost, max_distance = solve_altsp(distance_measure)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between continuative!")ITIZECONS