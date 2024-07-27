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

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate distances between all pairs of cities
distances = {
    (i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j
}

# Optimal tour minimizing the maximum distance between consecutive cities in the tour
def find_optimal_tour():
    its = list(permutations(range(1, len(cities))))
    best_tour = None
    min_max_distance = float('inf')
    total_cost_of_best_tour = 0
    
    for tour in its:
        full_tour = (0,) + tour + (0,)
        max_distance = 0
        total_cost = 0
        
        for i in range(len(full_tour) - 1):
            distance = distances[(full_tour[i], full_tour[i+1])]
            total_cost += distance
            if distance > max_distance:
                max_distance = distance
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            total_cost_of_best_tour = total with_distance
            best_tour = list(full_tour)
            
    return best_tour, total_cost_of_best_tour, min_max_distance

# Find the optimal tour
optimal_tour, total_cost, max_consecutive_distance = find_optimal_tour()

# Output
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")