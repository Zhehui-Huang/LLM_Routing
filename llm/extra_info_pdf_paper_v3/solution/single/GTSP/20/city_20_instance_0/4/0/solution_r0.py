import math
from itertools import product

# City coordinates including the depot
coordinates = [
    (8, 11),  # Depot
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46),
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Precompute distances between all pairs of cities
distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Iterate over all possible combination of one city from each group
min_cost = float('inf')
optimal_tour = None

for tour in product(groups[0], groups[1], groups[2]):
    # Add the depot city at the start and end of the tour
    full_tour = [0] + list(tour) + [0]
    
    # Compute the travel cost of the full tour
    cost = sum(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour)-1))
    
    # Update the best found solution
    if cost < min_cost:
        min_cost = cost
        optimal_tour = full_tour

# Output the result
print("Tour:", optimal_tour)
print("Total travel cost:", round(min_cost, 2))