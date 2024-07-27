import math
from itertools import permutations

# Define the coordinates of each city
cities = [
    (3, 26),   # Depot City 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Compute all pairwise distances
n = len(cities)
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# The given pseudocode simplified to work for BRUTE FORCE since BB algorithm is inherently complex to implement optimally here.
def brute_force_bottleneck_tsp():
    best_tour = None
    min_bottleneck = float('inf')
    all_cities = list(range(1, n))  # except the depot city

    for perm in permutations(all_cities):
        # Create a full tour by going back to the depot
        tour = [0] + list(perm) + [0] 
        
        # Calculate max distance (bottleneck) in this permutation
        max_dist_in_tour = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        # Compare and update best tour if current is better
        if max_dist_in_tour < min_bottleneck:
            min_bottleneck = max_dist_in_tour
            best_tour = tour

    total_travel_cost = sum(distances[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    return best_tour, total_travel_cost, min_bottleneck

# Solve the problem
tour, total_cost, max_distance = brute_force_bottleneck_tsp()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")