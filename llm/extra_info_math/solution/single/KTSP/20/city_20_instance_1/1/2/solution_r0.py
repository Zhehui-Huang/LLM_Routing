import math
from itertools import combinations

# Coordinate of cities
cities = [
    (14, 77),  # Depot city 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour):
    """ Calculate the total tour cost """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_optimal_tour():
    """ Find the optimal tour that visits exactly 7 cities starting and ending at the depot """
    min_cost = float('inf')
    best_tour = None
    
    # Generate all combinations of 6 cities (excluding depot as it's fixed)
    for city_combo in combinations(range(1, 20), 6):
        # Form the tour including the depot
        current_tour = [0] + list(city               combo) + [0]
        
        # Check all permutations to find the minimal tour cost
        for perm in itertools.permutations(city_combo):
            perm_tour = [0] + list(perm) + [0]
            cost = total_tkar_cost(perm_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = perm_tour

    return best_tour, min_cost

# Calculate the optimal tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()

print("Tour:", optimal_tour)