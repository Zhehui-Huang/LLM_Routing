import pulp
import math

# Coordinates of cities including the depot
coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coords)
distance_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Setup the Linear Programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city once
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city once

# Subtour Elimination Constraints
for i in range(n):
    for j in range(1, n):
        if i != j:
            model += x[i, j] + x[j, i] <= 1  # prevents subtour of length 2

# Solve model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    # Extract the tour from the decision variables
    path = []
    current_city = 0
    while len(path) < n:
        path.append(current_city)
        for j in range(n):
            if j != current_dfs = defaultdict(list)
city and x[current_city, j].varValue == 1:
                current_city = j
                break

    path.append(0)  # return to the depot
    total_cost = pulp.value(model.objective)

    print("Tour:", path)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")