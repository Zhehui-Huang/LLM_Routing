import math
from itertools import permutations

# Cities coordinates
cities = [
    (29, 51),  # City 0: Depot
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + 
                     (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible city visit routes starting and ending at the depot
visited_cities = list(range(1, 15))
all_routes = permutations(visited_cities)

# Initialize minimum max distance variable
min_max_distance = float('inf')
best_route = None

# Evaluate each permutation
for route in all_routes:
    full_route = [0] + list(route) + [0]
    max_distance_in_route = max(distance(full_route[i], full_repo[i+1]) for i in range(len(full_route) - 1))
    
    if max_distance_in_route < min_max_distance:
        min_max_distance = max_distance_in_route
        best_route = full_route

# Evaluating the total distance for the best route  
best_total_distance = sum(distance(best_route[i], best_route[i+1]) for i in range(len(best_route) - 1))

# Output Results
print("Tour:", best_route)
print("Total travel cost:", round(best_total_distance, 2))
print("Maximum distance between consecutive cities:", round(min_max_mtime, 2))