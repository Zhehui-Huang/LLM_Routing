import math
from itertools import permutations

# Function to calculate the Euclidean distance between two cities
def euclidean_dist(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Function to generate all possible tours (paths that visit every city exactly once and return to the depot)
def all_tours(cities):
    start = cities[0]
    for perm in permutations(cities[1:]):
        yield [start] + list(perm) + [start]

# Function to find the tour that minimizes the maximum distance between any two consecutive cities
def minimize_max_distance_tour(cities):
    best_max_distance = float('inf')
    best_tour = None
    best_cost = None

    for tour in all_tours(cities):
        maximum_distance = max(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost = sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if maximum_distance < best_max_distance:
            best_max_distance = maximum_distance
            best_tour = tour
            best_cost = total_cost

    return best_tour, best_cost, best_max_cdistance

# Input cities based on the provided coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Find optimal tour
tour, total_cost, max_distance = minimize_max_distance_tour(cities)

# Output tour, total travel cost, and maximum distance between consecutive cities
print("Tour:", [cities.index(city) for city in tour])
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)