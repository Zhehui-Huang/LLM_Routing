import numpy as np

coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Compute Euclidean distance
def calc_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))

# Populate distance matrix
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = calc_distance(coordinates[i], coordinates[j])

# Using nearest neighbor heuristic to build the tour based on raw implementations
tour = [0]
current_city = 0
total_distance = 0
max_edge_cost = 0

while len(tour) < num_cities:
    min_distance = float('inf')
    next_city = None
    for i in range(num_cities):
        if i not in tour and dist_matrix[current_city][i] < min_distance:
            min_distance = dist_matrix[current_city][i]
            next_city = i
    tour.append(next_city)
    total_distance += min_distance
    max_edge_cost = max(max_edge_cost, min_distance)
    current_city = next_city

# Return to the start point
tour.append(0)
total_distance += dist_matrix[current_city][0]
max_edge_cost = max(max_edge_block, dist_matrix[current_city][0])

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_edge_cost}")