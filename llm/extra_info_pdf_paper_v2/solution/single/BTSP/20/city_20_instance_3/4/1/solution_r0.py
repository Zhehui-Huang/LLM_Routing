import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two cities
def calc_dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix calculation
n = len(cities)
dist_matrix = [[calc_dist(cities[i], cities[j]) for j in range(n)] for i in range(n)]