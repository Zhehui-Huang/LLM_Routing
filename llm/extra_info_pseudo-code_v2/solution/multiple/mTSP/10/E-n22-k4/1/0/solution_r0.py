import numpy as np
from itertools import permutations

# City coordinates (index corresponds to the city number)
cities = {
    0: (145, 215),  # Depot
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239),
    9: (163, 236), 10: (148, 232), 11: (128, 231),12: (156, 217),
    13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206),
    17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Number of robots
num_robots = 4