import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value

def euclidean_distance(p1, p2):
    """ Compute the Euclidean distance between two points """
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates for the depot and cities
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

n = len(coordinates)  # Number of cities including the depot

# Calculate cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Decision variables, x_ij = 1 if tour goes from city i to j, 0 otherwise
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Subject to the constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city only once
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
from itertools import combinations
for k in range(2, n):
    for S in combinations(range(1, n), k):
        problem += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Extract tour from decision variables
path = []
visited = {0}
current = 0
while len(path) < n:
    path.append(current)
    for j in range(n):
        if j != current and x[current, j].varValue == 1:
            next_city = j
            break
    visited.add(next_city)
    current = next_city

path.append(0)  # Return to depot

# Calculate the total cost of the tour
total_cost = sum(cost[path[i]][path[i + 1]] for i in range(len(path) - 1))

# Output the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")