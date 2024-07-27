import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities coordinates
cities = [
    (50, 42), # Depot city 0
    (41, 1), 
    (18, 46), 
    (40, 98), 
    (51, 69), 
    (47, 39), 
    (62, 26), 
    (79, 31), 
    (61, 90), 
    (42, 49)
]