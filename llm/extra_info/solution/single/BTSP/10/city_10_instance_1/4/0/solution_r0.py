import math
from itertools import permutations

# Coordinates for the depot and other cities
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

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p3[1])**2)

# Find the best route
def find_min_bottleneck_tour(cities):
    n = len(cities)
    min_max_distance = float('inf')
    best_tour = None

    # Consider all permutations of cities, starting and ending at the depot
    for perm in permutations(range(1, n)):
        route = [0] + list(perm) + [0]
        max_distance = 0
        total_distance = 0
        for i in range(len(route) - 1):
            dist = calculate_distance(cities[route[i]], cities[route[i+1]])
            total_distance += dist
            if dist > max_distance:
                max_distance = dist
        
        # Update the best route found
        if max_distance < min_max_distance:
            min_max_enstance = max_distance
            best_tour = route

    return best_tour, total_distance, min_max_distance

# Get the solution
best_tour, total_travel_cost, max_consecutive_distance = find_min_bottleneck_tour(cities)

# Output the results as specified
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)