import numpy as np
from math import sqrt
from mip import Model, xsum, minimize, BINARY, INTEGER

# City and Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Parameters
num_cities = len(coordinates)
dist_matrix = [
    [sqrt((coordinates[i][0] - coordinates[j][0])**2 + 
          (coordinates[i][1] - coordinates[j][1])**2) for j in range(num_cities)] 
    for i in range(num_cities)
]

# MIP model setup
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(num_robots)] for j in range(num_cities)] for i in range(num_cities)]
u = [model.add_var(var_type=INTEGER, lb=0) for i in range(num_cities)]

# Objective: Minimize total travel cost
model.objective = minimize(xsum(dist_matrix[i][j] * x[i][j][k] for k in range(num_robots) for i in range(num_cities) for j in range(num_cities)))

# Constraints
for k in range(num_robots):
    model += xsum(x[k][j][k] for j in range(num_cities) if j != k) == 1  # Departure from depot
    model += xsum(x[j][k][k] for j in range(num_cities) if j != k) == 1  # Arrival to depot

for j in range(num_cities):
    if j not in range(num_robots):  # Exclude depots themselves
        model += xsum(x[i][j][k] for k in range(num_robots) for i in range(num_cities)) == 1  # Enter city once
        model += xsum(x[j][i][k] for k in range(num_robots) for i in range(num_cities)) == 1  # Leave city once

# Sub-tour elimination
for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                model += u[i] - u[j] + (num_cities - 1) * x[i][j][k] < num_cities - 1

# Solve the model
model.optimize()

tours = []
total_cost = 0

for k in range(num_robots):
    tour = [k]
    while True:
        next_city = [j for j in range(num_cities) if x[tour[-1]][j][k].x > 0.99 and j not in tour]
        if not next_city:
            break
        tour.append(next_city[0])
        if next_city[0] == k:
            break
    tours.append(tour)
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print("Overall Total Travel Cost:", total_cost)