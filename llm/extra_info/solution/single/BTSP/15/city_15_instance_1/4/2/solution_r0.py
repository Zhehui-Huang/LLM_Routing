import math

# Define the cities' coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20),
          (18, 61), (40, 57), (57, 30), (36, 12),
          (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

# Function to compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

# Compute the distances matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]