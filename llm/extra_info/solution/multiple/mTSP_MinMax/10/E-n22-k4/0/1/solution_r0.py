import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import permutations

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Number of robots
num_robots = 4

# Solve the TSP problem for a given array of city indices
def solve_tsp(tour):
    min_dist = float('inf')
    best_order = None
    all_permutations = permutations(tour[1:])  # All permutations excluding the depot
    
    for perm in all_permutations:
        perm = (tour[0],) + perm + (tour[0],)
        dist = sum(euclidean_distance(cities[perm[i]], cities[perm[i+1]]) for i in range(len(perm) - 1))
        if dist < min_dist:
            min_dist = dist
            best_order = perm
            
    return list(best_order), min_dist

# Split cities more or less evenly across all robots
city_indices = list(cities.keys())[1:]  # Exclude the depot city
np.random.shuffle(city_indices)
city_splits = np.array_split(city_indices, num_robots)

# Finding tours and their costs
max_cost = 0
routes = {}

for i, split in enumerate(city_splits):
    tour, cost = solve_tsp([0] + list(split))
    routes[i] = {'tour': tour, 'cost': cost}
    if cost > max_cost:
        max_cost = cost

# Output tours and their costs
for i in range(num_robots):
    print(f"Robot {i} Tour: {routes[i]['tour']}")
    print(f"Robot {i} Total Travel Cost: {routes[i]['cost']}")

print(f"Maximum Travel Cost: {max_cost}")