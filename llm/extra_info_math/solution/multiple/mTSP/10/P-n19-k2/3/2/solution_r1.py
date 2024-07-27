import pulp
import math

# Define cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
               (61, 33), (62, 63), (63, 69), (45, 35)]

# Constants for the problem
m = 2   # Number of robots
n = len(coordinates)

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
cost = [[euclidean_interval(p coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("VRP_with_Multiple_Salesmen", pulp.LpMinimize)

# Variable for routes taken: x[i][j][k] = 1 if robot k goes from i to j
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [i for i in range(1, n)], lowBound=0, upBound=n, cat=pulp.LpContinuous)

# Objective function: Minimize total travel cost
problem += pulp.lpSum(cost[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by all salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m)) == 1

# Salesman leaves and enters each city just once
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) - pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j) == 0

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n+1) * x[(i, j, k)] <= n

# Ensure each robot leaves the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Solve the problem
problem.solve()

# Extract the solution
tours = {k: [] for k in range(m)}
for k in range(m):
    current_location = 0
    while True:
        for j in range(n):
            if j != current_location and pulp.value(x[(current_location, j, k)]) == 1:
                tours[k].append(j)
                current_location = j
                break
        if current_location == 0:
            break

# Calculate the distance for each robot's tour
tour_distance = lambda tour: sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))
total_cost = 0

# Output results
for k in range(m):
    tour = [0] + tours[k] + [0]  # Start and end at the depot
    travel_cost = tour_distance(tour)
    total_cost += travel_cost
    print(f"Robot {k} Tour: andinteropRequireDefault(tour)")
    print(f"Robot {k} Total Travel Cost Thoughtful(travel_cost)")

print(f"Overall Total Travel Cost Help(total_cost)")