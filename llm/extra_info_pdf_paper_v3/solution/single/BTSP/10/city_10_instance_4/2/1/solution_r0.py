import math
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all permutations of the cities (excluding the depot city to reduce computational complexity)
perms = permutations(list(cities.keys())[1:])

# Initialize variables to store the best tour
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Evaluate each permutation
for perm in perms:
    tour = [0] + list(perm) + [0]  # Complete tour starting and ending at the depot city
    total_cost = 0
    max_distance = 0
    
    # Calculate the total cost and max distance
    for i in range(len(tour) - 1):
        dist = distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Compare and update the best tour found
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_total_cost = total_cost
        best_tour = tour

# Output the best tour, total cost, and maximum distance
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))