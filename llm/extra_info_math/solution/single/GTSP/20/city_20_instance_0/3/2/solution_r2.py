import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, PULP_CBC_CMD

# Define the coordinates of each city
coordinates = {
    0: (8, 11),   # Depot
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((coordinates[c1][0] - coordinates[c2][0]) ** 2 + (coordinates[c1][1] - coordinates[c2][1]) ** 2)

# Problem setup
prob = LpProblem("Minimize_Distance", LpMinimize)
V = set(coordinates.keys())

# Decision variables
x = LpVariable.dicts("x", [(i,j) for i in V for j in V if i != j], cat='Binary')

# Objective function
prob += lpSum(x[i, j] * euclidean_distance(i, j) for i in V for j in V if i != j)

# Constraints ensuring one exit and one entry per group
for group in groups:
    prob += lpSum(x[i, j] for i in group for j in V if j not in group) == 1
    prob += lpSum(x[j, i] for i in group for j in V if j not in group) == 1

# Flow conservation at each node
for i in V:
    prob += lpSum(x[i, j] for j in V if i != j) == lpSum(x[j, i] for j in V if i != j)

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Retrieve solution and calculate total distance
tour = [0]
total_distance = 0
for _ in range(len(V)-1):
    next_city = [j for j in V if j != tour[-1] and x[tour[-1], j].value() == 1]
    if next_city:
        tour.append(next_city[0])
        total_distance += euclidean_distance(tour[-2], next_city[0])

# Ensure tour returns to the depot
if tour[-1] != 0:
    tour.append(0)
    total_distance += euclidean_distance(tour[-2], 0)

# Output the tour and total distance
print("Tour:", tour)
print("Total travel cost:", total_distance)