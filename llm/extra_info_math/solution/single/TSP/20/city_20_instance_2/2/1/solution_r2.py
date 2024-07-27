import pulp
import math
from itertools import product

# Define the coordinates of all cities including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including the depot
n = len(coordinates)

# Calculate Euclidean distance between two points
def distance(i, j):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[j]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Create an LP minimization problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create variables x[i, j] for each pair i != j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function: Minimize the total travelling distance
model += pulp.lpSum(distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city must be left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour Elimination Constraints
for S in range(2, n):
    for subset in combinations(range(1, n), S):  # Creating subset of nodes
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Check if a feasible solution is found
if model.status == pulp.LpStatusOptimal:
    # Extracting tour
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    tour = [0]  # start from depot
    while len(edges) > 0:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                edges.remove((i, j))
                break
    tour.append(0)  # return to depot

    # Calculate tour cost
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")