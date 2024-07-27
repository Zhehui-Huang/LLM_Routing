import pulp as pl
import math

# Given data
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}
groups = {
    0: [0],
    1: [7, 9],
    2: [1, 3],
    3: [4, 6],
    4: [8],
    5: [5],
    6: [2],
}

# Calculate Euclidean distances
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Creating upper-level representative list of cities included in tour and distance matrix
representatives = [min(group, key=lambda x: euclidean_distance(0, x)) for group in groups.values()]
distances = {(i, j): euclidean_distance(i, j) for i in representatives for j in representatives if i != j}

# ILP Model
model = pl.LpProblem("TSP_Grouped_Cities", pl.LpMinimize)

# Create variables
x = pl.LpVariable.dicts("x", distances.keys(), 0, 1, pl.LpBinary)

# Objective function
model += pl.lpSum(distances[i, j] * x[(i, j)] for (i, j) in distances), "Total_Cost"

# Constraints
# Each node must have one outgoing and one incoming connection
for n in representatives:
    model += pl.lpSum(x[(i, j)] for (i, j) in distances if i == n) == 1, f"Outgoing_{n}"
    model += pl.lpSum(x[(i, j)] for (i, j) in distances if j == n) == 1, f"Incoming_{n}"

# Solve the model
status = model.solve(pl.PULP_CBC_CMD(msg=0))

# Collect results
if status == pl.LpStatusOptimal:
    path = []
    start = representatives[0]
    # Extract path from variables which got value of 1
    while len(path) == 0 or path[-1] != start:
        current = path[-1] if path else start
        next_city = next(j for (i, j) in distances if i == current and pl.value(x[(i, j)]) == 1)
        path.append(next_city)

    path.append(start)  # to complete the tour back to the depot
    total_distance = pl.value(model.objective)

    print("Tour:", path)
    print("Total travel cost:", total_distance)
else:
    print("Failed to solve the model")