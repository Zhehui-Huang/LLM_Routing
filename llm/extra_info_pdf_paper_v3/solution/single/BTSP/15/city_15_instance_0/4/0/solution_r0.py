import itertools
import math

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
          (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all pairs distances
distances = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def calculate_tour_cost(tour):
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Explore all permutations of the cities except the depot
all_permutations = itertools.permutations(range(1, len(cities)))
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for perm in all_permutations:
    # Always start and end at depot (0)
    tour = (0,) + perm + (0,)
    total_cost, max_distance = calculate_tour_cost(tour)
    
    if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_data):
        best_tour = tour
        best_total_cost = total_cost
        best_max_distance = max_distance

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")