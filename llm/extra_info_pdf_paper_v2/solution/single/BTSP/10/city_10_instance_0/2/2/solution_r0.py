import math
from itertools import permutations

# Data for the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 97),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Generating all possible tours
def generate_tours():
    nodes = list(cities.keys())
    for perm in permutations(nodes[1:]):
        yield [0] + list(perm) + [0]

# Evaluate the tours to find the optimal one
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = None
    
    for tour in generate_tours():
        max_distance = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, min_max_distance

# Get the optimal tour information
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output according to specified format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")