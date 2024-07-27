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
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Building the cost matrix
N = len(cities)
costs = {}
for i in cities:
    for j in cities:
        if i != j:
            costs[(i, j)] = euclidean_distance(cities[i], cities[j])

# Define the problem
model = pulp.LpProblem("min_cost_tour", pulp.LpMinimize)

# Define the variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 0, 1, pulp.LpBinary)

# Objective function
model += pulp.lpSum(costs[i, j] * x[i, j] for i in cities for j in cities if i != j and (i, j) in costs)

# Constraints
# Each group must connect exactly once to and from the rest of the nodes
for group in groups.values():
    model.addConstraint(pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1)
    model.addConstraint(pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1)

# Flow conservation constraints
for k in cities:
    model += pulp.lpSum(x[i, k] for i in cities if i != k and (i, k) in x) - pulp.lpSum(x[k, j] for j in cities if j != k and (k, j) in x) == 0

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))
if status == pulp.LpStatusOptimal:
    print("Solution found.")
    # Extracting the tour
    tour = [0]
    next_city = 0
    for _ in range(len(cities)):
        next_city = next((j for j in cities if pulp.value(x[next_city, j]) == 1 and j != next_city), None)
        if next_city is None or next_city == 0:
            break
        tour.append(next_city)
    tour.append(0)  # return to the depot
    total_cost = pulp.value(model.objective)
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")