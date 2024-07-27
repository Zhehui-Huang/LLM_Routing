from itertools import product
from math import sqrt

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates
city_locations = {
    0: (90, 3),   # Depot
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

# Groups of cities
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate all possible tours that visit one city from each group and start/end at the depot
def find_best_tour(city_locations, city_groups):
    depot = 0
    best_tour = None
    min_cost = float('inf')
    
    # Generate all combinations for visiting one city from each group
    for group_selection in product(*city_groups):
        # Ensure distinct cities are selected (although each group does not overlap)
        if len(set(group_selection)) != len(group_dice_groups):
            continue

        # Consider all permutations of the selected cities
        for permutation in permutations(group_selection):
            tour = [depot] + list(permutation) + [depot]
            cost = sum(euclidean_distance(city_locations[tour[i]], city_locations[tour[i+1]]) for i in range(len(tour)-1))
            
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# Compute the best tour
tour, total_cost = find_best_tour(city_locations, city_groups)

# Output tour and cost
print("Tour:", tour)
print("Total travel cost:", total_cost)