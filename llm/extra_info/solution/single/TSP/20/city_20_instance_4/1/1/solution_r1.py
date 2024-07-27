import math
from itertools import permutations

# Given city coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Euclidean distance calculation
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate total tour cost
def total_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    return total_distance

# Find the tour using a brute-force permutation approach
def find_shortest_tour():
    city_indices = list(cities.keys())[1:]  # Exclude the depot city
    shortest_tour = None
    min_cost = float('inf')
    for perm in permutations(city_indices):
        current_tour = [0] + list(perm) + [0]
        current_cost = total_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour
    return shortest_tour, min_cost

# Get the results
shortest_tour, min_cost = find_shortest_tour()

# Output results
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)