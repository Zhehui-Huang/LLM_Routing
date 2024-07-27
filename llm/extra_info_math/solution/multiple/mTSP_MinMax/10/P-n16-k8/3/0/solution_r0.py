import pulp as pl
import math

# Given city coordinates with depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

num_robots = 8
tour_lists = {}

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate distances
distances = {(i, j): calculate_distance(cities[i], cities[j])
             for i in cities.keys() for j in cities.keys() if i != j}

# Create the optimization problem
problem = pl.LpProblem("mTSP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", (range(len(cities)), range(len(cities)), range(num_robots)),
                        cat='Binary', lowBound=0, upBound=1)

# Continuous variables to prevent subtours
u = pl.LpVariable.dicts("u", range(1, len(cities)), cat='Continuous', lowBound=0)

# Objective function: Minimize the maximum distance a robot travels
max_distance = pl.LpVariable("max_distance")
problem += max_distance

# Constraints

# Each non-depot city must be visited exactly once by any salesman
for j in range(1, len(cities)):
    problem += pl.lpSum(x[i][j][k] for i in range(len(cities)) for k in range(num_robots) if i != j) == 1

# Salesman must leave each non-depot city exactly once
for k in range(num_robots):
    for j in range(1, len(cities)):
        problem += pl.lpSum(x[j][i][k] for i in range(len(cities)) if i != j) == pl.lpSum(x[i][j][k] for i in range(len(cities)) if i != j)

# Salesman leaves from depot
for k in range(num_robots):
    problem += pl.lpSum(x[0][j][k] for j in range(1, len(cities))) == 1

# Salesman returns to depot
for k in range(num_robots):
    problem += pl.lpSum(x[i][0][k] for i in range(1, len(cities))) == 1

# Subtour elimination
for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (len(cities) - 1) * x[i][j][k] <= len(cities) - 2

# Maximum distance constraints
for k in range(num_robots):
    problem += pl.lpSum(distances[i, j] * x[i][j][k] for i in range(len(cities)) for j in range(len(cities)) if i != j) <= max_distance

# Solve problem
problem.solve()

tours = {k: [0] for k in range(num_robot')}}
max_travel_cost = max_distance.varValue

# Read the solution
for k in range(num_robots):
    path = []
    current = 0
    remaining = set(range(1, len(cities)))
    while remaining:
        next_step = [j for j in remaining if pl.value(x[current][j][k]) == 1]
        if next_step:
            next_city = next_step[0]
            path.append(next_city)
            current = next_city
            remaining.remove(next_city)
        else:
            break
    path.append(0)  # Return to depot
    tour_lists[k] = path

# Output each tour and calculate cost
total_costs = {}
for k, path in tour_lists.items():
    cost = sum(distances[path[i], path[i + 1]] for i in range(len(path) - 1))
    total_costs[k] = cost
    print(f"Robot {k} Tour: {path}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print("Maximum Travel Cost:", max_travel_cost)