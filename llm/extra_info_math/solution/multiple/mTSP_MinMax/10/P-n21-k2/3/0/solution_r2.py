from pulp import *
import math

# Coordinates of Cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
n = len(cities)
num_robots = 2

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create problem
prob = LpProblem("MultiRobotTSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(num_robots)], cat=LpBinary)
u = LpVariable.dicts("u", [(i) for i in range(1, n)], lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum route among all routes
max_route_length = LpVariable("max_route_length")
prob += max_route_length

# Constraints
# Assignment constraint
for j in range(1, n):
    prob += lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(num_robots)) == 1

# Each robot must leave each city it enters
for k in range(num_robots):
    for i in range(1, n):
        prob += lpSum(x[(i, j, k)] for j in range(n) if i != j) == lpSum(x[(j, i, k)] for j in range(n) if i != j)

# Each robot leaves the depot and returns to it
for k in range(num_robots):
    prob += lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    prob += lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                prob += (u[i] - u[j] + n * x[(i, j, k)]) <= n-1

# Max route length constraint
for k in range(num_robots):
    prob += lpSum(x[(i, j, k)] * distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j) <= max_route_length

# Solve the problem
prob.solve()

# Output
print("Status:", LpStatus[prob.status])
print("Maximum Route Length:", max_route_representation(value(max_route_length)))

for k in range(num_robots):
    print(f"Robot {k} Tour:", end=' ')
    route = []
    for i in range(n):
        for j in range(n):
            if x[(i, j, k)].varValue == 1:
                route.append((i, j))
    # Order route starting from the depot
    ordered_route = []
    current_location = 0
    while len(ordered_route) < len(route):
        for i, j in route:
            if i == current_location:
                ordered_route.append(j)
                current_location = j
                break
    print([0] + ordered_socket_route)