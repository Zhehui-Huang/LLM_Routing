import math
from pulp import *

def euclidean(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Problem data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
num_cities = len(coordinates)
cost_matrix = {(i, j): euclidean(coordinates[i], coordinates[j]) for i in range(num_cities) for j in range(num_cities) if i != j}
num_robots = 8
depot = 0

# Create problem
prob = LpProblem("VRP", LpMinimize)

# Define Variables
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(num_cities), lowBound=0, cat=LpContinuous)

# Objective Function
prob += lpSum(cost_matrix[i, j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Each city is visited exactly once
for j in range(1, num_cities):
    prob += lpSum(x[i, j] for i in range(num_cities) if i != j) == 1

# Each city is left exactly once
for i in range(1, num_cities):
    prob += lpSum(x[i, j] for j in range(num_cities) if i != j) == 1

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            prob += u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1

# Solve the problem
prob.solve()

# Extract the solution
routes = []
for i in range(num_cities):
    route = []
    cur = i
    while True:
        route.append(cur)
        found_next = False
        for j in range(num_cities):
            if j != cur and x[cur, j].varValue == 1:
                cur = j
                found_next = True
                break
        if not found_next:
            break
    if route[0] == depot and len(route) > 1:
        routes.append(route)

overall_cost = sum(cost_matrix[route[i], route[i+1]] for route in routes for i in range(len(route)-1))
# Output tours and travel costs
for robot, route in enumerate(routes):
    tour_cost = sum(cost_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")