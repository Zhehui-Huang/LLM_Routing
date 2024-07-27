import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# ACO Parameters
antnum = 10
cyclenum = 100
inittrail = 1.0
alpha = 1
beta = 5
rho = 0.1

# Calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Initialize pheromone trails
pheromone = { (i, j): inittrail for i in cities for j in cities if i != j }
heuristic = { (i, j): 1/distance(i, j) for i in cities for j in cities if i != j and i != j }