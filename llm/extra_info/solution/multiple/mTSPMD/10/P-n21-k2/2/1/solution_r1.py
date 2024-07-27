import numpy as user_np
from scipy.spatial.distance import cdist
from mip import Model, xsum, minimize, BINARY

# Coordinates of cities including depots
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
])

num_cities = len(coordinates)

# Euclidean distance matrix
dist_matrix = cdist(coordinates, coordinates)

# Model initialization
model = Model()

# Variables: x[i, j] == 1 if travel from city i to city j
x = [[model.add_var(var_type=BINARY) for j in range(num_cities)] for i in range(num_cities)]

# Objective: minimize the travel distance
model.objective = minimize(xsum(dist_matrix[i][j] * x[i][j] for i in range(num_cities) for j in range(num_cities)))

# Constraints
# Only one exit per city
for i in range(num_cities):
    model += xsum(x[i][j] for j in range(num_cities) if i != j) == 1

# Only one entry per city
for j in range(num_cities):
    model += xsum(x[i][j] for i in range(num_cities) if i != j) == 1

# Subtour elimination (SEC)
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            u = [model.add_var() for i in range(num_cities)]
            model += u[i] - u[j] + num_cities * x[i][j] <= num_cities - 1

# Solve the model
model.optimize()

# Retrieve the tour
tour = []
city = 0
while True:
    next_cities = [j for j in range(num_cities) if x[city][j].x >= 0.99]
    if len(next_cities) == 0:
        break
    next_city = next_cities[0]
    tour.append(city)
    city = next_city
    if city == 0:
        break

tour.append(0)  # return to depot

# Compute cost
tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the final tour and cost
print(f"Tour: {tour}")
print(f"Total Travel Cost: {tour_cost}")