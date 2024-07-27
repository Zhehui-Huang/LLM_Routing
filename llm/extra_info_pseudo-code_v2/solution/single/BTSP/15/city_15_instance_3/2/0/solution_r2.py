import math
from itertools import permutations

# Define the coordinates of cities (indexed from 0 onwards)
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92),
    4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69),
    8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

num_cities = 15

# Helper function to compute Euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Compute all pairwise distances
distances = {(i, j): euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j}

# Generate all possible permutations of city visits starting and ending at the depot city (Node 0)
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    
    # Exclude city 0 in permutations; it is the depot start and end
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour

    return optimal_tour, min_max_distance

# Solve for the optimal tour
optimal_tour, min_max_distance = find_optimal_tour()

# Calculate total travel cost
total_travel_cost = sum(distances[optimal_tour[i], optimal_tour[i+1]] for i in range(len(optimal_tour) - 1))

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")