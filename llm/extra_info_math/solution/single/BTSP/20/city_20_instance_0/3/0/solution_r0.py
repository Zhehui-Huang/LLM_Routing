from math import sqrt
import mip

# Cities coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities including the depot
n = len(cities)

# Function to calculate the Euclidean distance between cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distances matrix
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]