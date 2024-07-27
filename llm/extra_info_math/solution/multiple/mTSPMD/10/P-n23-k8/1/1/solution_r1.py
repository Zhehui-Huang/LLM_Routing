import numpy as np
from math import sqrt
from mip import Model, xsum, minimize, BINARY

# City Indices and Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_cities = len(coordinates)
num_robots = 8

# Distance matrix calculation
dist_matrix = [[sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
                for j in range(num_cities)] for i in range(num_cities)]

# Binary variables indicating if node j is visited after node i by robot k
model = Model()
x = [[[model.add_var(var_type=BINARY) for k in range(num_robots)] for j in range(num_cities)] for i in range(num_cities)]

# Definition of each depot's robot tour
Z = [model.add_var(var_type=BINARY) for j in range(num_cities)]

# Objective function
model.objective = minimize(xsum(dist_matrix[i][j] * x[i][j][k]
                                for k in range(num_robots)
                                for i in range(num_cities)
                                for j in range(num_cities)))

# Constraints
for k in range(num_robots):
    model += xsum(x[k][j][k] for j in range(num_cities) if j != k) == 1  # exactly one edge leaving each depot
    model += xsum(x[j][k][k] for j in range(num_cities) if j != k) == 1  # exactly one edge arriving at each depot

for j in range(num_cities):
    if j not in range(num_robots):  # each city must be visited exactly once (hence excluding depots themselves)
        model += xsum(x[i][j][k] for i in range(num_cities) for k in range(num_robots)) == 1
        model += xsum(x[j][i][k] for i in range(num_cities) for k in range(num_robots)) == 1

# Eliminate subtours
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                model += xsum(x[i][j][k] for j in range(num_cities)) - \
                         xsum(x[j][i][k] for j in range(num_cities)) == 0

# Solve the model
model.optimize()

# Output tour for each robot
for k in range(num_robots):
    tour = [k]
    next_city = k
    while True:
        next_city = [j for j in range(num_cities) if x[next_city][j][k].x >= 0.99 and j not in tour][0]
        tour.append(next_city)
        if next_city == k:
            break
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour();

# Output the overall cost:
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for k in range(num_robots) for i in range(len(tour)-1))
print("Overall Total Travel Cost:", total_cost)