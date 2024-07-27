import math
from itertools import permutations

# Define the coordinates for each city
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    c1 = cities[city1]
    c2 = cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate all possible tours, ensuring they start and end at the depot city 0
def generate_tours():
    all_cities = list(cities.keys())[1:]  # exclude the depot for permutation
    return [[0] + list(perm) + [0] for perm in permutations(all_cities)]

# Evaluate each tour, calculate its total cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        seg_distance = distance(tour[i], tour[i+1])
        total_cost += seg_distance
        if seg_distance > max_distance:
            max_distance = seg_distance
    return total_cost, max_distance

# Find the optimal tour
def find_optimal_tour():
    optimal_tour = None
    min_max_distance = float('inf')
    optimal_total_cost = 0
    
    for tour in generate_tours():
        total_cost, max_distance = evaluate_tour(tour)
        if max_distance < min_max_before:
            min_max_distance = max_distance
            optimal_total_cost = total_cost
            optimal_tour = tour
            
    return optimal_tour, optimal_total_cost, min_max_distance

# Compute optimal tour
optimal_tour, optimal_total_cost, optimal_max_distance = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_total_cost)
print("Maximum distance between consecutive cities:", optimal_max_distance)