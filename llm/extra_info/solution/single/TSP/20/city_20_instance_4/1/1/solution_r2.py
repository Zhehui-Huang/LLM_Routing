import math
from itertools import permutations

# City coordinates
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

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    dx = cities[city1][0] - cities[city2][0]
    dy = cities[city1][1] - cities[city2][1]
    return math.sqrt(dx * dx + dy * dy)

# Calculate total tour cost
def total_cost(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Find the shortest tour using brute-force
def find_shortest_tour():
    shortest_path = None
    lowest_cost = float('inf')
    for path in permutations(cities.keys() - {0}):
        path = [0] + list(path) + [0]
        cost = total_cost(path)
        if cost < lowest_cost:
            lowest_cost = cost
            shortest_path = path
    return shortest_path, lowest_cost

# Compute the shortest path and cost
shortest_path, total_travel_cost = find_shortest_tour()

# Output the results
print("Tour:", shortest_path)
print("Total travel cost:", total_travel_cost)