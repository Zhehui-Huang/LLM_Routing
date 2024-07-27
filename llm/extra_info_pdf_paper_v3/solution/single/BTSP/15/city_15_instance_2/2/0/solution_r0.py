import math
from itertools import permutations

# Define coordinates for each city
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours starting and ending at the depot city 0
def generate_tours():
    all_cities = list(cities.keys())[1:]  # exclude depot city
    for city_order in permutations(all_cities):
        tour = [0] + list(city_order) + [0]
        yield tour

# Evaluate each tour to find the one that minimizes the maximum leg distance
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for tour in generate_tours():
        max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < total_min_cost):
            best_tour = tour
            best_max_distance = max_distance
            total_min_cost = total_cost
            
    return best_tour, total_min_cost, best_max_distance

# Obtain the optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")