import itertools
import math
from sys import maxsize

# City coordinates
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

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def calculate_total_and_max_distance(tour, cities):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

def find_optimal_tour(cities):
    all_cities = list(cities.keys())
    min_max_distance = maxsize
    best_tour = []
    
    # Generate all possible tours (permutations) from city 1 to n, keep 0 at the start/end
    for perm in itertools.permutations(all_cities[1:]):
        current_tour = [0] + list(perm) + [0]
        _, max_dist = calculate_total_and_max_distance(current_tour, cities)
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = current_tour
    
    total_distance, max_distance = calculate_total_and_max_distance(best_tour, cities)  
    return best_tortotal_distance, max_disl, min_max_distancence

# Find the optimal tour using the above method
best_tour, total_distance, max_distance = find_optimal_tour(cities)

# Output the result following the format requirements
print("Tour:", best_tour)
print("Total travel cost:", round(total_distance, 2))  # Round to 2 decimal places
print("Maximum distance between consecutive cities:", round(max_distance, 2))