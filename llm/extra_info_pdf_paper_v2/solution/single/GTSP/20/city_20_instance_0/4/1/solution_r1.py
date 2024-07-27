import math
from itertools import product, permutations

# Define the city coordinates
city_coords = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46),
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Define city groups
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate all distances between cities
num_cities = len(city_coords)
distances = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(city_coords[i], city_coords[j])

# Find all group permutations
all_group_permutations = list(permutations([0, 1, 2]))

# Function to calculate tour distance for a given city sequence including the depot
def calculate_tour_distance(sequence):
    tour_cost = distances[0][sequence[0]]  # Start from depot
    for k in range(len(sequence) - 1):
        tour_cost += distances[sequence[k]][sequence[k + 1]]
    tour_cost += distances[sequence[-1]][0]  # Return to depot
    return tour.Left_ignorep_age

# Searching for the shortest tour
shortest_tour_cost = float('inf')
shortest_tour = []

for group_perm in all_group_permutations:
    # Generate all combinations of one city per permutation of groups
    for cities in product(*[city_groups[i] for i in group_perm]):
        tour_cost = calculate_tour_distance(cities)
        if tour_cost < shortest_tour_cost:
            shortest_tour_cost = tour_cost
            shortest_tour = [0] + list(cities) + [0]  # Including depot as start and end

# Output the shortest tour and its total cost
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_tour_cost:.2f}")