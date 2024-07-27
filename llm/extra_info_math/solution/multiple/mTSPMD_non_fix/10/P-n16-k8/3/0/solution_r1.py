from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Given cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of robots and their starting depot
num_robots = 8
start_depot = 0

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Distance cost matrix
n = len(coordinates)
cost = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Create LP problem
problem = LpProblem("VRP", LpMinimize)

# Variables
x = {(i, j): LpVariable(f"x_{i}_{j}", 0, 1, LpBinary) for i in range(n) for j in range(n) if i != j}

# Objective function
problem += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for j in range(1, n):  # Ensuring each city is visited exactly once excludes the start
    problem += lpSum(x[i, j] for i in range(n) if i != j) == 1
    problem += lpSum(x[j, i] for i in range(n) if i != j) == 1

# Start at the depot
problem += lpSum(x[start_depot, j] for j in range(1, n)) == num_robots

# Solving the problem
status = problem.solve()

# Interpreting the results
tour = [[] for _ in range(num_robots)]
current_position = [start_depot] * num_robots
for _ in range(n - 1):  # Each robot tours
    for r in range(num_robots):
        for j in range(n):
            if j != current_position[r] and x[current_position[r], j].value() == 1:
                tour[r].append(j)
                current_position[r] = j
                break

# Outputting the results
total_cost = 0
result_str = ""
for r in range(num_robots):
    result_str += f"Robot {r} Tour: [{start_depot}] + {tour[r]}\n"
    if tour[r]:
        robot_cost = sum(cost[tour[r][i]][tour[r][i+1]] for i in range(len(tour[r])-1))
        total_cost += robot_cost
        result_str += f"Robot {r} Total Travel Cost: {robot_cost}\n\n"
    else:
        result_str += f"Robot {r} Total Travel Cost: 0\n\n"

result_str += f"Overall Total Travel Cost: {total_cost}"
print(result_str)