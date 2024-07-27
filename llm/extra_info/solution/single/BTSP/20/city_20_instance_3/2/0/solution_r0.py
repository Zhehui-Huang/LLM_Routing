import math
from itertools import permutations

# Coordinates of each city including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities including the depot
n_cities = len(coordinates)

# Calculate Euclidean distances between all pairs of cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distances matrix
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n_cities)] for i in range(n_cities)]

# Function to determine the best tour minimizing the single longest travel distance between consecutive cities
def find_best_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_travel_cost_best = float('inf')

    # Check every possible permutation of the cities (excluding the starting depot, which is city 0)
    for tour in permutations(range(1, n_cities)):
        # Add the depot at the start and the end of the tour
        full_tour = [0] + list(tour) + [0]
        
        # Calculate the total cost and the max distance between consecutive cities
        total_cost = 0
        max_distance = 0
        for i in range(1, len(full_tour)):
            dist = distances[full_tour[i-1]][full_tour[i]]
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        # Check if found a new optimal tour
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_travel_balance_best):
            best_tour = full_tour
            min_max_distance = max_distance
            total_travel_cost_best = total_cost

    return best_tour, total_travel_cost_best, min_max_distance

# Solve the problem
best_tour, total_travel_cost, max_distance_between_consecutive_cities = find_best_tour()

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_between_consecutive_cities}")