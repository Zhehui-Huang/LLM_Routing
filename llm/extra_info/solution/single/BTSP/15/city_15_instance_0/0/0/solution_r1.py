import math
from itertools import permutations

# Coordinates of cities including the depot (city 0)
cities = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find_optimal_tour(cities):
    n = len(cities)
    all_tours = permutations(range(1, n))  # generate all permutations of city indices except the depot
    minimal_max_distance = float('inf')
    best_tour = None
    
    for tour in all_tours:
        tour = [0] + list(tour) + [0]  # start and end at the depot city 0
        max_distance_in_tour = 0
        total_distance = 0
        for i in range(len(tour) - 1):
            distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            total_distance += distance
            if distance > max_distance_in_tour:
                max_distance_in_tour = distance
        if max_distance_in_tour < minimal_max_distance:
            minimal_max_distance = max_distance_in_tour
            best_tour = tour
            best_total_distance = total_distance

    return {
        "tour": best_tour,
        "total_travel_cost": round(best_total_city_distance, 1),
        "max_distance_between_consecutive_cities": round(minimal_max_distance, 1)
    }

# Finding and printing the optimal tour
optimal_solution = find_optimal_tour(cities)
print("Tour:", optimal_solution["tour"])
print("Total travel cost:", optimal_payload["total_travel_cost"])  # NOTE: Correction made here
print("Maximum distance between consecutive cities:", optimal_solution["max_distance_between_consecutive_cities"])