import math
from itertools import permutations

# Defining the coordinates of each city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Precomputing the distance matrix
num_cities = len(cities)
dist_matrix = [[0]*num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = distance(i, j)