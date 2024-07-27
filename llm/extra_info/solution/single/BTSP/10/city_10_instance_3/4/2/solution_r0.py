from itertools import permutations
from math import sqrt

# Data for cities
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

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all pairs' distances
distances = {}
for i in range(10):
    for j in range(i+1, 10):
        dist = distance(i, j)
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Brute force search for optimal tour minimizing the maximum distance between consecutive cities
best_tour = None
best_max_dist = float('inf')
best_total_cost = float('inf')

for tour in permutations(range(1, 10)):
    tour = (0,) + tour + (0,)
    total_cost = 0
    max_dist = 0
    valid = True

    for i in range(len(tour) - 1):
        d = distances[(tour[i], tour[i+1])]
        total_cost += d
        if d > max_dist:
            max_dist = d

    if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < best_total_cost):
        best_tour = tour
        best_max_dist = max_dist
        best_totalct_cost = total_cost

# Format the output
print("Tour:", list(best_tour))
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_dist)