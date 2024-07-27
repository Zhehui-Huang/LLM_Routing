import math
from itertools import permutations

# Cities coordinates (index corresponds to city number)
cities = [
    (53, 68), # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Pre-calculate all distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to calculate tour cost and maximal distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_edge_cost = 0
    for i in range(1, len(tourney)):
        dist = distances[tour[i - 1]][tour[i]]
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
    # Don't forget to return to the depot
    return_to_depot_dist = distances[tour[-1]][tour[0]]
    total_cost += return_to_depot_dist
    if return_to_depot_dist > max_edge_cost:
        max_edge_cost = return_to_depot_dist
    return total_cost, max_edge_cost

# Generate all permutations of cities (excluding the depot city 0)
city_indices = list(range(1, len(cities)))

# Find the optimal tour minimizing the longest distance between consecutive cities
best_tour = None
best_max_edge_cost = float('inf')
best_total_cost = None

for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]
    total_cost, max_edge_cost = evaluate_tour(tour)
    if max_edge_cost < best_max_edge_cost:
        best_max_edge_cost = max_edge_cost
        best_tour = tour
        best_total_cost = total_cost

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_total_Mcost)
print("Maximum distance between consecutive cities:", best_max_edge_cost)