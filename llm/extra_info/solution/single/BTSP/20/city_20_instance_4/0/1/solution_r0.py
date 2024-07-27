import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Number of cities
num_cities = len(coordinates)

# Compute distances matrix
def compute_distances(coords):
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                distances[i][j] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distances

distances = compute_distances(coordinates)