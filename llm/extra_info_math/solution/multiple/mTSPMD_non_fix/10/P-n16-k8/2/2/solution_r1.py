import math
import pulp

# Coordinates for the cities (including depots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Euclidean distance calculation
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate cost matrix
num_cities = len(coordinates)
cost_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Set up problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities)), cat='Binary')

# Objective function
problem += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities)), "Total Tour Cost"

# Constraints
# Each city is visited by exactly one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j] for i in range(num_cities)) == 1

# Number of robots entering and leaving the starting depot (0)
number_of_robots = 8
problem += pulp.lpSum(x[0, j] for j in range(1, num_cities)) == number_of_robots
problem += pulp.lpSum(x[i, 0] for i in range(1, num_cities)) == number_of_robots

# Ensuring a valid tour by connecting each node
for i in range(1, num_cities):
    problem += pulp.lpSum(x[j, i] for j in range(num_cities)) == pulp.lpSum(x[i, k] for k in range(num_cities))

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Output results
if status == 1:
    print("Optimal solution found.\n")
    total_cost = 0.0
    for r in range(num_cities):
        tour = []
        current_location = r
        if pulp.value(x[r, 0]) > 0.9:
            tour.append(r)
            next_location = next(j for j in range(num_cities) if pulp.value(x[current_location, j]) > 0.9)
            total_robot_cost = 0.0
            while next_location != r:
                total_robot_cost += cost_matrix[current_location][next_location]
                current_location = next_location
                tour.append(current_location)
                next_location = next(j for j in range(num_cities) if pulp.value(x[current_location, j]) > 0.9 and j != current_location)
            tour.append(r)
            total_robot_cost += cost_matrix[current_location][r]
            total_cost += total_robot_cost
            print(f"Robot from Depot {r} Tour: {tour}")
            print(f"Robot from Depot {r} Total Travel Cost: {total_robot_cost:.2f}\n")

    print(f"Overall Total Travel Cost: {pulp.value(problem.objective):.2f}")
else:
    print("No optimal solution found.")