import math
from pulp import *

# City coordinates (index: city id, value: (x, y))
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

n = len(coords)

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:  # No self-loops
            cost_matrix[(i, j)] = euclidean_distance(coords[i], coords[j])
        else:
            cost_matrix[(i, j)] = 0

# Problem setup
prob = LpProblem("TSP", LpMinimize)

# Variables: x_ij
x = LpVariable.dicts("x", (range(n), range(n)), 0, 1, LpBinary)

# Objective function
prob += lpSum(x[i][j] * cost_matrix[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour Elimination using MTZ constraints
u = LpVariable.dicts("u", range(n), 0, n - 1)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i][j] <= n - 1, f"MTZ_{i}_{j}"

# Solving the problem
prob.solve()

# Extracting the solution
tour = []
current_city = 0
count = 0
while count < n:
    for j in range(n):
        if x[current_city][j].varValue == 1:
            tour.append(j)
            current_city = j
            count += 1
            break

# Including return to depot
tour.append(0)

# Calculate the total cost
total_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")