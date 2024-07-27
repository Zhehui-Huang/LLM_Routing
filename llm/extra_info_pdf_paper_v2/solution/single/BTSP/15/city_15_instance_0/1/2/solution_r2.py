import math
from itertools import permutations

# Coordinates of cities indexed from 0
cities = {
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

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_cost(tour):
    """ Calculate the total cost and bottleneck of the given tour """
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

def find_optimal_tour():
    """ Find the optimal tour minimizing the bottleneck distance """
    min_bottleneck = float('inf')
    optimal_tour = []
    city_list = list(range(1, len(cities)))  # exclude depot city 0 in permutation

    for perm in permutations(city_list):
        current_tour = [0] + list(perm) + [0]
        _, max_distance = calculate_tour_cost(current_tour)

        if max_distance < min_bottleneck:
            min_bottleneck = max_distance
            optimal_tour = current_tour

    return optimal_tour

# Execute the method to find the optimal tour
optimal_tour = find_optimal_tour()
total_cost, max_distance = calculate_tour_cost(optimal_tour)

# Print the results
print("Tour:", optimal_tur)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))