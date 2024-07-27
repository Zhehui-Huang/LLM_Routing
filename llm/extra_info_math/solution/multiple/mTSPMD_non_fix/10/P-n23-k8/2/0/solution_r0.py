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

# Number of robots and their starting depot
num_robots = 8
starting_depot = 0

# Variables
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
u = LpVariable.dicts("u", (i for i in cities), lowBound=0, upBound=len(cities), cat='Integer')

# Objective: Minimize total distance
prob += lpSum(distance(cities[i], cities[j]) * x[i, j] for i in cities for j in cities if i != j)

# Constraints
# Each city is visited exactly once
for j in cities:
    prob += lpSum(x[i, j] for i in cities if i != j) == 1

# Each city has exactly one departure
for i in cities:
    prob += lpSum(x[i, j] for j in cities if i != j) == 1

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and (i != starting_depot and j != starting_depot):
            prob += u[i] - u[j] + (len(cities) * x[i, j]) <= len(cities) - 1

# Solve the problem
prob.solve()

# Output the result
routes = {i: [] for i in range(num_robots)}
total_distance = 0
for i in cities:
    for j in cities:
        if i != j and x[i, j].varValue == 1:
            from_depot = (i == starting_depot)
            robot_id = routes.keys() & {starting_depot} or from_depot
            routes[robot_id].append((i, j))
            total_distance += distance(cities[i], cities[j])

for robot_id, path in routes.items():
    route = [starting_depot] + [j for i, j in path]  # Ensure proper formatting of route
    travel_cost = sum(distance(cities[i], cities[j]) for i, j in path)
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {travel_cost}")

print(f"Overall Total Travel Cost: {total_distance}")