import numpy as np
from scipy.spatial.distance import euclidean
import pulp

# --- Problem Definition ---

# Coordinates of cities including depot
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demand at each city
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Number of robots and their loading capacities
num_robots = 8
robot_capacity = 40

# Distance matrix computation
n = len(coords)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean(coords[i], coords[j])

# --- PuLP Model Setup ---

# Initialize the problem
problem = pulp.LpProblem("Vehicle_Routing_Problem", pulp.LpMinimize)

# Variables: x[i, j, k] = 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(num_robots) if i != j), cat="Binary")

# Objective: Minimize the total travel distance
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for k in range(num_robots) for i in range(n) for j in range(n) if i != j)

# Constraints:

# Ensure each city (except depot) is visited exactly once
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(num_robots) if i != j) == 1

# Enforcing capacity
for k in range(num_robots):
    problem += pulp.lpSum(demands[j] * x[i, j, k] for i in range(n) for j in range(1, n) if i != j) <= robot_capacity

# Departure and return to depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1  # leave depot
    problem += pulp.lp_sum(x[j, 0, k] for j in range(1, n)) == 1  # return to depot

# Load conservation (continuity of the route)
for j in range(1, n):
    for k in range(num_robots):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Solve the problem
problem.solve()

# Display the solution
total_cost = 0
routes = []

for k in range(num_robots):
    tour = []
    for i in range(n):
        if any(pulp.value(x[i, j, k]) == 1 for j in range(n) if i != j):
            tour = [0] + [j for j in range(n) if pulp.value(x[0, j, k]) == 1]
            current_city = tour[-1]
            while current_city != 0:
                next_city = next(j for j in range(n) if pulp.value(x[current_city, j, k]) == 1)
                tour.append(next_city)
                current_city = next_city

    if len(tour) > 1:
        routes.append(tour)
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost += cost
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {float(cost)}")

print("Overall Total Travel Cost:", float(total_cost))