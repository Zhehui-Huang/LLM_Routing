from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, LpContinuous
import math

# Define the coordinates of the cities including the depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Number of nodes and robots
n = len(coordinates)
m = 8  # Number of robots

# Create costs matrix
costs = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
problem = LpProblem("VRP_Multiple_Robots", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0, cat=LpContinuous)

# Objective: Minimize the maximum travel cost among all tours
max_cost = LpVariable("max_cost", lowBound=0)
problem += max_cost

# Constraints
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1  # Leave depot
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1  # Return to depot
    for j in range(1, n):
        problem += lpSum(x[i, j, k] for i in range(n) if i != j) == lpSum(x[j, i, k] for i in range(n) if i != j)

for k in range(m):
    for i in range(1, n):
        problem += lpSum(x[i, j, k] for j in range(n) if i != j) - lpSum(x[j, i, k] for j in range(n) if i != j) == 0

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * lpSum(x[i, j, k] for k in range(m)) <= n - 1

# Ensure the max cost limit is not exceeded for any robot's tour
for k in range(m):
    problem += lpSum(costs[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_cost

# Solve Problem
problem.solve()

# Extract tours for each robot
tours = [[] for _ in range(m)]
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and x[i, j, k].varValue == 1:
                tours[k].append((i, j))

# Convert tours to a readable format and calculate the cost
for k in range(m):
    tour = []
    current_location = 0
    tour_cost = 0
    tour.append(current_location)
    while True:
        next_step = next((j for j in range(n) if x[current_location, j, k].varValue == 1), None)
        if next_step is None or next_step == 0:
            tour.append(0)
            break
        tour.append(next_step)
        tour_cost += costs[current_location][next_step]
        current_location = next_step
    print(f"Robot {k} Tour:", tour)
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print("Maximum Travel Cost:", max_cost.varValue)