import math
import itertools

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Locations of cities (indices match city numbers)
locations = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        x1, y1 = locations[route[i]]
        x2, y2 = locations[route[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def find_optimal_tour():
    min_cost = float('inf')
    best_tour = None
    
    # Generate all combinations of cities, picking one city from each group
    for group_selection in itertools.product(*groups):
        # Check all permutations of the selected cities from each group
        for perm in itertools.permutations(group_selection):
            candidate_tour = [0] + list(perm) + [0]
            cost = calculate_route_cost(candidate_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = candidate_tour

    return best_tour, min_cost

optimal_tour, optimal_cost = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)