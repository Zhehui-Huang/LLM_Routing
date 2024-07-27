import numpy as np
from scipy.spatial import distance_matrix
import pulp

# City coordinates
cities = {
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

# Convert to list to ensure ordering and then calculate the distance matrix
coords = [cities[i] for i in range(len(cities))]
distance_mtx = distance_matrix(coords, coords)

# Initialize the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j), cat='Binary')
k = pulp.LpVariable("k", lowBound=0, cat='Continuous')

# Constraints
# Incoming and outgoing flow constraints
for i in range(len(cities)):
    problem.addConstraint(pulp.lpSum(x[j, i] for j in range(len(cities)) if i != j) == 1)
    problem.addConstraint(pulp.lpSum(x[i, j] for j in range(len(cities)) if i != j) == 1)

# Minimax constraint
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            problem.addConstraint(x[i, j] * distance_mtx[i][j] <= k)

# Objective function
problem.setObjective(k)

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(len(cities)), lowBound=1, upBound=len(cities)-1, cat='Continuous')

for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            problem.addConstraint(u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1)

# Solve the problem
status = problem.solve()

# Check if the solution is optimal
if pulp.LpStatus[status] == 'Optimal':
    # Extract the tour using the x variables
    path = []
    cur_node = 0
    while True:
        path.append(cur_node)
        next_nodes = [j for j in range(len(cities)) if j != cur_node and pulp.value(x[cur_node, j]) == 1]
        if not next_nodes:
            break
        cur_node = next_nodes[0]
    path.append(path[0])  # to complete the cycle back to the starting point

    # Calculate the cost and max_distance
    total_cost = sum(distance_mtx[path[i]][path[i + 1]] for i in range(len(path) - 1))
    max_distance = max(distance_mtx[path[i]][path[i + 1]] for i in range(len(path) - 1))

    print("Tour:", path)
    print("Total travel cost: {:.2f}".format(total_cost))
    print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))
else:
    print("Failed to find an optimal solution.")