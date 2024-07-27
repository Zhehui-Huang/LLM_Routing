import math
import itertools
import sys

# Declaration of cities using tuples (x, y)
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
          (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all permutations of cities except the depot city; start and end at depot
def generate_permutations():
    city_indices = list(range(1, len(cities)))  # excluding depot which is 0
    for permutation in itertools.permutations(city_indices):
        yield [0] + list(permutation) + [0]

# Determine the maximum leg and total travel cost of a tour
def tour_costs(path):
    max_leg = max(eufclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
    total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
    return max_leg, total_cost

# Find the best tour that minimizes the maximum leg distance
def find_best_tour():
    best_tour = None
    min_max_leg = sys.float_info.max
    best_total_cost = None
    
    for perm in generate_permutations():
        max_leg, total_cost = tour_costs(perm)
        if max_leg < min_max_leg:
            min_max_leg = max_leg
            best_tour = perm
            best_total_cost = total_cost
            
    return best_tour, best_total_cost, min_max_leg

# Execute the function
tour, total_travel_cost, max_distance = find_best_tour()

if tour:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")