import itertools
import math

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
          (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

def euclidean_distance(city1, city2):
    """ Calculates the Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix to speed up lookup
distances = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def calculate_tour_cost(tour):
    """ Returns the total cost and maximum distance between consecutive cities in a tour."""
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Use permutations to find the best path minimizing the maximum distance between cities
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Generate all permutations of city indices starting from 1, as 0 is the depot
all_permutations = itertools.permutations(range(1, len(cities)))
for perm in all_permutations:
    # Always start and end at depot (0)
    tour = (0,) + perm + (0,)
    total_cost, max_distance = calculate_tour_cost(tour)
    
    # Check if found new optimal solution based on max distance
    if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
        best_tour, best_max_distance, best_total_cost = tour, max_distance, total_cost

# Output the results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")