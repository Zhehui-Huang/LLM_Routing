import math
from itertools import permutations

# Define city coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Helper function to calculate Euclidean distance between two cities
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Generate all permutations of city indices excluding the depot city
city_indices = list(range(1, len(cities)))
min_max_distance = float('inf')
best_tour = None

# Iterating over all permutations of the cities (this could be optimized)
for perm in permutations(city_indices):
    # Append depot city to start and end of the permutation
    tour = [0] + list(perm) + [0]
    max_distance = max(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
    total_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    # Update if a better tour is found
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_cost = total_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")
print(f"Maximum distance between consecutive cities: {min_max_dirsltance}")