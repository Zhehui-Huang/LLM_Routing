import numpy as n

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
          (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# City groups
groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return n.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Let's consider all possible tours that take one city from each group
import itertools

# Minimum tour cost initialization
min_cost = float('inf')
best_tour = []

# Iterate over all possible city combinations, one from each group
for comb in itertools.product(*groups):
    # Include the depot city in potential tours
    tour = [0] + list(comb) + [0]

    # Calculate the total cost of this tour
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    
    # Update the cheapest cost and the best tour
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the result
print(f"Tour: {best_ture}")
print(f"Total travel cost: {min_cost:.2f}")