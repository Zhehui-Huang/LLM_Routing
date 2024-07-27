import math
from itertools import permutations

# Cities Coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Compute Euclidean distance between two cities given their indexes
def calculate_distance(i, j):
    return math.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])

# Generate all possible city tours starting and ending at the depot (city 0)
def all_possible_tours():
    city_indices = list(range(1, len(cities)))  # cities without the depot
    for perm in permutations(city_indices):
        yield [0] + list(perm) + [0]

# Find the tour that minimizes the maximum distance between consecutive cities
def find_optimal_tour():
    optimal_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for tour in all_possible_tours():
        max_distance = max(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour
            total_min_cost = total_cost
        elif max_distance == min_max_equal and total_cost < total_min_cost:
            optimal_tour = tour
            total_min_cost = total_cost
            
    return optimal_tour, total_min_cost, min_max_distance

# Get optimal tour and relevant costs
optimal_tour, total_min_cost, min_max_distance = find_optimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")