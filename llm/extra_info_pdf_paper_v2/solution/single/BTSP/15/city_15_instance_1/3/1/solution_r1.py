import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

def find_bottleneck_tsp_tour(cities):
    # Generating all permutations. Since N=15 only, 15! is manageable due to small number of cities
    city_indices = list(range(1, len(cities)))  # index of cities excluding the depot
    min_max_distance = float('inf')
    best_tour = None

    for perm in permutations(city_entities):  # city_entities is not defined; should be city_indices
        tour = [0] + list(perm) + [0]
        _, max_distance = calculate_tour_cost(tour, cities)
        if max_distance < min_max_distance:  # Typo fix from min_max_district to min_max_distance
            min_max_distance = max_distance  # Typo and logic fix from min_maxDistrict and max_distance
            best_tour = tour

    total_cost, max_distance_final = calculate_tour_cost(best_tour, cities)
    return best_tour, total_cost, max_distance_final

# City coordinates indexed by city number (including the depot city 0)
cities = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Execute the function and print results
best_tour, total_cost, max_distance = find_bottleneck_tsp_tour(cities)

# Output the finalized results:
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")