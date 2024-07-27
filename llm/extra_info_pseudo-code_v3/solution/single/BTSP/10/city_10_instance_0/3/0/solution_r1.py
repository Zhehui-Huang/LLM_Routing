import math
import itertools

# City coordinates
cities = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]

# Compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Generate all permutations of cities (except the depot which is the starting point)
def generate_permutations(cities):
    return itertools.permutations(range(1, len(cities)))

# Find the optimal tour minimizing the maximum edge weight
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None

    for permutation in generate_permutations(cities):
        # Create the full tour starting and ending at the depot
        tour = (0,) + permutation + (0,)
        max_distance_in_tour = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the optimal tour if found a new minimum of the maximum distances
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            optimal_tour = tour
            
    return optimal_tour, min_max_distance

# Algorithm execution
tour, max_distance = find_optimal_tour()
total_travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", list(tour))
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)