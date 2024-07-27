import math
from itertools import permutations

# Given city locations
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14),
    13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# City groups (respecting the exactly-one-in-a-set constraint of GTSP)
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(route):
    """ Calculate the total distance of a given tour or route """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return total_distance

# Use permutations to try every combination of picking one city from each group, then find the best tour
def find_shortest_tour(groups):
    best_route = None
    best_distance = float('inf')
    
    # Generate all permutations of one from each group
    for combination in permutations([g[0] for g in groups]):
        for indices in permutations(combination):
            indices = (0,) + indices + (0,)  # Start and end at the depot (City 0)
            distance = calculate_total_distance(indices)
            if distance < best_distance:
                best_distance = distance
                best_route = indices
                
    return best_route, best_distance

# Calculate the optimal route
best_route, best_distance = find_shortest_tour(groups)

# Print the optimal tour and its cost
print(f"Tour: {list(best_route)}")
print(f"Total travel cost: {best_distance:.2f}")