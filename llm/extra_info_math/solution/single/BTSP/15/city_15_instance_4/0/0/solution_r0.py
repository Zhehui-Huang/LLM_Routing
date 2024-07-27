import numpy as np
from scipy.spatial.distance import euclidean
from pulp import *

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

n = len(cities)

# Calculate the distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinity cost for traveling to the same city

# Create the optimization model
model = LpProblem("Min_Max_TSP", LpMinimize)
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')
b = LpVariable.dicts("b", [i for i in range(n)], lowBound=0, cat='Integer')

# Objective function: minimize the maximum distance
U = LpVariable("U", lowBound=0)
model += U

# Constraints
for j in range(1, n):
    model += lpSum([x[i, j] for i in range(n) if i != j]) == 1

for i in range(1, n):
    model += lpSum([x[i, j] for j in range(n) if i != j]) == 1

# Subtour elimination and U definition
for i in range(n):
    for j in range(1, n):
        if i != j:
            model += U >= distance_matrix[i][j] * x[i, j]
            model += b[i] - b[j] + (n) * x[i, j] <= n - 1

model += lpSum([x[0, j] for j in range(1, n)]) == 1
model += lpSum([x[i, 0] for i in range(1, n)]) == 1

# Solving the problem
status = model.solve()

# Extract the solution
tour = []
if LpStatus[model.status] == 'Optimal':
    active_edges = [(i, j) for i in range(n) for j in range(n) if x[i, j].varValue == 1]
    current_location = 0
    while len(active_edges) > 0:
        next_moves = [j for i, j in active_edges if i == current_location]
        next_move = next_moves[0]
        tour.append(current_location)
        current_location = next_move
        active_edges = [(i, j) for i, j in active_edges if i != tour[-1]]
    tour.append(0)  # end at the starting point

    # Calculate the total cost and maximum edge cost
    max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost = sum(distance_list[i][tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("An optimal tour could not be found.")