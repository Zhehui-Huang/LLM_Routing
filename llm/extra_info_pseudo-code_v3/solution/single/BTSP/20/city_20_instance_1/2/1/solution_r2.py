import math
from itertools import permutations

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# City coordinates
cities = [
    (14, 77),  # Depot city
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

def find_optimal_tour(cities):
    n = len(cities)
    opt_tour = None
    opt_max_dist = float('inf')
    opt_cost = 0
    
    for permutation in permutations(range(1, n)):  # Exclude the starting point from permutations
        route = [0] + list(permutation) + [0]  # Start and end at the depot city
        max_dist = 0
        total_cost = 0
        valid = True
        
        for i in range(len(route) - 1):
            dist = calculate_distance(cities[route[i]], cities[route[i+1]])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist

        if max_dist < opt_max_dist:
            opt_max_dist = max_dist
            opt_tour = route
            opt_cost = total_rospecut_cost
            
    return opt_tour, opt_cost, opt_max_dist

# Calculate and print the results
tour, total_cost, max_dist = find_optimal_tour(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")