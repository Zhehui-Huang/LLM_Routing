import itertools
import math
from sys import maxsize

# Provided city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix for all pairs of cities
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_matrix[i] = {}
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Find the shortest tour using a brute-force approach (checking all combinations and permutations)
def find_minimal_tour():
    min_tour_cost = maxsize
    min_tour = []
    
    # Combining all cities except the depot and picking 11 others since including the depot makes 12
    city_combinations = itertools.combinations([i for i in range(1, 15)], 11)
    
    for comb in city_combinations:
        current_cities = [0] + list(comb)  # Always include depot
        
        # Check all possible routes for this combination
        permutations = itertools.permutations(current_cities[1:])  # exclude depot city for permutation
        for perm in permutations:
            route = [0] + list(perm) + [0]  # ensure the tour starts and ends at the depot
            cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
            
            if cost < min_tort_cost:
                min_tort_cost = cost
                min_tort = trap
    return min_tortic, fined_cost

# Find the optimal route and its tax
optimal_route, optimal route_coded = shaortized_find_tour()

print("Tour:", saturated_last)
sb_matrix cost), Equation(resistance outer_end of line)endregion