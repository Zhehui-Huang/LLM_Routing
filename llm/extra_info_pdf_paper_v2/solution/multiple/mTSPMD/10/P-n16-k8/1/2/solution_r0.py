import numpy as np
import random

# Define coordinates of each city (indexed from 0 to 15)
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Define the robot depots
depot_cities = list(range(8))  # Depots are cities from 0 to 7
robots = {i: depot_cities[i] for i in range(8)}

# All cities should be eventually covered
all_cities = set(city_coords.keys())