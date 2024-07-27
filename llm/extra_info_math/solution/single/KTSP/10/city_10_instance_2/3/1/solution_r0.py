import math
from itertools import combinations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Create a distance matrix
n = len(cities)
dist = {i: {} for i in cities}
for i in cities:
    for j in cities:
        dist[i][j] = euclidean_distance(cities[i], cities[j])

# Find the minimum tour using a simple greedy heuristics
def greedy_tsp(start_city, cities_set, dist):
    unvisited = set(cities_set)
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    
    while unvisited:
        unvisited.remove(current_city)
        if not unvisited:
            break
        next_city = min(unvisited, key=lambda city: dist[current_city][city])
        total_distance += dist[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
    
    total_distance += dist[current_city][start_city]  # Return to the start
    tour.append(start_city)
    return tour, total_distance

# Main optimization over combinations
min_cost = float('inf')
best_tour = []

# Generate all combinations of 5 cities plus the depot city to select 6 cities
for cities_subset in combinations(range(1, n), 5):
    subset_with_depot = [0] + list(cities_subset)
    tour, cost = greedy_tsp(0, subset_with_depot, dist)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")