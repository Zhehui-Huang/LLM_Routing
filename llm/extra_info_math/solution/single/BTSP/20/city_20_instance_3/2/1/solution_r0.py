import numpy as np
from mip import Model, xsum, minimize, BINARY

# Define coordinates of the cities
coordinates = np.array([
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
])

# Calculate distances between each pair of cities
n = len(coordinates)
dist = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i, j] = np.linalg.norm(coordinates[i] - coordinates[j])

# Create the optimization model
model = Model()

# Create variables: x[i, j] = 1 if the path goes from city i to city j, 0 otherwise
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
max_dist = model.add_var()

# Objective: minimize the max distance between consecutive cities
model.objective = minimize(max_dist)

# Constraints:
# Each city must have exactly one outgoing connection
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1

# Each city must have exactly one incoming connection
for j in range(n):
    model += xsum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination constraints
for I in range(1, n-1):
    for S in combinations(range(1,n), I):
        model += xsum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Max distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += dist[i][j] * x[i][j] <= max_dist

# Solve the model
status = model.optimize()

if status == model.OPTIMAL:
    # Extract the tour
    path = []
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                path.append((i, j))
                
    # Construct the tour from the path
    tour = [0]
    current_city = 0
    while len(tour) < n:
        for i, j in path:
            if i == current_city:
                tour.append(j)
                current_city = j
                break

    tour.append(0)  # return to the depot

    # Calculate total travel cost and maximum distance
    total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Optimal solution not found.")