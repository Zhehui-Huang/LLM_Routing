import cvxpy as cp
import numpy as np
import math

# Define the coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_cities = len(coordinates)
num_robots = 8
vehicle_capacity = 35

# Calculate distance matrix (Euclidean distances)
cost_matrix = np.array([
    [math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
     for j in range(num_cities)] for i in range(num_cities)])

x = cp.Variable((num_robots, num_cities, num_cities), boolean=True)

# Objective
objective = cp.Minimize(cp.sum(cp.multiply(cost_matrix, cp.sum(x, axis=0))))

# Constraints
constraints = []

# Every city must be visited exactly once
for j in range(1, num_cities):
    constraints.append(cp.sum(x[:, j, :]) == 1)

# Departure and arrival at the depot for each robot
for r in range(num_robots):
    constraints.append(cp.sum(x[r, 0, :]) == 1)
    constraints.append(cp.sum(x[r, :, 0]) == 1)

# Flow conservation for all cities for each robot
for r in range(num_robots):
    for j in range(1, num_cities):
        constraints.append(cp.sum(x[r, :, j]) == cp.sum(x[r, j, :]))

# Capacity constraints
for r in range(num_robots):
    constraints.append(cp.sum(cp.multiply(demands, cp.sum(x[r, :, :], axis=0))) <= vehicle_capacity)

# Model solve
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.GLPK_MI)

# Extracting and displaying the result
if problem.status == cp.OPTIMAL:
    overall_total_cost = 0
    for r in range(num_robots):
        tour = [0]
        current_location = 0
        total_cost = 0
        while True:
            next_city = None
            for j in range(num_cities):
                if x.value[r, current_location, j] > 0.5:
                    next_city = j
                    break
                    
            if next_city is None or next_city == 0:
                break
            
            tour.append(next_city)
            total_cost += cost_matrix[current_location, next_city]
            current_location = next_city
        
        if tour[-1] != 0:
            tour.append(0)  # Ensure to return to depot
            total_cost += cost_matrix[current_location, 0]
        
        overall_total_cost += total_cat
        print(f"Robot {r} Tour: {tour}")
        print(f"Robot {r} Total Travel Cost: {total_cost:.2f}")
    
    print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")
else:
    print("No optimal solution found.")