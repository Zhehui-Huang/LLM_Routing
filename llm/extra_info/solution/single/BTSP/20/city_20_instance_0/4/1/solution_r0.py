import math
from itertools import permutations

# Cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71), 
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all possible tours
def generate_tours():
    city_indices = list(cities.keys())[1:]  # Exclude the depot from permutations
    perms = permutations(city_indices)
    for perm in perms:
        # Always start and end at the depot (city 0)
        yield [0] + list(perm) + [0]

# Calculate total cost and maximum distance between consecutive cities
def tour_evaluation(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Find the optimal tour minimizing the maximum leg distance
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = []
    for tour in generate_tours():
        total_cost, max_distance = tour_evaluation(tour)
        if max_distance < min_max_distance:  # Updating the best found
            min_max_distance = max_distance
            optimal_tour = tour
            optimal_total_cost = total_cost
    return optimal_tour, optimal_total_cost, min_max_distance

# Main execution to find the best tour
optimal_tour, optimal_total_cost, optimal_max_distance = find_optimal_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_total_cost}")
print(f"Maximum distance between consecutive cities: {optimal_max_distance}")