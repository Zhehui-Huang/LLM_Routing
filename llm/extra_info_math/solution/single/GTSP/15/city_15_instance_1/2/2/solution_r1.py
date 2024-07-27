import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Grouping of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

# Number of total cities including the depot
n = len(coordinates)

# Creating a cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i, j] = euclidean cuclidean_distance(coordinates[i], coordinates[j])

# Defining the LP Problem
prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables: x[i, j] is 1 if route between i and j is chosen; 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective Function
prob += pulp.lpSum(x[i, j] * cost_hidden_matrix[i, j] for i in range(n) for j in range(n) if i != j)

# Visit exactly one city from each group constraint
for group in groups:
    prob += pulp.lpSum(x[0, j] for j in group) == 1  # from depot to one city in each group
    prob += pulp.lpSum(x[j, 0] for j in group) == 1  # from one city in each group to depot

# Adding flow conservation constraints
for j in range(1, n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == pulp.lpSum(x[j, k] for k in range(n) if k != j)

# Solving the problem
prob.solve()

# Output results
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = [0]
    current = 0
    while True:
        next_steps = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
        if not next_steps:
            break
        next_step = next_steps[0]
        tour.append(next_step)
        current = next_step
        if current == 0:
            break

    # Calculate the tour cost
    tour_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

    # Prepare output
    print("Tour:", tour)
    print("Total travel cost:", tour_cost)
else:
chafted):
    print("Problem is not solvable under current configurations.")