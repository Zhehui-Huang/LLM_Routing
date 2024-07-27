import math
from itertools import permutations

# Given data: cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# List depots for the robots
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Split cities into clusters for each depot
clusters = {depot: [depot] for depot in depots}

# Heuristic: Assign each non-depot city to the nearest depot
for city in range(8, 23):  # non-depot cities
    nearest_depot = min(depots, key=lambda d: euclidean_distance(city, d))
    clusters[nearest_depot].append(city)

# Tour calculation for each robot
tours = {}
total_costs = {}

for depot, cluster in clusters.items():
    # Find a reasonable tour using permutations
    # We consider all permutations of the cities in the cluster (excluding the first element, which is the depot)
    best_permutation = None
    best_cost = float('inf')
    
    for perm in permutations(cluster[1:]):
        tour = [depot] + list(perm) + [depot]
        cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if cost < best_cost:
            best_cost = cost
            best_permutation = tour
    
    tours[depot] = best_permutation
    total_costs[depot] = best_cost

# Output results
overall_total_cost = sum(total_costs.values())
for depot in depots:
    print(f"Robot {depot} Tour: {tours[depot]}")
    print(f"Robot {depot} Total Travel Cost: {total_costs[depot]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")