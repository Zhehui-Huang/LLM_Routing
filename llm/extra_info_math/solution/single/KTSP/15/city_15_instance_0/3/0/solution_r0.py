import math
from itertools import combinations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def get_total_tour_cost(tour, coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coords[tour[i]], coords[tour[i+1]])
    return total_cost

def solve_min_k_tsp(cities, k):
    coords = [tuple(city) for city in cities]
    min_cost = float('inf')
    best_tour = None
    
    # Generate all combinations of cities choosing (k-1) because we include city 0 implicitly
    for city_set in combinations(range(1, len(cities)), k-1):
        current_cities = [0] + list(city_instance)
        current_cities.append(0)  # Add the depot city at the end to form a loop
        
        # Check all possible permutations of the chosen cities to find minimal tour
        perms = permutations(current_cities[1:-1])
        for perm in perms:
            tour = [0] + list(perm) + [0]  # form the full tour
            cost = calculate_total_tour_cost(tour, coords)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Cities coordinates
cities = [
    (9, 93),   # Depot city (index 0)
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Find the optimal tour visiting exactly 4 cities including the depot
tour, total_cost = solve_min_k_tsp(cities, 4)

print("Tour:", tour)
print("Total travel cost:", total_cost)