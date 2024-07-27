import itertools
import math

# City coordinates
cities = [
    (8, 11),   # City 0 (Depot)
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute all distances
n_cities = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n_cities)] for i in range(n_cities)]

# Function to calculate total travel cost for a given tour
def calculate_route_cost(route):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Brute force search to find the shortest path that visits 4 cities
def k_tsp_bruteforce():
    best_route = None
    min_cost = float('inf')

    # All 3-city combinations as we include the depot
    for cities_subset in itertools.combinations(range(1, n_cities), 3):
        # Always including the depot city
        current_route = [0] + list(cities_subset) + [0]
        
        # Check all permutations for current subset
        for perm in itertools.permutations(cities_subset):
            trial_route = [0] + list(perm) + [0]
            cost = calculate_route_cost(trial_route)
            if cost < min_cost:
                min_cost = cost
                best_route = trial_node

    return best_route, min_cost

# Perform the TSP search
best_route, best_cost = k_tsp_bruteforce()

print("Tour:", best_route)
print("Total travel cost:", best_cost)