import itertools
import math

# Coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_optimal_tour():
    """Finds the optimal tour of exactly 6 cities starting and ending at the depot city."""
    min_tour = None
    min_cost = float('inf')
    
    # Generate combinations of 5 cities since city 0 is fixed as start and end
    city_combinations = itertools.combinations(range(1, 15), 5)
    
    for combo in city_combinations:
        # Always include the depot city at the start and end
        full_tour = (0,) + combo + (0,)
        
        # Generate all permutations of the selected cities to ensure shortest path
        for perm in itertools.permutations(combo):
            current_tour = (0,) + perm + (0,)
            current_cost = sum(calculate_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            
            if current_cost < min_cost:
                min_cost = current_cost
                min_tour = current_tour

    return min_tour, min_cost

# Get the optimal tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()

# Print the results
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {int(optimal_cost)}")