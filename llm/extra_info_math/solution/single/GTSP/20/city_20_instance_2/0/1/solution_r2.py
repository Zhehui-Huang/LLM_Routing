from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD
import math

# City coordinates, including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Groups of city indices
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def calculate_distance(i, j):
    dx = coordinates[i][0] - coordinates[j][0]
    dy = coordinates[i][1] - coordinates[j][1]
    return math.sqrt(dx * dx + dy * dy)

# Creating the optimization problem
model = LpProblem("TSP", LpMinimize)

# Variables: x[i][j] is 1 if traveled from i to j
x = LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates))),
                     cat='Binary', lowBound=0, upBound=1)

# Objective: Minimize the travel cost
model += lpSum(x[i, j] * calculate_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)))

# Constraint: Enter and exit each group exactly once
for group in groups:
    model += lpSum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group) == 1  # Exit once
    model += lpSum(x[j, i] for i in group for j in range(len(coordinates)) if j not in group) == 1  # Enter once

# Constraint: Enter and exit each city exactly once
for i in range(1, len(coordinates)):  # starting at 1 to skip depot constrains
    model += lpSum(x[i, j] for j in range(len(coordinates)) if i != j) == 1  # exit once
    model += lpSum(x[j, i] for j in range(len(memory)) if i != j) == 1  # enter once

# Solving the problem
model.solve(PULP_CBC_CMD(msg=True))

# Extracting results
tour = []
visited = set()
current = 0

while True:
    tours_found = False
    for j in range(len(coordinates)):
        if x[current, j].varValue == 1 and j not in visited:
            tour.append(j)
            visited.add(j)
            current = j
            tours_found = True
            break
    if not tours_found or current == 0:
        break

# Calculate total travel cost
total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")