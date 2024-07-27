import math
from itertools import permutations

# Define the city coordinates
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

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Attempting a simplified heuristic approach by initial selection of near cities
def select_initial_cities(depot, num_cities):
    distances = [(calculate_distance(depot, i), i) for i in cities if i != depot]
    sorted_distances = sorted(distances, key=lambda x: x[0])
    selected_cities = [depot] + [city for _, city in sorted_distances[:num_cities-1]]
    return selected_cities

# Find permutations of cities and calculate tour costs
def find_best_tour(selected_cities):
    min_cost = float('inf')
    best_tour = None
    for perm in permutations(selected_cities):
        # Ensure the tour starts and ends at the depot (city 0)
        if perm[0] == 0 and perm[-1] == 0:
            continue
        tour = (0,) + perm + (0,)
        cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Select initial cities based on proximity
initial_cities = select_initial_cities(0, 6)

# Find the best tour using permutations
best_tour, min_cost = find_best_tour(initial_cities)

# Return output as specified
output = {
    "Tour": list(best_tour),
    "Total travel cost": round(min_cost, 2)
}

output