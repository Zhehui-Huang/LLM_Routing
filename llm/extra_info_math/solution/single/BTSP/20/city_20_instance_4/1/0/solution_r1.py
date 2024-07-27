import numpy as np
from scipy.spatial.distance import euclidean
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

# Define cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
n = len(cities)

# Calculate distance matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean(cities[i], cities[j])

# Integer programming model
model = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)
dt_max = LpVariable("dt_max")

# Objective
model += dt_max

# Constraints
for i in range(n):
    model += lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"Out_{i}"
    model += lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"In_{i}"

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[(i, j)] <= dt_max

# Solve the model
model.solve(PULP_CBC_CMD(msg=True))

# Extract solution
tour = []
current_node = 0
visited = set([current_node])

for _ in range(1, n):
    next_node = None
    for j in range(n):
        if j != current_node and x[(current_node, j)].varValue == 1:
            next_node = j
            break
    if next_node is None:
        print("Failed to find the next node, termination.")
        break
    tour.append(current_node)
    current_node = next_node
    visited.add(current_node)

tour.append(0)  # complete the loop back to the depot

# Calculate tour metrics
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")