import math
from itertools import permutations

# Coordinates for the depot and the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create a distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Function to calculate travel cost for a tour
def tour_cost(tour):
    return sum(distance_frames[tour[i]][tour[i+1]] for i in range(len(tour)-1))