import math

# Coordinates for each city including depot
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Helper function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute-force algorithm to find minimum bottleneck tour
def min_bottleneck_tour(cities):
    # Generate all permutations of cities excluding the depot
    from itertools import permutations
    optimal_tour = None
    minimal_bottleneck = float('inf')
    minimal_total_cost = float('inf')

    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        max_distance = max(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if max_distance < minimal_bottleneck:
            current_total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            if max_distance < minimal_bottleneck or (max_distance == minimal_bottleneck and current_total_cost < minimal_total_cost):
                minimal_bottleneck = max_distance
                minimal_total_cost = current_total_cost
                optimal_tour = tour
    
    return optimal_tour, minimal_bottleneck, minimal_total_cost

# Let's find the best path using the function defined
best_tour, max_distance, total_cost = min_bottleneck_tour(cities)

# Display the results
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))