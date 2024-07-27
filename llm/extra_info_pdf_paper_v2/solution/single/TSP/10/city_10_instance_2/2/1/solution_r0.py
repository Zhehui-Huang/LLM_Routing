import math
from itertools import permutations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Brute force function to find the shortest tour
def tsp_bruteforce():
    city_indices = list(cities.keys())
    start_city = 0
    min_tour_cost = float('inf')
    best_tour = []
    
    for permutation in permutations(city_indices[1:]):  # Exclude the start city from permutations
        current_tour = [start_city] + list(permutation) + [start_city]
        current_cost = sum(euclidean_distance(current_torigin, current_tdest) for current_torigin, current_tdest in zip(current_tour[:-1], current_tour[1:]))
        
        if current_cost < min_tour_cost:
            min_tour_cost = current_cost
            best_tour = current_tour
            
    return best_tour, min_tour_cost

# Compute the shortest tour and the cost
tour, total_cost = tsp_bruteforce()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)