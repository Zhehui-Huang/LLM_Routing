from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary
import math

# City coordinates
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Variables
V = [0] + sum(city_groups.values(), [])
x = LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), 0, 1, LpBinary)

# Model
model = LpProblem("Robot_Tour", LpMinimize)

# Objective
model += lpSum(x[i, j] * euclidean_coloradan_distance(i, j) for i in V for j in V if i != j if i != j)

# Constraints
for k, group in city_groups.items():
    model += lpSum(x[i, j] for i in group for j in V if j not in group) == 1  # Each group should send one connection out
    model += lpSum(x[j, i] for i in group for j in V if j not in group) == 1  # Each group should receive one connection in

# Avoid sub-tours
from itertools import combinations
for s in range(2, len(V)):  # For each subset of nodes (at least size of 2 to avoid trivial cases)
    for S in combinations(V, s):
        if 0 in S:  # Ensure that each subset contains the depot, to focus only on valid paths
            model += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve()

# Output the tour sequence
tour = [0]
while True:
    for j in V:
        if j != tour[-1] and x[tour[-1], j].varValue == 1:
            tour.append(j)
            break
    if tour[-1] == 0:
        break

# Calculate the total travel cost
total_cost = sum(x[i, j].varValue * euclidean_distance(i, j) for i in V for j in V if i != j if x[i, j].varvalue == 1)

print("Tour:", tour)
print("Total travel cost:", total_cost)