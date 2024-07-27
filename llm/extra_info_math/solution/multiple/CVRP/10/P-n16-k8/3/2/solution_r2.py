import cvxpy as cp
import numpy as np
import math

# Definitions of city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Constants
num_cities = len(coordinates)
num_robots = 8
vehicle_capacity = 35

# Distance calculation with Euclidean formula
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cost_matrix = np.array([
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
])

# CVX variables
x = cp.Variable((num_robots, num_cities, num_cities), boolean=True)

# Objective: minimize total travel cost
objective = cp.Minimize(cp.sum(cost_matrix * cp.sum(x, axis=0)))

# Constraints setup
constraints = []

# Each customer is visited exactly once
for j in range(1, num_cities):
    constraints.append(cp.sum(x[:, j, :]) == 1)

# Establish routes for each vehicle
for r in range(num_robots):
    constraints.append(cp.sum(x[r, 0, :]) == 1)
    constraints.append(cp.sum(x[r, :, 0]) == 1)

# Flow conservation
for r in range(num_robots):
    for j in range(num_cities):
        constraints.append(cp.sum(x[r, j, :]) == cp.sum(x[r, :, j]))

# Capacity constraint
for r in range(num_robots):
    constraints.append(cp.sum(cp.multiply(demands, cp.sum(x[r, :, :], axis=0))) <= vehicle_capacity)

# Problem and solution
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.GLPK_MI)

# Pull solution details
overall_total_cost = 0
if x.value is not None:
    for r in range(num_robots):
        tour = [0]
        current_location = 0
        total_cost = 0
        while True:
            found_next = False
            for j in range(1, num_cities):
                if int(x.value[r, current_location, j] + 0.5) == 1:
                    tour.append(j)
                    total_cost += cost_matrix[current_location, j]
                    current_location = j
                    found_next = True
                    break
            if not found_next:
                break
        tour.append(0)
        total_cost += cost_matrix[current_screen, 0]  # Returning to depot
        overall_total_cost += total_cost
        print(f"Robot {r} Tour: {tour}")
        print(f"Robot {r} Total Travel The ovcost: {total_cost:.2f}")

    print(f"Overall Total Cost: {overall_total_cost:.2f}")
else:
    print("Optimal solution was not found.")