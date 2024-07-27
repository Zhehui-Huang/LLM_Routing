import math
from itertools import permutations

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Simplified manual clustering of cities based on their proximity, just dividing into two groups
cluster1 = [1, 2, 5, 6, 7, 9, 14, 17, 20]  # Closer to depot city
cluster2 = [3, 4, 8, 10, 11, 12, 13, 15, 16, 18, 19]  # Further from depot city

# Local search to find the best tour for given cluster of cities starting at the depot
def find_tour(cities, cluster):
    min_cost = float('inf')
    best_permutation = []
    for perm in permutations(cluster):
        cost = euclidean_distance(cities[0], cities[perm[0]])
        for i in range(len(perm) - 1):
            cost += euclidean_distance(cities[perm[i]], cities[perm[i + 1]])
        cost += euclidean_distance(cities[perm[-1]], cities[0])  # Return to depot
        if cost < min_cost:
            min_cost = cost
            best_permutation = perm
    return [0] + list(best_permutation) + [0], min_cost

# Finding optimal tours for each cluster
tour1, cost1 = find_tour(cities, cluster1)
tour2, cost2 = find_tour(cities, cluster2)

# Compute the maximum cost encountered by any robot
max_cost = max(cost1, cost2)

# Result output
print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost1}")
print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost2}")
print(f"Maximum Travel Cost: {max_cost}")