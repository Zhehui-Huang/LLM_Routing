import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def calculate_tour_cost(tour):
    """ Calculate total travel cost for a given tour. """
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def find_best_tours():
    n = len(coordinates)
    min_max_cost = float('inf')
    best_sol = None
    
    # Initial setup without using any optimization logic as heuristic
    # Exhaustive split for each robot and then do permutation search over smaller set
    # Due to the manageable number of cities, this brute-force version iterates over all distributions
    
    city_indices = list(range(1, n))  # Exclude depot from permutation list
    half_size = len(city_indices) // 2
    
    for first_half in permutations(city_indices, half_size):
        second_half = [city for city in city_indices if city not in first_half]
        
        for perm_first in permutations(first_half):
            for perm_second in permutations(second_half):
                tours = [
                    [0] + list(perm_first) + [0],
                    [0] + list(perm_second) + [0]
                ]
                costs = [calculate_tour_cost(tour) for tour in tours]
                max_cost = max(costs)
                
                if max_cost < min_max_cost:
                    min_max_cost = max_cost
                    best_sol = (tours, costs)
    
    return best_sol, min_max_cost

best_sol, min_max_cost = find_best_tours()

# Display results
for idx, (tour, cost) in enumerate(zip(best_sol[0], best_sol[1])):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(cost)}")

print(f"Maximum Travel Cost: {round(min_max_cost)}")