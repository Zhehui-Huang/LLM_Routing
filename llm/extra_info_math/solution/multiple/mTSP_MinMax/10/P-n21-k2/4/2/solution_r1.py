import numpy as np
import pulp
from scipy.spatial.distance import cdist

def solve_mTSP(num_robots, coordinates):
    n = len(coordinates) - 1  # number of nodes excluding the depot
    depot = 0
    points = list(range(1, n+1))

    # Calculate Euclidean distance matrix
    distance_matrix = cdist(coordinates, coordinates)

    # Problem
    problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

    # Variables
    x = {(i, j, k): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}_{k}")
         for k in range(num_robots) for i in range(n+1) for j in range(n+1) if i != j}
    u = {i: pulp.LpVariable(cat=pulp.LpContinuous, lowBound=0, name=f"u_{i}") for i in range(1, n+1)}
    
    # Objective: Minimize the maximum distance among all robots
    maximum_distance = pulp.LpVariable("maximum_distance")
    problem += maximum_distance

    # Constraints
    # Each city visited exactly once
    for j in points:
        problem += sum(x[i, j, k] for k in range(num_robots) for i in points if i != j) == 1
    
    # Leave and enter each city once per robot
    for k in range(num_robots):
        for j in points:
            problem += sum(x[i, j, k] for i in range(n+1) if i != j) == sum(x[j, i, k] for i in range(n+1) if i != j)
            
    # Each robot leaves the depot
    for k in range(num_robots):
        problem += sum(x[depot, j, k] for j in points) == 1
        problem += sum(x[j, depot, k] for j in points) == 1

    # Set distances to be below maximum_distance for each robot
    for k in range(num_robots):
        for i in range(n+1):
            for j in range(n+1):
                if i != j:
                    problem += x[i, j, k] * distance_matrix[i][j] <= maximum_distance

    # Subtour elimination
    for k in range(num_robots):
        for i in points:
            for j in points:
                if i != j:
                    problem += u[i] - u[j] + n * x[i, j, k] <= n-1

    # Solve the problem
    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    # Collect the results
    routes = {k: [] for k in range(num_robots)}
    costs = {k: 0 for k in range(num_robots)}

    for k in range(num_robots):
        # Find the route starting from the depot
        current_location = depot
        while True:
            next_location = next(j for i, j, kk in x if i == current_location and kk == k and pulp.value(x[i, j, k]) == 1)
            costs[k] += distance_matrix[current_location][next_location]
            routes[k].append(next_location)
            if next_location == depot:
                break
            current_temp = current_location
            current_location = next_location
            if current_temp == 0:
                break

    max_cost = max(costs.values())
    return routes, costs, max_cost

# Solve the TSP problem for the given data
routes, costs, max_cost = solve_mTSP(num_robots, coordinates)

for k in routes:
    print(f"Robot {k} Tour: {[0] + routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Maximum Travel Cost: {max_cost}")