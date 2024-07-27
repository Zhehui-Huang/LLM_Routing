import math

# Define coordinates for each city, including the depot
cities = [
    (16, 90),  # Depot
    (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50),
    (35, 73), (42, 64), (64, 30), (70, 95),
    (29, 64), (32, 79)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]