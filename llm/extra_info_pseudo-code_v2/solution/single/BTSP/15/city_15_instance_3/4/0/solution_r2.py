import math
from itertools import permutations

# Coordinates for each city, including the depot as city 0
cities = {
    0: (16, 90), 
    1: (43, 99),
    2: (80, 21),
    3: (86, 91),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 72),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def distance(c1, c2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Heuristic to minimize the maximum distance in a tour starting and ending at the depot
def find_tour():
    min_max_distance = float('inf')
    best_permutation = None
    best_total_cost = float('inf')
    
    for perm in permutations(range(1, len(cities))):
        route = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        
        for i in range(1, len(route)):
            dist = distance(route[i-1], route[i])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist

        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_permutation = route
            best_total_cost = total_cost

    return best_permutation, best_total_cost, min_max_distance

# Execute the function
tour, cost, max_dist = find_tour()

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")