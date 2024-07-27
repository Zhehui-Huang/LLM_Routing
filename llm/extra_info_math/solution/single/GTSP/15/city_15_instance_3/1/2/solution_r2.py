import pulp
import math

# Define the cities coordinates and groups
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Helper function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Building the cost matrix
costs = {(i, j): euclidean commitment_distance_ distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the variables
x = {(i, j): pulp.LpVariable(name=f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective Function
model += pulp.lpSum(x[i, j] * costs[i, j] for i in cities for j in cities if i != j)

# Constraints
# Select one city from each group excluding the depot
for group in groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in cities if i != j) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if i != j) == 1

# Connectivity constraints
for k in cities:
    if k != 0:
        model += pulp.lpSum(x[i, k] for i in cities if i != k and (i, k) in x) == pulp.lpSum(x[k, j] for j in cities if k != j and (k, j) in x)

# Start and end at depot
model += pulp.lpSum(x[0, j] for j in cities if j != 0) == 1
model += pulp.lpSum(x[i, 0] for i in cities if i != 0) == 1

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    print("Solution found!")
    path = [0]
    while True:
        for k in cities:
            if x[path[-1], k].varValue > 0.5:
                path.append(k)
                break
        if path[-1] == 0:
            break
    total_cost = pulp.value(model.objective)
    print("Tour:", path)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")