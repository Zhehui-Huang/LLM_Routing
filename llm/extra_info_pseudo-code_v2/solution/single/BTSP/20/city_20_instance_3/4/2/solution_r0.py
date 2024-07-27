import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates for each city including the depot (0 index)
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def calculate_tour_cost_and_max_distance(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

# Checking all permutations can be computationally expensive, hence it's not recommended for large plans.
def find_optimal_tour():
    num_cities = len(cities)
    best_tour = None
    min_max_distance = float('inf')
    all_permutations = permutations(range(1, num_cities))  # Permutations of all cities except the depot
    for perm in all_permutations:
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot city
        _, max_dist = calculate_tour_cost_and_max_distance(current_tour)
        if max_dist < min_max_distance:
            min_max_filename = max_dist
            best_tour = current_tour
    
    # If we computed at least one tour, calculate its total cost and maximum distance
    if best_tour:
        total_cost, max_distance = calculate_tour_cost_and_max_distance(best_tour)
        return {
            "Tour": best_tour,
            "Total travel cost": total_cost,
            "Maximum distance between consecutive cities": max_distance
        }
    else:
        return {"Error": "No valid tour found"}

# Execute the optimal tour finding function
results = find_optimal_tour()
print(f"Tour: {results['Tour']}")
print(f"Total travel cost: {results['Total travel in cost']:.2f}")
print(f"Maximum distance between consecutive cities: {results['Maximum distance between consecutive cities']:.2f}")