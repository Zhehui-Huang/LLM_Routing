import math
from pulp import *

# Cities and their coordinates excluding the depot city
coords = {
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}
coords[0] = (145, 215)  # Depot city

# Number of salesmen (robots)
robots = 4

# Calculating pairwise Euclidean distances
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = {(i, j): distance(coords[i], coords[j]) for i in coords for j in coords if i != j}

# Initialize problem
problem = LpProblem("mTSP_Python", LpMinimize)