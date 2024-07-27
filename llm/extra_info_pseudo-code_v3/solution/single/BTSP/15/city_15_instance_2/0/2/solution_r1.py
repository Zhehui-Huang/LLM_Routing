import math
import itertools

# Define the coordinates of each city
coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Generate all city indices except the depot
cities = list(coordinates.keys())[1:]

# Find all possible permutations of city visits
all_permutations = list(itertools.permutations(cities))

# Variables to keep track the optimal tour
min_max_edge_length = float('inf')
optimal_tour = None
total_distance_optimal = 0

# Check each possible permutation
for perm in all_permutations:
    route = [0] + list(perm) + [0]
    max_edge_length = 0
    total_distance = 0

    # Calculate the travel cost and maximum edge length
    for i in range(len(route) - 1):
        current_distance = euclidean_distance(route[i], route[i+1])
        total_distance += current_distance
        if current_distance > max_edge_length:
            max_edge_length = current_distance  # Corrected line
    
    if max_edge_length < min_max_edge_length:
        min_max_edge_length = max_edge_length
        optimal_tour = route
        total_distance_optimal = total_distance

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_distance_optimal:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_edge_length:.2f}")