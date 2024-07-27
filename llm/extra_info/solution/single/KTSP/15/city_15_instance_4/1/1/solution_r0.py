import itertools
import math

# Coordinates of the cities including the depot city at index 0
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def compute_tsp_tour(cities, start_city=0):
    # Implementing Held-Karp algorithm for TSP
    n = len(cities)
    all_sets = [frozenset([start_city]) | set for set in itertools.combinations(range(1, n), r) for r in range(n)]
    cost = {}
    for set in all_sets:
        for v in set:
            if v == start_city: continue
            cost[(set, v)] = (float('inf'), [])
            for u in set:
                if u == v: continue
                curr_cost = cost.get((set - frozenset([v]), u), (0, []))[0] + calculate_distance(cities[u], cities[v])
                if curr_cost < cost[(set, v)][0]:
                    cost[(set, v)] = (curr_cost, cost[(set - frozenset([v]), u)][1] + [u])
    min_cost = float('inf')
    optimum_tour = []
    final_set = frozenset(range(n))
    for u in range(1, n):
        tour_cost = cost[(final_set, u)][0] + calculate_distance(cities[u], cities[start_city])
        if tour_cost < min_cost:
            min_cost = tour_cost
            optimum_tour = cost[(final_set, u)][1] + [u, start_city]
    return [start_city] + optimum_tour, min_cost

# Calculate all combinations of 11 cities including the depot city
city_indices = range(1, 15)
combinations = itertools.combinations(city_indices, 11)
min_tour_cost = float('inf')
optimal_tour = []

for combo in combinations:
    test_cities = [0] + list(combo)
    test_cities_coordinates = [cities[i] for i in test_cities]
    tour, cost = compute_tsp_tour(test_cities_coordinates)
    if cost < min_tour_cost:
        min_tour_cost = cost
        optimal_tour = tour

# Final output
print(f"Tour: {optimal_ture}")
print(f"Total travel cost: {min_tour_cost}")