from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
from math import sqrt

# Distance function
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of robots
num_robots = 2
n = len(cities)

# Cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i == j:
            cost_matrix[i, j] = 0
        else:
            cost_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Problem
prob = LpProblem("RobotRoutingProblem", LpMinimize)

# Variables
x = LpVariable.dicts("x", (range(n), range(n), range(num_robots)), cat=LpBinary)  # x[i, j, k]
u = LpVariable.dicts("u", range(2, n), lowBound=0, cat='Continuous')  # position variables, u[i]

# Objective
max_distance = LpVariable("max_distance")
prob += max_distance

# Constraints
# Exactly one visit to each node
for j in range(1, n):
    prob += lpSum(x[i][j][k] for i in range(n) for k in range(num_robots)) == 1

# Flow conservation
for k in range(num_robots):
    for p in range(n):
        prob += lpSum(x[p][j][k] for j in range(n)) - lpSum(x[i][p][k] for i in range(n)) == 0

# Each robot starts and ends at the depot
for k in range(num_robots):
    prob += lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            prob += u[i] - u[j] + n * lpSum(x[i][j][k] for k in range(num_robots)) <= n - 1

# Max distance constraint
for k in range(num_robots):
    prob += lpSum(x[i][j][k] * cost_matrix[i][j] for i in range(n) for j in range(n)) <= max_distance

# Solve the problem
prob.solve()

# Output results
for k in range(num_robots):
    print(f"Robot {k} Tour: ", end="")
    tour = [0]
    next_city = 0
    while True:
        next_city = [j for j in range(n) if x[next_city][j][k].varValue == 1][0]
        tour.append(next_city)
        if next_city == 0:
            break
    print(tour)
    distance = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Total Travel Cost: {distance}")

print(f"Maximum Travel Cost: {max_distance.value()}")