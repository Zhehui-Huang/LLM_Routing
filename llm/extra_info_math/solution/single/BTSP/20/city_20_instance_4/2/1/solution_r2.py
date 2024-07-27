import math
from itertools import product
from mip import Model, xsum, minimize, BINARY, INTEGER

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

n = len(coordinates)  # Total number of cities

# Distance matrix calculation
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Creating the model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER, lb=1, ub=n) for i in range(n)]
z = model.add_var()

# Objective: minimize the maximum distance between consecutive cities
model.objective = minimize(z)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination (SEC)
for (i, j) in product(range(1, n), repeat=2):
    if i != j:
        model += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2

# Link z to the maximum distance in a tour
for (i, j) in product(range(n), repeat=2):
    if i != j:
        model += distances[i][j] * x[i][j] <= z

# Solving the model
model.optimize()

# Retrieve the tour from decision variables
tour = [0]  # starting point
current = 0
for _ in range(n-1):  # exclude the return to the starting city in this loop
    next_city = next(j for j in range(n) if x[current][j].x >= 0.99)
    tour.append(next_city)
    current = next_city

# Calculate travel details
total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(-1, n-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(-1, n-1))

# Append the starting city to complete the loop in the output
tour.append(0)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {z.x}")