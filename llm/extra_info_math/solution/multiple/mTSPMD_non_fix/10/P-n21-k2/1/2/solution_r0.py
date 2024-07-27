import pulp
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

num_vehicles = 2
depots = [0, 1]

n = len(cities)  # Total number of nodes including depots

# Calculate distances between each city
costs = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Create the problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=1, upBound=n, cat='Continuous')

# Objective function
prob += pulp.lpSum(costs[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each node is visited exactly once
for j in range(n):
    if j not in depots:
        prob += sum(x[i, j] for i in range(n) if i != j) == 1  # Incoming
        prob += sum(x[j, i] for i in range(n) if i != j) == 1  # Outgoing

# Number of vehicles leaving the depot
for i in depots:
    prob += sum(x[i, j] for j in range(n) if i != j) == num_vehicles // len(depots)
        
# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j and i not in depots and j not in depots:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
prob.solve()

routes = [[] for _ in range(num_vehicles)]
tour_costs = [0] * num_vehicles

# Extract the solution
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            assigned_to = 0 if i == 0 or j == 0 else 1  # simplistic assignment
            routes[assigned_to].append((i, j))
            tour_costs[assignedo] += costs[i, j]

# Print results
total_cost = sum(tour_costs)
for idx, route in enumerate(routes):
    tour_route = [depots[idx]] + [j for i, j in route if i == depots[idx]] + [depots[idx]]
    print(f"Robot {idx} Tour: {tour_route}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")
print(f"Overall Total Travel Cost: {total_cost}")