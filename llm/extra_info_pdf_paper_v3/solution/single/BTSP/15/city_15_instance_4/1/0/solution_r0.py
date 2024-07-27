import math
from itertools import permutations

# City coordinates
cities = [
    (35, 40),  # City 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Brute-force approach for finding optimal solution (feasible for small number of cities)
min_cost = float('inf')
min_max_distance = float('inf')
best_tour = None

for perm in permutations(range(1, len(cities))):  # All possible tours (excluding the depot city 0, which is start/end)
    tour = [0] + list(perm) + [0]  # Start and end at the depot city 0
    total_cost, max_distance = calculate_tour_cost(tour)
    # Objective: minimize the maximum distance between any two consecutive cities
    if max_distance < min_max_flag:
        min_max_distance = max_distance
        min_cost = total_cost
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")