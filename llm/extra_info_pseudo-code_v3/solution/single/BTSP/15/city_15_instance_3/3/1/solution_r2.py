import math
from itertools import permutations

# Coordinates of the cities
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 29),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Constructing the distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to find the minimum bottleneck tour path
def find_min_bottleneck_tour():
    min_bottleneck = float('inf')
    best_tour = None

    # Try all permutations of cities (excluding depot, which is city 0)
    for perm in permutations(range(1, n)):
        cycle = [0] + list(perm) + [0]
        max_edge_in_cycle = max(distance_matrix[cycle[i]][cycle[i + 1]] for i in range(len(cycle) - 1))
        if max_edge_in_cycle < min_bottleneck:
            min_bottleneck = max_edge_in_cycle
            best_tour = cycle
    
    # Calculate total travel cost
    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, min_bottleneck

# Obtain the best tour and related metrics
tour, total_travel_cost, max_distance = find_min_bottleneck_tour()

# Output the tour and cost data
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel # Output the tour and cost dataprint(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")