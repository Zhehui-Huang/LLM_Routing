import math

# Coordinates of cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(point1, point2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Distance matrix
distance_matrix = [
    [euclidean_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]