import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# City coordinates index by city ID
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Grouping cities
city_groups = {0: [8, 12, 14], 1: [7, 10, 11], 2: [4, 6, 9], 3: [1, 3, 13], 4: [2, 5]}

# Initialize the linear programming problem
problem = LpProblem("RobotRouting", LpMinimize)