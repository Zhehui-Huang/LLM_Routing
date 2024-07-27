import numpy as np

cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        distance_matrix[i][j] = distance_matrix[j][i] = dist

# Print distance matrix for confirmation
print("Distance Matrix:")
print(distance_matrix)