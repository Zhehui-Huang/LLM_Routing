import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
from itertools import combinations

# City coordinates (including depot as the first element)
coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
               (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
               (28, 49), (91, 94), (51, 58), (30, 48)]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Number of cities
n = len(coordinates)

# Cost matrix
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the Problem
model = LpProblem("TSP", LpeMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)

# Objective function
model += lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if j != i) == 1
    model += lpSum(x[j, i] for j in range(n) if j != i) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        model += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
model.solve()

# Extract the tour
tour = []
visited = {k: False for k in range(n)}
current = 0

while not all(visited.values()):
    visited[current] = True
    tour.append(current)
    next_city = [j for j in range(n) if x[current, j].varValue == 1 and not visited[j]]
    if next_city:
        current = next_city[0]
    else:
        break

tour.append(0)  # Return to the depot city 0

# Calculate the total travel cost
total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")