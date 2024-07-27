import math
import pulp

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_cities = len(cities)
num_robots = 2

# Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
distances = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Optimizer setup
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) 
                                  for j in range(num_cities) if i != j
                                  for k in range(num_robots)), 
                           cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)),
                          lowBound=0, cat='Continuous')