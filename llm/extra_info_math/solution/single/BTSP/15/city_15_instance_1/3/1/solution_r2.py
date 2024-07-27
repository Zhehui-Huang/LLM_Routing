import numpy as np
import pulp

# Define the cities' coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(coordinates)

# Compute the Euclidean distance between each pair of cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] 
    for i in range(n)
]

# Create the PuLP model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f'x_{i}_{j}', cat=pulp.LpBinary) for i in range(n) for j in range(n)}
u = {i: pulp.LpVariable(f'u_{i}', lowBound=0, upBound=n-1, cat=pulp.LpInteger) for i in range(n)} # for subtour constraints
M = pulp.LpVariable("Max_distance", lowBound=0, cat=pulp.LpContinuous)

# Objective function
model += M

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave each city once
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter each city once

# Subtour elimination and maximum distance constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[(i, j)] <= n-2
        model += x[(i, j)] * distance_matrix[i][j] <= M

# Solve the model
model.solve()

# Retrieve the solution
tour = []
current = 0
for _ in range(n):
    for next_ in range(n):
        if pulp.value(x[(current, next_)]) == 1:
            tour.append(current)
            current = next_
            break
tour.append(0) # come back to the depot

# Calculate the metrics
max_edge_length = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
total_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_edge_length}")