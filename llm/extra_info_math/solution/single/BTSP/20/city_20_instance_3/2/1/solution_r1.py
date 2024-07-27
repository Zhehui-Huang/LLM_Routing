import numpy as np
from mip import Model, xsum, minimize, BINARY
from itertools import permutations

# Define coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

n = len(coordinates)  # Total number of cities

# Calculate Euclidean distance between each pair of cities
dist = [[None]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i][j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j])) 
        else:
            dist[i][j] = 0

# Creating a Mixed Integer Linear Programming Model
model = Model()

# Variable x[i, j]: 1 if route takes the path from city i to city j, 0 otherwise.
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# Variable for the maximum distance in the route
max_d = model.add_var()

# Objective: Minimize the maximum distance traveled between any two consecutive cities
model.objective = minimize(max_d)

# Constraints
# Each city is arrived at from exactly one other city
for j in range(n):
    model += xsum(x[i][j] for i in range(n) if i != j) == 1

# Each city is departed to exactly one other city
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1

# Subtour elimination via Miller-Tucker-Zemlin (MTZ) formulation
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n-1

# Constraint to keep the maximum distance to the minimum found
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i][j] * dist[i][j] <= max_d

# Solve the model
model.optimize()

# Extract the tour
tour = []
current = 0
for _ in range(n):
    tour.append(current)
    next_city = [j for j in range(n) if x[current][j].x >= 0.99 and current != j][0]
    current = next_city
tour.append(0)  # to return to the starting city 

# Calculate the total cost and maximum leg distance
total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))