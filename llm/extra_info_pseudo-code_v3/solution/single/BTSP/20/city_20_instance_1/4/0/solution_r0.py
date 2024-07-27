import math
import itertools
from sympy.utilities.iterables import multiset_permutations

def dist(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# City coordinates
cities = [
    (14, 77),  # City 0: Depot
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Evaluate all permutations of cities, excluding the depot (0)
min_max_distance = float('inf')
best_tour = None
tour_cost = 0

for perm in multiset_permutations(range(1, len(cities))):
    current_perm = [0] + list(perm) + [0]
    current_max_distance = 0
    current_tour_cost = 0
    
    # Calculate distances and max distance in the tour
    for i in range(len(current_perm) - 1):
        city_from = current_perm[i]
        city_to = current_perm[i+1]
        current_distance = dist(cities[city_from], cities[city_to])
        current_tour_cost += current_distance
        
        if current_distance > current_max_distance:
            current_max_distance = current_distance
    
    # Check if the current permutation has a smaller bottleneck
    if current_max_distance < min_max_distance:
        min_max_delta = current_max_distance
        best_tour = current_perm
        tour_cost = current_tour_cost
        min_max_distance = current_max_distance
        
        # Shortcut: we find a viable solution and stop (adjust based on required accuracy/performance balance)
        if min_max_distance < 80:  # Preset threshold for acceptable bottleneck
            break

print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min max_distance:.2f}")