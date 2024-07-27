import math
from itertools import product

# City coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
          (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# City groups
groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two city coordinates."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of cities, choosing one city from each group
all_combinations = list(product(*groups))

# Track the minimum distance and corresponding tour
min_distance = float('inf')
best_tour = []

# Compute the travel cost for each combination
for combo in all_combinations:
    # Including the depot city as starting and ending point
    tour = [0] + list(combo) + [0]
    # Calculate the total distance of this tour
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Update the minimum distance and best tour found
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = tour

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")