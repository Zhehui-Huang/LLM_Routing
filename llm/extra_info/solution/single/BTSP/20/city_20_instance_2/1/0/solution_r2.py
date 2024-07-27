from math import sqrt
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Gather city indices except the depot
city_indices = list(cities.keys())[1:]
best_tour = None
smallest_max_distance = float('inf')
perfect_total_cost = float('inf')

# Evaluate each permutation of the city indices
for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(tour[i-1], tour[i])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    if (max_distance < smallest_max_distance) or \
       (max_distance == smallest_max_distance and total_cost < perfect_total_dist):
        best_tour = tour
        smallest_max_distance = max_distance
        perfect_total_cost = total_cost

# Output the optimal tour results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {perfect_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {smallest_max_distance:.2f}")