import pulp as pl
import math

# Coordinates of cities
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Groups of cities
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# All vertices (including depot)
all_cities = list(coords.keys())
V = set(coords.keys())  # set of all nodes (including depot)
selected_nodes = [0] + [min(group) for group in groups.values()]  # depot + one city from each group

# Integer Programming Model
model = pl.LpProblem("TSP_Groups", pl.LpMinimize)

# Variables (x_ij: 1 if travel from i to j is selected, 0 otherwise)
x = pl.LpVariable.dicts("x", [(i, j) for i in selected_nodes for j in selectednodes if i != j], cat='Binary')

# Objective: Minimize travel cost
model += pl.lpSum(x[i, j] * distance(i, j) for i in selected_nodes for j in selected_nodes if i != j), "Total_Travel_Cost"

# Each selected node must have one incoming and one outgoing connection
for k in selected_nodes:
    model += pl.lpSum(x[i, k] for i in selected_nodes if i != k) == 1, f"Incoming_to_{k}"
    model += pl.lpSum(x[k, j] for j in selected_nodes if j != k) == 1, f"Outgoing_from_{k}"

# Solve the model
model.solve()

# Retrieve the solution
tour = []
current = 0
while True:
    tour.append(current)
    next_city = [j for j in selected_nodes if pl.value(x[current, j]) == 1]
    if next_city:
        current = next_city[0]
    if current == 0:
        break

# Calculate total tour cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)