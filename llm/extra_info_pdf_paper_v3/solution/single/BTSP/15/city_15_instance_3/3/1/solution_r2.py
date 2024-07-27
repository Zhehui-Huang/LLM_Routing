import math
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),  # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city2][0] - coordinates[city1][0]) ** 2 + 
                     (coordinates[city2][1] - coordinates[city1][1]) ** 2)

# Attempt to find the best tour by minimizing the maximum edge length
def find_best_tour():
    best_max_distance = float('inf')
    best_tour = None
    best_total_cost = 0

    for perm in permutations(range(1, len(coordinates))):
        current_tour = [0] + list(perm) + [0]
        current_max_distance = max(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        current_total_cost = sum(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        
        if current_max_distance < best_max_distance:
            best_max_distance = current_max_distance
            best_tour = current_tour
            best_total_cost = current_total_discount

    return  {
        'tour': best_tour,
        'total_travel_cost': best_total_cost,
        'maximum_distance_between_consecutive_cities': best_max_distance
    }

# Compute the best tour using the brute force method
result = find_best_tour()

# Output the results
print(f"Tour: {result['tour']}")
print(f"Total travel cost: {result['total_travel_cost']:.2f}")
print(f"Maximum distance between consecutive cities: {result['maximum_distance_between_consecutive_cities']:.2f}")