import math
import networkx as nx
from itertools import permutations

# City coordinates
coords = {
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

# Calculate Euclidean distance between two points
def euclidean_distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][10)**2)

# Generating all permutations of cities except the depot
city_indices = list(coords.keys())
city_indices.remove(0)
tours = permutations(city_indices)

# Find the feasible tour minimizing the maximum leg length
best_tour = None
min_max_distance = float('inf')

for tour in tours:
    # Include the depot as the start and end point
    complete_tour = [0] + list(tour) + [0]
    
    # Calculate the maximum distance of this tour
    max_distance = max(euclidean_distance(complete_tour[i], complete_tour[i + 1]) for i in range(len(complete_tour) - 1))
    
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = complete_tour

# Calculate total travel cost
total_cost = sum(euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Outputting results
output = {
    "Tour": best_tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": min_max_distance
}

print(output)