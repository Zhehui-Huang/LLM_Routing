import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

# Given cities and their coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Number of cities
num_cities = len(cities)

# Calculate Euclidean distance between each pair of cities
def calc_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = calc_adistance(cities[i], cities[j])

# Generate a minimum spanning tree using the distances
mst = minimum_spanning_tree(distances).toarray()

# Using depth-first search ordering starting from the depot (index 0)
order = depth_first_order(mst, directed=False, i_start=0)[0]

# Append the initial city to complete the tour
tour = list(order) + [0]

# Calculate total travel cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour)-1):
    distance = distances[tour[i], tour[i+1]]
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")