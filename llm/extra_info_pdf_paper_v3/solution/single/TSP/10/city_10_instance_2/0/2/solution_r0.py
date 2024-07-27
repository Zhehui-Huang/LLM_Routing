import numpy as np

# City locations
locations = [
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35),
    (23, 95), (20, 56), (49, 29), (13, 17)
]

# Compute distance matrix
def calc_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

n_cities = len(locations)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = calc_distance(locations[i], locations[j])
        else:
            distance_matrix[i][j] = float('inf')