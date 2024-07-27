import numpy as np
import cvxpy as cp
import math

# City coordinates (including depots)
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

n = len(city_coordinates)  # Total number of cities
depots = [0, 1]
num_robots = 1  # Adjusted based on depots

# Euclidean distance calculator
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix initialization
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Variables for CVXPY
x = cp.Variable((n, n), boolean=True)
u = cp.Variable(n, integer=True)

# Define the objective function
objective = cp.Minimize(cp.sum(cp.multiply(distances, x)))

constraints = []

# Every robot leaves the depot
for depot in depots:
    constraints.append(cp.sum(x[depot, :]) == num_robots)

# Ensure each city is connected to exactly one next city
for j in range(n):
    constraints.append(cp.sum(x[:, j]) == 1)
    constraints.append(cp.sum(x[j, :]) == 1)

# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j:
            constraints.append(u[i] - u[j] + n * x[i, j] <= n - 2)

# Problem solving using CVXPY
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.GUROBI, verbose=True)

# Extracting detailed solution
solution = x.value > 0.5  # Getting significant values

# Finding routes from the solution matrix
def retrieve_route(starting_depot):
    route = [starting_depot]
    current = starting_depot

    while True:
        next_stop = np.where(solution[current, :] == 1)[0]
        if len(next_stop) == 0:
            break
        next_city = next_stop[0]
        route.append(next_city)
        current = next_city
        if current in depots:
            break

    return route

# Display the results
tours = [retrieve_route(d) for d in depots]
tour_costs = [sum(distances[tours[i][j], tours[i][j + 1]] for j in range(len(tours[i]) - 1)) for i in range(len(tours))]

print(f"Overall Total Travel Cost: {sum(tour_costs)}")
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")