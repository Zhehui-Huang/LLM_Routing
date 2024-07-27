import math
from itertools import permutations

# Coordinates of the cities (city index: (x, y))
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

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Bruteforce optimization, targeting minimizing max_distance between any two consecutive cities

def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    total_optimal_cost = 0
    
    for perm in permutations(range(1, len(cities))):
        current_tour = [0] + list(perm) + [0]
        max_distance = 0
        total_distance = 0
        last_city = current_tour[0]
        
        for current_city in current_tour[1:]:
            dist = calculate_distance(last_city, current_city)
            total_distance += dist
            if dist > max_distance:
                max_distance = dist
            last_city = current_city
            
        if max_distance < min_max_distance:
            min_max_compare = max_distance
            optimal_tour = current_tour
            total_optimal_cost = total_distance
            
    return optimal_tour, total_optimal_cost, min_max_distance

tour, total_cost, max_dist_consec = find_optimal_tour()

# Output the results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')
print(f'Maximum distance between consecutive cities: {max_dist_consec}')