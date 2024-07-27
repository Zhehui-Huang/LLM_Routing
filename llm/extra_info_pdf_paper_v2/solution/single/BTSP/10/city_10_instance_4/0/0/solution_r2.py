import math
from itertools import permutations

# Coordinates for the cities
locations = [
    (79, 15),
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n = len(locations)

# Finding the optimal tour that minimizes the maximum distance between consecutive cities
best_tour = None
min_max_distance = float('inf')
total_cost = 0

# Generate all possible tours starting and ending at the depot using permutations
for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]
    previous_city = 0
    max_dist = 0
    cumulative_cost = 0
    valid_tour = True

    # Validate tour for minimum maximum distance
    for city in tour[1:]:
        dist = euclidean_distance(previous_city, city)
        cumulative_cost += dist
        if dist > max_dist:
            max_dist = dist
        previous_city = city
    
    # Check if this tour has a new minimal maximum distance
    if max_dist < min_max_distance:
        best_tour = tour
        min_max_distance = max_dist
        total_cost = cumulative_cost

# Printing the results
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))