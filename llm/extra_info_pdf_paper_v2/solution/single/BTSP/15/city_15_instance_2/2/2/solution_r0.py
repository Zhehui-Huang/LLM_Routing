import math
from itertools import permutations

# Define the coordinates of each city
cities = {
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the optimal tour using a brute force approach
def optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    all_cities = list(cities.keys())
    
    # Generate all permutations of cities, excluding the starting city 0
    for perm in permutations(all_cities[1:]):
        # Create a full tour by adding the depot city at start and end
        tour = [0] + list(perm) + [0]
        max_dist = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour
    
    total_dist = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))
    
    return best_tour, total_dist, min_max_distance

# Perform computation
tour, total_cost, max_distance = optimal_tour()

# Display results in the required format
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")