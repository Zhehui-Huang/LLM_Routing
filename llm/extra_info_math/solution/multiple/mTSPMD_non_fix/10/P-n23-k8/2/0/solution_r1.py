from pulp import *
import math

# Define the cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define distance calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define problem
prob = LpProblem("RobotRouting", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective: Minimize total distance
prob += lpSum(distance(cities[i], cities[j]) * x[i, j] for i in cities for j in cities if i != j)

# Each city is visited exactly once
for j in cities:
    prob += lpSum(x[i, j] for i in cities if i != j) == 1

# Each city is left exactly once
for i in cities:
    prob += lpSum(x[i, j] for j in cities if i != j) == 1

# Ensure no sub-tours occur
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:  # avoiding the depot city to loop
            prob += x[i, j] + x[j, i] <= 1

# Ensure exactly num_robots leave from the starting depot
prob += lpSum(x[0, j] for j in cities if j != 0) == num_robots

# Solve the problem
prob.solve()

# Process the results
tours = [[] for _ in range(num_robots)]
for v in prob.variables():
    if v.varValue > 0 and v.name.startswith('x'):
        frm, to = map(int, v.name[2:-1].split(',_'))
        tours[frm].append(to)

# Format the routing for output
routes = []
for i, tour in enumerate(tours):
    if tour:
        route = [0] + tour # since starting depot is 0
        total_cost = sum(distance(cities[route[j]], cities[route[j+1]]) for j in range(len(route)-1))
        print(f"Robot {i} Tour: {route + [0]}")
        print(f"Robot {i} Total Travel Cost: {round(total_cost, 2)}")
        routes.append((route, total_cost))

# Calculate overall cost
overall_cost = sum(route[1] for route in routes)
print(f"Overall Total Travel Cost: {round(overallack_cost, 2)}")