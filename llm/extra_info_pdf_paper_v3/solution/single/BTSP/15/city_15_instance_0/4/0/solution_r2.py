import itertools
import math

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
          (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix to speed up subsequent lookups
distances = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def calculate_tour_cost(tour):
    """Assesses the total and maximum leg cost in a given tour."""
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_cost, max_geometric_distance

# Brute-Force the TSP: try all permutations of the cities (except the depot), searching explicitly for the minimum max leg distance
best_tour = None
best_total_cost = float('inf')
best_max_distance = float('inf')

# Explore all permutations of the cities except the depot
all_permutations = itertools.permutations(range(1, len(cities)))
for perm in all_permutations:
    tour = (0,) + perm + (0,)
    total_cost, max_distance = calculate_tour_cost(tour)
    
    # Update best tour based on smaller max distance or better total cost on ties
    if (max_distance < best_max_distance) or (max_distance == best_max_distance and total_cost < best_total_cost):
        best_tour = tour
        best_total_cost = total_cost
        best_max_distance = max_distance

# Output the results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")