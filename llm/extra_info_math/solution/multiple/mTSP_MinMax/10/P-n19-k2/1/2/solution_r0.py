import pulp
import math

# Given data
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_cities = len(coordinates)
num_robots = 2

# Euclidean distance calc function
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Set up problem
problem = pulp.LpProblem("RobotTourProblem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective function
max_travel_cost = pulp.LpVariable("max_travel_cost")
problem += max_travel_cost

# Constraints
# 1. Each city (not depot) visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum([x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j]) == 1

# 2. Flow conservation
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) - pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j) == 0

# Depot constraints
for k in range(num_robots):
    problem += pulp.lpSum([x[0, j, k] for j in range(1, num_cities)]) == 1
    problem += pulp.lpSum([x[j, 0, k] for j in range(1, num_cities)]) == 1

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities-1) * x[i, j, k] <= num_cities - 2

# Connecting cost and binary decision variables with the objective
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist = calc_distance(coordinates[i], coordinates[j])
            for k in range(num_robots):
                problem += x[i, j, k] * dist <= max_travel_cost

# Solve the problem
problem.solve()

# Extracting results
routes = []
costs = []
max_cost = 0
for k in range(num_robots):
    tour = [0]
    while True:
        next_city = [j for j in range(num_cities) if pulp.value(x[tour[-1], j, k]) == 1]
        if not next_city:
            break
        tour.extend(next_city)
        if tour[-1] == 0:
            break
    routes.append(tour)
    tour_cost = sum(calc_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    costs.append(tour_cost)
    max_cost = max(max_cost, tour_cost)

# Printing results as per the format requirements
for k in range(num_robots):
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Maximum Travel Cost: {max_cost}")