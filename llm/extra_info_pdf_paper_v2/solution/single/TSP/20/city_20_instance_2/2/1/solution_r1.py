import math
import random

# Define the coordinates of the cities, where the index represents the city number
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_distance(tour):
    total = 0
    for i in range(1, len(tour)):
        total += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total

def swap_2opt(route, i, k):
    new_route = route[0:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k + 1:])
    return new_route

def two_opt(route):
    best = route
    best_dist = total_distance(best)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for k in range(i + 1, len(route) - 1):
                new_route = swap_2opt(best, i, k)
                new_dist = total_distance(new_route)
                if new_dist < best_dist:
                    best = new_route
                    best_dist = new_dist
                    improved = True
        route = best
    return best, best_dist

# Initial tour: start at the depot, visit each city once, return to depot
initial_tour = list(cities.keys())
# Randomize starting tour (excluding the depot)
randomized_tour = [0] + random.sample(initial_tour[1:], len(initial_tour)-1) + [0]

# Optimize using 2-opt
optimized_tour, optimized_dist = two_opt(randomized_tour)

# Output the tour and total travel cost
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_dist)