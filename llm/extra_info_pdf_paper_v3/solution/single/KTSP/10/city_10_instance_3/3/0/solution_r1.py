import numpy as np
from itertools import permutations

# Define the city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Distance calculation using Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute all combinations of 6 cities to be visited excluding the depot
city_combinations = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))

# Placeholder variables for the shortest path
shortest_path = None
shortest_distance = float('inf')

# Explore all combinations and permutations to find the shortest tour
for combination in city_combinations:
    current_route = [0] + list(combination) + [0]
    
    # Consider all permutations of the chosen cities
    for perm in permutations(combination):
        permuted_route = [0] + list(perm) + [0]
        distance = sum(euclidean_distance(permuted_route[i], permuted_route[i+1]) for i in range(len(permuted_route) - 1))
        
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = permuted_route

# Printing the result
print(f"Tour: {shortest_path}")
print(f"Total travel cost: {shortest_distance:.2f}")