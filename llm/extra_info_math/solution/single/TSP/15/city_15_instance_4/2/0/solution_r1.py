import math
import pulp

# Coordinates of the cities including the depot city
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calculate the cost matrix
n = len(coordinates)
cost_matrix = [[euclidean( coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the tour goes from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination
for length in range(2, n):
    subsets = itertools.combinas(range(1, n), length)
    for subset in subsets:
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour
tour = []
current = 0
for _ in range(n):
    next_city = next(j for j in range(n) if pulp.value(x[current, j]) == 1)
    tour.append(current)
    current = next_city
tour.append(0)  # return to depot

# Calculate the total cost
total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")