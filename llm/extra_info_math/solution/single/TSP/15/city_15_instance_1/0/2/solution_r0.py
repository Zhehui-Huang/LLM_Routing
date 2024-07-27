import numpy as np
from scipy.spatial.distance import cdist
from gurobipy import Model, GRB, quicksum

# Coordinates of cities including the depot
coordinates = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Calculate distances matrix
distances = cdist(coordinates, coordinates, metric='euclidean')

# Create a model
m = Model("TSP")

# Number of cities
n = distances.shape[0]

# Create variables: x[i, j] = 1 if route goes from i to j
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")

# Set objective: minimize the total travel distance
m.setObjective(quicksum(distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j), GRB.MINIMIZE)

# Add constraints: each city must be left exactly once
m.addConstrs(quicksum(x[i, j] for j in range(n) if i != j) == 1 for i in range(n))

# Add constraints: each city must be entered exactly once
m.addConstrs(quicksum(x[j, i] for j in range(n) if i != j) == 1 for i in range(n))

# Subtour elimination constraints (SEC)
for q in range(2, n):
    for subset in itertools.combinations(range(1, n), q):
        m.addConstr(quicksum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Optimize the model
m.optimize()

# Extract tour order from decision variables and calculate total travel cost
tour = []
visited = [False] * n
current = 0
total_cost = 0

while not visited[current]:
    visited[current] = True
    tour.append(current)
    for j in range(n):
        if x[current, j].X > 0.5 and not visited[j]:  # Large float handling
            total_cost += distances[current, j]
            current = j
            break

tour.append(0)  # Return to depot
total_cost += distances[current, 0]  # Cost to return back to depot

# Output the required result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")