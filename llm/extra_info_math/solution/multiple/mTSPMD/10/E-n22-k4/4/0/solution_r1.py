import pulp
import math

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

depots = [0, 1, 2, 3]
n_robots = 4

# Calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the cost matrix
cost = {}
for i in cities:
    for j in cities:
        if i != j:
            cost[(i, j)] = euclidean_distance(cities[i], cities[j])
        else:
            cost[(i, j)] = float('inf')  # No loops

# Define the problem
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in cities for j in cities for k in depots),
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, cat=pulp.LpContinuous)

# Objective function
prob += pulp.lpSum([cost[i, j] * x[i, j, k] for i in cities for j in cities for k in depots])

# Constraints
for k in depots:
    prob += pulp.lpSum([x[k, j, k] for j in cities if j != k]) == 1  # Each robot departs from its depot
    prob += pulp.lpSum([x[j, k, k] for j in cities if j != k]) == 1  # Each robot returns to its depot

for j in cities:
    prob += pulp.lpSum([x[i, j, k] for i in cities for k in depots if i != j]) == 1  # Each city visited exactly once

for i in cities:
    for k in depots:
        prob += pulp.lpSum([x[i, j, k] for j in cities if i != j]) == \
                pulp.lpSum([x[j, i, k] for j in cities if i != j])  # Route continuity

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and i not in depots and j not in depots:
            for k in depots:
                prob += u[i] - u[j] + (len(cities) * x[i, j, k]) <= len(cities) - 1

# Solve the problem
prob.solve()

# Output solution
total_cost = 0
routes = {k: [] for k in depots}

for k in depots:
    path = []
    current_city = k
    while True:
        next_cities = [j for j in cities if pulp.value(x[current_city, j, k]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        path.append(next_city)
        current_city = next_city
        if current_city == k:
            break
    routes[k] = [k] + path + [k]
    route_cost = sum(cost[routes[k][i], routes[k][i + 1]] for i in range(len(routes[k]) - 1))
    total_cost += route_cost
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")