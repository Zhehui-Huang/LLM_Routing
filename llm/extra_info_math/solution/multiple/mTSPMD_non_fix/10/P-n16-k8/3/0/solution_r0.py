from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpInteger
import math

# Given cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of robots and their starting depot
num_robots = 8
start_depot = 0   # All robots start at depot city 0

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Distance cost matrix
n = len(coordinates)
cost = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Create the LP problem
problem = LpProblem("VRP", LpMinimize)

# Variables
x = {(i, j): LpVariable(cat=LpInteger, lowBound=0, upBound=1, name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}

# Objective function
problem += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Total Travel Cost"

# Constraints
# Each non-depot city visited once
for j in range(n):
    if j != start_depot:
        problem += lpSum(x[i, j] for i in range(n) if i != j) == 1
        
# Each non-depot city is departed once
for i in range(n):
    if i != start_depot:
        problem += lpSum(x[i, j] for j in range(n) if i != j) == 1

# Number of robots leaving and returning the starting depot
problem += lpSum(x[start_depot, j] for j in range(n) if j != start_depot) == num_robots

# Solving the problem
status = problem.solve()
print(f"Status: {status}")

# Print the routes for each robot and calculate the costs
routes = {i: [] for i in range(num_robots)}
visited = set()
current_positions = [start_depot] * num_robots

for _ in range(n-1):
    for r in range(num_robots):
        current_pos = current_positions[r]
        for j in range(n):
            if j != current_pos and x[current_pos, j].varValue > 0.9:
                routes[r].append(j)
                current_positions[r] = j
                break

# Output the results
total_cost = 0
for r in range(num_robots):
    cost = sum(cost[routes[r][i]][routes[r][i + 1]] for i in range(len(routes[r]) - 1))
    total_cost += cost
    print(f"Robot {r} Tour: [{start_depot}] + {routes[r]}")
    print(f"Robot {r} Total Travel Cost: {cost}\n")

print(f"Overall Total Travel Cost: {total_cost}")