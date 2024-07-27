import math
from itertools import permutations, combinations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_tour_cost(tour, coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coords[tour[i]], coords[tour[i+1]])
    return total_cost

def solve_min_k_tsp(coords, k):
    min_cost = float('inf')
    best_tour = None
    
    # Generate all combinations of cities choosing (k-1) because we include city 0 implicitly
    for city_set in combinations(range(1, len(coords)), k-1):
        current_cities = [0] + list(city_set)
        # Generate all permutations of the chosen cities
        perms = permutations(current_cities[1:])
        for perm in perms:
            tour = [0] + list(perm) + [0]  # form the full tour
            cost = calculate_total_tour_cost(tour, coords)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Coordinates of each city
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Find the optimal tour visiting exactly 4 cities (including the depot)
tour, total_cost = solve_min_k_tsp(cities, 4)

print("Tour:", tour)
print("Total travel cost:", total_cost)