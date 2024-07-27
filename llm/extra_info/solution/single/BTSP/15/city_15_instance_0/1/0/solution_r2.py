import math
from itertools import permutations

# City coordinates (indexed by city number).
cities_coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_optimal_tour():
    """ Find the optimal tour minimizing the max distance between consecutive cities. """
    city_indices = list(cities_coordinates.keys())[1:]  # Exclude the depot city (0) initially.
    best_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')

    for permutation in permutations(city_indices):
        # Complete tour by adding the depot city (0) at the beginning and the end.
        tour = [0] + list(permutation) + [0]

        # Calculate the total cost and maximum distance between consecutive cities.
        total_cost = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            distance = euclidean_distance(tour[i], tour[i + 1])
            total_cost += distance
            if distance > max_distance:
                max_distance = distance
        
        # Check if this tour has the minimal max distance so far
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_min_cost):
            best_tour = tour
            min_max_distance = max_distance
            total_min_cost = total_cost

    return best_tour, total_min_cost, min_max_distance

# Evaluate the optimal tour
tour, total_cost, max_distance = find_optimal_tour()
result_output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"
print(result_output)