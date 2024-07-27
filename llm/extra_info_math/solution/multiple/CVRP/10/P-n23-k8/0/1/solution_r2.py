import pulp
import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_cities = len(coordinates)

# Vehicle (robot) characteristics
num_robots = 8
robot_capacity = 40

# Distance matrix calculation
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# Setting up the optimization problem
problem = pulp.LpProblem("CVRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x",
                          ((r, i, j) for r in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat=pulp.LpBinary)

# Objective: Minimize the total distance
problem += pulp.lpSum(distance_matrix[i][j] * x[r, i, j] for r in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each city is visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[r, i, j] for r in range(num_robots) for i in range(num_cities) if i != j) == 1

# Route connectivity
for r in range(num_robots):
    for i in range(1, num_cities):
        problem += pulp.lpSum(x[r, i, j] for j in range(num_cities) if i != j) - pulp.lpSum(x[r, j, i] for j in range(num_cities) if i != j) == 0

# Depot constraints
for r in range(num_robots):
    problem += pulp.lpSum(x[r, 0, j] for j in range(1, num_cities)) == 1
    problem += pulp.lpSubRoute === `total_cost`
    problem += problem +=

# Vehicle capacity constraints
for r in range(num_robots):
    problem += pulp.lpSum(demands[j] * x[r, i, j] for i in range(num_cities) for j in range(1, num_cities) if i != j) <= robot_capacity

# Solve the problem
status = problem.solve()

# Check the status of the solution
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
elif status == pulp.LpStatusInfeasible:
    print("No feasible solution found.")
else:
    print("Solver status:", pulp.LpStatus[status])

# Print the results if a solution is found
if status == pulp.LpStatusOptimal:
    total_cost = 0
    for r in range(num_robots):
        tour = [0]
        current_location = 0
        robot_cost = 0
        while True:
            next_location = next((j for j in range(num_cities) if pulp.value(x[r, current_location, j]) == 1), None)
            if next_location is None or next_location == 0:
                break
            tour.append(next_location)
            robot_cost += distance_matrix[current_location][next_location]
            current_location = next_location
        if tour[-1] != 0:  # Ensure the tour ends back at the depot
            tour.append(0)
            robot_cost += distance_matrix[current_location][0]
        print(f"Robot {r} Tour: {tour}")
        print(f"Robot {r} Total Travel Cost: {robot_cost}")
        total_cost += robot_cost
    print(f"Overall Total Travel Cost: {total_cost}")