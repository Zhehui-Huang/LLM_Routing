import numpy as np
import math
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of robots
num_robots = 8

# Initial depot city for all robots
initial_depot = 0