import math
from itertools import permutations, combinations
from pulp import *

# City coordinates provided in the problem statement
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Number of cities
n = len(cities)

# Euclidean distance between two city coordinates
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Constructing the distance matrix
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Using PuLP to solve the problem
problem = LpProblem("Minimax_TSP", LpMinimize)

# Boolean variables x_ij which is 1 if path from i to j is taken
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat="Binary")

# The maximum distance between consecutive cities - this is what we want to minimize
T_max = LpVariable("T_max", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum distance between consecutive cities
problem += T_max, "Minimized Maximum Leg Distance"

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Exit_{i}"
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i][j] <= T_max, f"Max_Constraint_{i}_{j}"

# Subtour elimination constraints using u variables
u = LpVariable.dicts('u', list(range(n)), lowBound=0, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n-1

# Solve the problem
problem.solve(PULP_CBC_CMD(msg=0))  # msg=0 for no output logs from CBC solver

# Extract the solution
tour = []
for v in problem.variables():
    if v.varValue == 1 and 'x_' in v.name:
        i, j = map(int, v.name.split('_')[1].split(','))
        tour.append((i, j))

# Organize tour to human-readable format
sorted_tour = []
current_location = 0  # assume start at depot (0)
sorted_tour.append(current_location)

for _ in range(n-1):  # loop less 1 because current_location starts at start point.
    for t in tour:
        if t[0] == current_location:
            current_location = t[1]
            sorted_tour.append(current_location)
            break

sorted_tour.append(0)  # returning to the start point

# Calculating the output values
max_distance = value(T_max)
total_travel_cost = sum(distances[sorted_tour[i]][sorted_tour[i+1]] for i in range(len(sorted_tour)-1))

# Output result
print("Tour:", sorted_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)