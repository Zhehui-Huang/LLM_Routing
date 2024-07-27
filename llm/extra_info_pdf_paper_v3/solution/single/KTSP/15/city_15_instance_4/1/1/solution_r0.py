import math
from itertools import combinations

# Cities as provided in the problem statement, depot city included
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

# Create a distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]