import math
from itertools import permutations

# Provided city coordinates
cities = [
    (9, 93),  # Depot City 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0])**2 + (cities[city2][1] - cities[city1][1])**2)

# Generate all permutations of the cities except the depot city
city_indices = list(range(1, len(cities)))
all_permutations = permutations(city_indices)

# Variables to find the optimal tour
min_max_distance_tour = None
min_max_distance = float('inf')
min_total_cost = float('inf')

# Evaluate each permutation
for perm in all_permutations:
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Update the optimal tour if a better one is found
    if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < min_total_cost):
        min_max_distance = max_distance
        min_max_distance_tour = tour
        min_total_cost = total_cost

# Output results
print("Tour:", min_max_distance_tour)
print("Total travel cost:", min_total_cost)
print("Maximum distance between consecutive cities:", min_max_distance)