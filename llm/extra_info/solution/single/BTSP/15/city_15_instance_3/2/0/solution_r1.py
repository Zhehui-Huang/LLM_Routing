from itertools import permutations
import math

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 98),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (9, 61),
    7: (86, 69),
    8: (29, 50),
    9: (32, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79),
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Compute all permutations of cities (excluding the depot city)
city_indices = list(cities.keys())[1:]  # excluding depot
all_tours = permutations(city_x_indices)

min_max_distance = float('inf')
best_tour = None
best_total_cost = 0

# Explore each possible tour permutation
for tour in all_tours:
    complete_tour = [0] + list(tour) + [0]
    total_cost = 0
    max_local_distance = 0

    for i in range(len(complete_tour) - 1):
        cost = distance(complete_tour[i], complete_tour[i + 1])
        total_cost += cost
        if cost > max_local_distance:
            max_local_distance = cost

    if max_local_distance < min_max_distance:
        min_max_distance = max_local_distance
        best_total_cost = total_cost
        best_tour = complete_tour

if best_tour:
    print("Tour:", best_tour)
    print("Total travel cost:", round(best_total_cost, 2))
    print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
else:
    print("No feasible tour found.")