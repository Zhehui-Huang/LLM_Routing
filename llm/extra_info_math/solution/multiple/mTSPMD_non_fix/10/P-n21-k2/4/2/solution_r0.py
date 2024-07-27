import numpy as np
import cvxpy as cp
import math

# Define the city coordinates (including depots)
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

n = len(city_coordinates)  # Total number of cities
depots = 2
depot_list = [0, 1]
num_robots = 2

# Calculate the Euclidean distance between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# CVXPY formulation
x = cp.Variable((n, n), boolean=True)
u = cp.Variable(n, integer=True)

# Objective: Minimize total distance traveled
total_distance = cp.sum(cp.multiply(distances, x))

constraints = []
# Exactly two robots leave the depots
for depot in depot_list:
    constraints.append(cp.sum(x[depot, :]) == num_robots)

# Every city is visited exactly once
for j in range(depots, n):
    constraints.append(cp.sum(x[:, j]) == 1)

# Continuity constraints to eliminate subtours
for i in range(depots, n):
    for j in range(depots, n):
        if i != j:
            constraints.append(u[i] - u[j] + n * x[i, j] <= n - 1)

# Each city leads to exactly another one (continuity of tour)
for i in range(depots, n):
    constraints.append(cp.sum(x[i, :]) == 1)

# Robots do not need to return to depot
for i in range(depots, n):
    constraints.append(x[i, depot_list[0]] == 0)
    constraints.append(x[i, depot_list[1]] == 0)

# Solving the problem
problem = cp.Problem(cp.Minimize(total_distance), constraints)
problem.solve(solver=cp.GUROBI)

# Extract the solution
solution = np.round(x.value).astype(int)

# Printing the tours for each robot
def extract_tours(solution, start_node):
    visited = set()
    tour = [start_node]
    current = start_node
    while True:
        next_city = np.where(solution[current, :] == 1)[0]
        if len(next_city) == 0:
            break
        next_city = next_city[0]
        if next_city in visited:
            break
        visited.add(next_city)
        tour.append(next_city)
        current = next_city
    return tour

# Compute and display results
tours = [extract_tours(solution, d) for d in depot_list]
tour_costs = [sum(distances[tours[i][j], tours[i][j + 1]] for j in range(len(tours[i]) - 1)) for i in range(len(tours))]

overall_cost = sum(tour_costs)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")