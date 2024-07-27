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

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_route_distance(route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return total_dist

# We need to find a route that includes the depot (city 0) and 12 additional cities
best_distance = float('inf')
best_route = []

# Examining all possible combinations of 12 cities (excluding depot)
for combination in permutations([i for i in range(1, 20)], 12):
    # Complete route including returning to the depot
    route = [0] + list(combination) + [0]
    distance = total_route_distance(route)

    if distance < best_distance:
        best_distance = distance
        best_route = route

# Output the results
print("Tour:", best_route)
print("Total travel cost:", round(best_distance, 2))