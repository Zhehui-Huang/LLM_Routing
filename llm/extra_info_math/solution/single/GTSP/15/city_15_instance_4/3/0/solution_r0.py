import pulp
import math

# Coordinates of cities including the depot
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
               (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21),
               (12, 39)]

# City groups
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
num_groups = len(city_groups)

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two coordinates """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cost matrix based on Euclidean distances
number_of_cities = len(coordinates)
costs = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(number_of_cities)] for i in range(number_of_cities)]