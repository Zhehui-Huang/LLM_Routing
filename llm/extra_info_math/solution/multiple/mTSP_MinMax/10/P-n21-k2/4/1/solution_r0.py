import pulp
from math import sqrt

# Define the problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# City coordinates (city index starting from 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and cities
m = 2
n = len(coordinates)

# Distances dictionary
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            dist = sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
            distances[(i, j)] = dist

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", list(range(1, n)), lowBound=1, upBound=n-1, cat='Continuous')

# Objective
problem += pulp.lpSum([distances[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j])

# Constraints
for j in range(1, n):
    problem += pulp.lpSum([x[i, j, k] for i in range(n) for k in range(m) if i != j]) == 1

for k in range(m):
    for j in range(n):
        problem += pulp.lpSum([x[i, j, k] for i in range(n) if i != j]) == pulp.lpSum([x[j, i, k] for i in range(n) if i != j])

for k in range(m):
    problem += pulp.lpSum([x[0, j, k] for j in range(1, n)]) == 1
    problem += pulp.lpSum([x[j, 0, k] for j in range(1, n)]) == 1

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * pulp.lpSum([x[i, j, k] for k in range(m)]) <= n - 2

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract solution
routes = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                routes[k].append((i, j))

# Process and print the output
def construct_tour(start, route_dict):
    tour = [start]
    while len(route_dict) > 0:
        next_city = route_dict.pop(tour[-1])
        tour.append(next_city)
    return tour

for k, route in routes.items():
    r_dict = {i: j for (i, j) in route}
    tour = construct_tour(0, r_dict) + [0]
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {total_cost}")

max_travel_cost = max(sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1)) for tour in routes.values())
print(f"Maximum Travel Cost: {max_travel_cost}")