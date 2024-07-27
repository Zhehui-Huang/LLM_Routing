import pyomo.environ as pyo
import math

# Function to compute Euclidean distance between cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates where each key is city index and value is coordinates (x, y)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of depots and robots
num_depots = 7
num_robots = 8

# Distance matrix
n = len(cities)
distance_matrix = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Depot allocation (assuming all robots start from depot city 0)
depot_allocation = {0: num_robots}