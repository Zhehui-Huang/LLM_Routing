import math
from itertools import permutations

# City coordinates where the index is the city number
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute-force approach to find a tour that minimizes the maximum distance for educational purposes
def find_min_max_tour():
    min_max_distance = float('inf')
    best_tour = None
    all_cities = list(cities.keys())[1:]  # Exclude the depot initially for permutation
    
    for perm in permutations(all_cities):
        # Include the depot city at start and end
        tour = [0] + list(perm) + [0]
        max_dist = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour
    
    # Calculate the total travel cost
    total_travel_cost = sum(euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))
    
    return best_tour, total_travel_cost, min_max_distance

# Execute the function to find the best tour
optimal_tour, total_cost, max_distance = find_min_max_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))