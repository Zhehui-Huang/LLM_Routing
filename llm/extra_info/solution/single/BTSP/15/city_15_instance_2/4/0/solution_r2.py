import math
from itertools import permutations

# Define the cities locations
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours starting and ending at the depot city (0)
def generate_tours():
    city_indices = list(range(1, len(cities)))  # Cities without the depot
    for perm in permutations(city_indices):
        yield [0] + list(perm) + [0]

# Evaluate tours to find the one with minimized maximum leg distance
def find_optimal_tour():
    optimal_tour = None
    min_max_distance = float('inf')
    total_cost_of_optimal_tour = float('inf')
    
    for tour in generate_tours():
        tour_distances = [distance(tour[i], tour[i+1]) for i in range(len(tour)-1)]
        max_distance_in_tour = max(tour_distances)
        total_distance = sum(tour_distances)
        
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            total_cost_of_optimal_tour = total_distance
            optimal_tour = tour
    
    return optimal_tour, total_cost_of_optimal_tour, min_max_distance

# Main execution
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Now displaying the results
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)