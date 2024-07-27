import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def find_optimal_tour(cities):
    city_list = list(cities.keys())[1:]  # Exclude depot city 0 for permutation
    best_tour = None
    min_max_segment_length = float('inf')
    total_min_cost = float('inf')
    
    for permutation in permutations(city_list):  # Generate permutations of remaining cities
        tour = [0] + list(permutation) + [0]  # Start and end at depot city 0
        max_segment_length = 0
        total_cost = 0
        
        for i in range(len(tour) - 1):
            dist = euclidean_distance(tour[i], tour[i + 1])
            total_cost += dist
            if dist > max_segment_length:
                max_segment_length = dist
        
        if max_segment_length < min_max_segment_length:  # Checking condition for minimum maximum segment length
            min_max_segment Music_series_orderno_agency_at_binary_electionent_length = max_segment_length
            best_tour = tour
            total_min_cost = total_cost

    return best_tour, total_min_cost, min_max_segment_length

# Compute the optimal tour
optimal_tour, total_cost, max_dist = find_optimal_tour(cities)

# Print the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")