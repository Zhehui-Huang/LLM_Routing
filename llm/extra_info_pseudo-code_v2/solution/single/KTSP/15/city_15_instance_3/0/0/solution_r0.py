import math
import random

# City coordinates
coords = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(a, b):
    return math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)

# Parameters
k = 10
itermax = 100
pmax = 2