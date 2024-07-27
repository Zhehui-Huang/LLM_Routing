import pulp
import math

# Coordinates of the depot and each city
coordinates = [
    (30, 56),  # Depot
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16),
    (4, 43), (53, 76), (19, 72)
]

# City groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Function to calculate Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distances matrix
distances = [[euclidean_index(i, j) for j in range(20)] for i in range(20)]

# Initialize LP problem
prob = pulp.LpProblem("MinimizeRouteCost", pulp.LpMinimize)

# Variables: x_ij = 1 if path between i and j is selected
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(20) for j in range(20) if i != j}

# Objective: Minimize travel cost
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(20) for j in range(20) if i != j)

# Each group must be connected to and from the depot
for group in groups:
    prob += pulp.lpSum(x[0, j] for j in group) == 1
    prob += pulp.lpSum(x[j, 0] for j in group) == 1

# Flow conservation to avoid sub-tours
for k in range(1, 20):
    prob += pulp.lpSum(x[i, k] for i in range(20) if i != k) == pulp.lpSum(x[k, j] for j in range(20) if j != k)

# Solve the LP
prob.solve()

# Retrieve the solution
path = [0]  # start at the depot
while len(path) < len(groups) + 1:
    last_city = path[-1]
    next_city = next(i for i in range(20) if pulp.value(x[last_city, i]) == 1.0)
    path.append(next_city)

# Close the tour by returning to the depot
path.append(0)

# Calculate total travel cost
total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))

# Output the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost}")