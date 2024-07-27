import pulp
import math

# City positions
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups plus the depot
groups = [
    [0],                # Depot (treated as a single-group cluster)
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Functions to calculate Euclidean distance
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create cost matrix
n = len(positions)
costs = { (i, j): euclidean(positions[i], positions[j])
           for i in range(n) for j in range(n) if i != j }

# Define the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat=pulp.LpContinuous)

# Objective function
prob += pulp.lpSum(costs[i, j]*x[i, j] for (i, j) in costs)

# Constraints
# Each cluster must connect to exactly one other cluster
for group in groups:
    prob += pulp.lpSum(x[i,j] for i in group for j in range(n) if j not in group) == 1
    prob += pulp.lpSum(x[j,i] for i in group for j in range(n) if j not in group) == 1

# Subtour elimination
M = len(groups) + n  # an arbitrary large number greater than number of groups and cities
for i in range(n):
    for j in range(n):
        if i != j and (i, j) in costs:
            prob += u[i] - u[j] + M * x[i, j] <= M - 1

# Solve the problem
prob.solve()

# Extracting the tour
if prob.status == pulp.LpStatusOptimal:
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and x[i, j].value() == 1]
    # Extract tour
    tour = [0]  # start at depot
    while len(tour) < len(edges) + 1:
        current = tour[-1]
        next_city = next(j for (i, j) in edges if i == current)
        tour.append(next_city)

    # Calculate total cost
    cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {round(cost, 2)}")
else:
    print("An optimal solution could not be found.")