import pulp as pl
import math

# Define the coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the Euclidean distance function
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem parameters
num_cities = len(coordinates)
num_robots = 8
depot = 0

# Create the LP problem
problem = pl.LpProblem("Robot_Routing", pl.LpMinimize)

# Decision variables
# x[i, j, k] is 1 if robot k travels from city i to city j
x = pl.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)], cat='Binary')
# u[i] is a position variable for Subtour Elimination Constraints
u = pl.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# Objective Function: Minimize the total distance traveled
problem += pl.lpSum(distance(i, j) * x[i, j, k] for i in range(num_important_cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
# A city must be visited exactly once by any robot
for j in range(1, num_cities):
    problem += pl.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Flow conservation for each robot
for k in range(num_robots):
    for p in range(num_cities):
        problem += pl.lpSum(x[p, j, k] for j in range(num_cities)) == pl.lpSum(x[j, p, k] for j in range(num_cities))

# Every robot must leave and enter the depot
for k in range(num_robots):
    problem += pl.lpSum(x[depot, j, k] for j in range(1, num_cities)) == 1
    problem += pl.lpSum(x[i, depot, k] for i in range(1, num_cities)) == 1

# Subtour Elimination Constraints (SEC)
for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                problem += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solve the problem
problem.solve()

# Output results
tours = [[] for _ in range(num_robots)]
costs = [0 for _ in range(num_robots)]

# Extract tours from the decision variables
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if pl.value(x[i, j, k]) == 1:
                tours[k].append((i, j))
                costs[k] += distance(i, j)

# Format tours properly, starting and ending at the depot
formatted_tours = [[depot] for _ in range(num_robots)]
for k in range(num_robots):
    next_city = depot
    while len(formatted_tours[k]) < len(tours[k]) + 1:
        for (i, j) in tours[k]:
            if i == next_city:
                formatted_tours[k].append(j)
                next_city = j
                break

# Printing each robot's tour and costs
overall_cost = sum(costs)
for k in range(num_robots):
    print(f"Robot {k} Tour: {formatted_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Overall Total Travel Cost: {overall_cost}")