import math
from itertools import permutations

# City coordinates list
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generating and evaluating tours to find the optimal one
n = len(cities)
be_total_cost = math.inf
best_tour = []
best_max_dist = math.inf

for perm in permutations(range(1, n)):  # Permute over cities excluding the depot which is city 0
    # Include depot in the tour
    tour = [0] + list(perm) + [0]
    # Calculate the tour's total cost and maximum distance between consecutive cities
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    # Check for the best tour with the smallest maximum distance
    if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < be_total_cost):
        best_max_dist = max_dist
        be_total_cost = total_cost
        best_tour = tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {be_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_dist:.2f}")