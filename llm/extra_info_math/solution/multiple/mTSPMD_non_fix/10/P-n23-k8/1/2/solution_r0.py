from math import sqrt
import itertools
from mip import Model, xsum, minimize, BINARY

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Calculate Euclidian distances
def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

n = len(cities)
dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Number of robots
m = 8

# Model setup
model = Model()

# Variables: x[i,j] is 1 if travel from i to j
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# Objective: minimize total travel cost
model.objective = minimize(xsum(dist[i][j] * x[i][j] for i in range(n) for j in range(n)))

# Each city is visited exactly once, except for depot 0 which is the start for all robots
for j in range(1, n):
    model += xsum(x[i][j] for i in range(n)) == 1
    model += xsum(x[j][i] for i in range(n)) == 1

# Exactly m departures and arrivals from/to the depot city 0
model += xsum(x[0][j] for j in range(1, n)) == m
model += xsum(x[j][0] for j in range(1, n)) == m

# Subtour elimination
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
model.optimize()

# Retrieve routes from model
routes = [[i for i in range(n) if x[r][i].x >= 0.99] for r in range(n)]
organized_routes = []
for route in routes:
    if route:
        organized_route = []
        current_city = 0
        while True:
            next_city = route[current_city]
            organized_route.append(next_city)
            if next_city == 0:
                break
            current_city = next_city
        organized_routes.append(organized_route)

# Calculate and print the costs
total_cost = 0
for index, route in enumerate(organized_routes):
    cost = sum(dist[route[i]][route[i + 1]] for i in range(len(route) - 1))
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")