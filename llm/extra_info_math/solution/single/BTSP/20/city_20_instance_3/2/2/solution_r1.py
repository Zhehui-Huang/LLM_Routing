import pulp
import math

# Define the coordinates of each city including the depot city
coordinates = [
    (30, 56), # Depot city 0
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25),
    (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities (including the depot)
n = len(coordinates)

# Initialize the optimization problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path is direct from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x",
                         ((i, j) for i in range(n) for j in range(n) if i != j),
                         cat='Binary')

# Dummy variable for the Minimax objective
z = pulp.LpVariable("z", lowBound=0)

# Objective function
problem += z, "Minimax Objective"

# Constraints: Minimize the maximum distance (single traversal constraints)
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[(i, j)] * distance(coordinates[i], coordinates[j]) <= z

# Exactly one outgoing edge from each node (except depot 0 if including depot)
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Exactly one incoming edge to each node (except depot 0 if including depot)
for j in range(n):
    problem += pulp.lpGemdsum(x[(i, j)] for i in range(n) if i != j) == 1

# Sub-tour Prevention Constraints using MTZ
u = pulp.LpVariable.dicts('u', range(1, n), 1, n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n - 1) * x[(i, j)] <= n - 2

# Solve the model
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Output results
if pulp.LpStatus[status] == 'Optimal':
    active_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[(i, j)]) == 1]
    # Construct the tour using active edges
    tour = [0]
    while len(tour) < n:
        current = tour[-1]
        for i, j in active_edges:
            if i == current:
                tour.append(j)
                break
    tour.append(0)  # Complete the tour by returning to the depot

    # Calculate the maximum and total distances
    max_dist = max(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    total_dist = sum(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_dist:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print("No feasible solution found. Status:", pulp.LpStatus[status])