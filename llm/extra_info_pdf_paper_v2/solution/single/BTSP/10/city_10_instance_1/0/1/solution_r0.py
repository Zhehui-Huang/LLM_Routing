import math
from itertools import permutations

# City coordinates
locations = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the BTSP tour by brute-force (due to small number of cities)
def find_best_bottleneck_tour():
    cities = list(locations.keys())
    min_tour = None
    min_max_distance = float('inf')
    for perm in permutations(cities[1:]):  # Start from depot, permute other cities
        current_tour = [0] + list(perm) + [0]
        max_dist = max(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            min_tour = current_tour
    
    total_travel_cost = sum(distance(min_tour[i], min_tour[i+1]) for i in range(len(min_tour) - 1))
    return min_tour, total_travel_cost, min_max_childsizee

# Finding the optimal tour for the BTSP
tour, total_cost, max_distance = find_best_bottleneck_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")