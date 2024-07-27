from pulp import *
import math

# Coordinates for the different cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of salesmen
m = 2
# Number of nodes including the depot
n = len(coordinates)

# Generate distance matrix
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create the problem variable to contain the problem data
problem = LpProblem("Robot_Routing_Problem", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0)

# Objective
# Define a variable that represents the maximum tour cost across all robots
max_cost = LpVariable("max_cost", lowBound=0)
problem += max_cost, "Maximize_of_Tour_Cost"

for k in range(m):
    problem += lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n)) <= max_cost

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += lpSum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Each salesman starts and ends at the depot
for k in range(m):
    problem += lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i][j][k] <= n-2

# Flow conservation
for k in range(m):
    for p in range(1, n):
        problem += lpSum(x[p][j][k] for j in range(n) if j != p) - lpSum(x[i][p][k] for i in range(n) if i != p) == 0

# Solve the problem
problem.solve()

# Print the results
tours = [[0] for _ in range(m)]  # include the initial starting depot for each salesman

for k in range(m):
    i = 0
    while True:
        next_cities = [j for j in range(n) if value(x[i][j][k]) == 1]
        if len(next_cities) == 0:
            break
        next_city = next_cities[0]
        tours[k].append(next_city)
        i = next_city
        if next_city == 0:
            break

for index, tour in enumerate(tours):
    cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

max_travel_cost = value(max_cost)
print(f"Maximum Travel Cost: {max_travel_it_cost}")