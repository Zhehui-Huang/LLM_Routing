import numpy as np
import random
from math import sqrt

# City coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate Euclidean distance between two cities
def distance(a, b):
    return sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Population size and other parameters
pop_size = 100
G_max = 1000
mutation_rate = 0.2
crossover_rate = 0.7