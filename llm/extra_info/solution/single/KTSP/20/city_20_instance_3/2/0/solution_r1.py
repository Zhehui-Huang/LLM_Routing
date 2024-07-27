import numpy as np
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

N = len(cities)
city_indices = list(cities.keys())

# Calculate euclidean distance between two cities
def euclidean_distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Compute all combinations of visiting 12 cities, starting and ending at depot (city 0)
all_possible_routes = permutations(city_indices[1:], 12)  # 19 choose 12 cities permutations
min_distance = float('inf')
best_route = None

# Evaluate each route
for route in all_possible_routes:
    # Include the depot as the start and end point of the route
    route_with_depot = [0] + list(route) + [0]
    
    # Calculate the total distance of this route
    distance = sum(euclidean_distance(route_with_depot[i], route_with_depot[i+1]) for i in range(len(route_with_depot) - 1))
    
    if distance < min_distance:
        min_distance = distance
        best_route = route_with_depot

# Output the results
print("Tour:", best_route)
print("Total travel cost:", round(min_distance, 2))