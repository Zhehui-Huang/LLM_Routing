import pulp
import math

# City positions
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Functions to calculate Euclidean distance
def euclidean(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Create cost matrix
n = len(positions)
costs = [[euclidean(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)

# Objective function
prob += pulp.lpSum(costs[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Exactly one edge out of each group
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(n) if j not in group) == 1

# Exactly one edge into each group
for group in groups:
    prob += pulp.lpSum(x[i, j] for j in group for i in range(n) if i not in group) == 1

# Flow conservation
for i in range(1, n):
    prob += pulp.lpSum(x[j, i] for j in range(n) if j != i) == pulp.lpSum(x[i, j] for j in range(n) if j != i)

# Subtour elimination
k = len(groups) + 1  # As it includes depot as separated set
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] + (n - 3) * x[j, i] <= n - 2

# Solve the problem
prob.solve()

# Check if there is an optimal solution
if pulp.LpStatus[prob.status] == "Optimal":
    # Extracting the tour
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and x[i, j].varValue == 1]
    tour = [0]
    while len(tour) < k + 1:
        last = tour[-1]
        next_city = next(j for (i, j) in edges if i == last)
        tour.append(next_city)
        edges = [(i, j) for (i, j) in edges if i != next_city]
    tour.append(0)  # complete the cycle back to the depot

    # Calculate total tour cost
    cost = sum(costs[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {cost}")
else:
    print("An optimal solution could not be found.")