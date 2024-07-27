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

# Calculate Euclidean distance between two given cities by their indices
def distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0]) ** 2 + (cities[city2][1] - cities[city1][1]) ** 2)

# Permutes all city indices except the depot city
city_indices = list(range(1, len(cities)))
all_permutations = permutations(city_indices)

# Initialize tracking for the optimal tour
min_max_distance_tour = None
min_max_distance = float('inf')
min_total_cost = float('inf')

# Evaluate each tour permutation
for perm in all_permutations:
    # Generate a tour starting and ending at the depot city 0
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_distance = 0

    # Calculate tour cost and max distance between consecutive cities
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check if this tour has a lower max distance between consecutive cities
    # or same max distance but lower total cost
    if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < min_total_cost):
        min_max_distance = max_distance
        min_max_distance_tour = tour
        min_total_cost = total_cost

# Output the best found optimal tour results
print("Tour:", min_max_distance_tour)
print("Total travel cost:", min_total_cost)
print("Maximum distance between consecutive cities:", min_max_distance)