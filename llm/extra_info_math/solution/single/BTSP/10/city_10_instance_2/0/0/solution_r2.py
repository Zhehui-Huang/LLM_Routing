import pulp
import math
import itertools

# City coordinates
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Number of cities
n = len(coordinates)

# Calculate Euclidean distance
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Initialize problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts('u', (i for i in range(n)), lowBound=0, upBound=n-1, cat=pulp.LpInteger)  # for subtour elimination
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')

# Objective: Minimize the maximum distance between consecutive cities in the tour
prob += M

# Each city is left once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city is entered once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination
for i in range(n):
    for j in range(1, n):  # Condition to exclude depot (u[0] is always 0)
        if i != j:
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Constraint max distance
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(coordinates[i], coordinates[j]) <= M

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Interpret the output
if status == pulp.LpStatusOptimal:
    print("Status:", pulp.LpStatus[prob.status])
    optimization_result = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[(i, j)]) == 1:
                optimization_result.append((i, j))

    path = []
    current_location = 0
    path.append(current_location)
    while len(path) < n:
        next_moves = [j for (i, j) in optimization_result if i == current_location]
        next_location = next_moves[0]
        path.append(next_leg)
        current_location = next_leg

    path.append(0)  # End at the starting point

    total_cost = sum(distance(coordinates[path[i]], coordinates[path[i + 1]]) for i in range(len(path) - 1))
    max_distance = max(distance(coordinates[path[i]], coordinates[path[i + 1]]) for i in range(len(path) - 1))

    print("Optimal tour: ", path)
    print("Total travel cost: ", total_cost)
    print("Maximum distance between consecutive cities: ", max_distance)

else:
    print("The problem does not have an optimal solution.")