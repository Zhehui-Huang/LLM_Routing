import pulp
import math

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities and their positions
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
          (45, 35)]

# Problem parameters
num_vehicles = 2
depots = [0, 1]

n = len(cities)

# Distance matrix
distances = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Problem definition
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum([distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
# Every city needs to be visited exactly once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Every city is left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour prevention and depot linkage
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            prob += x[i, j] * (n - 1) + x[j, i] * (n - 3) <= n - 2

# Depot linkage
for d in depots:
    prob += pulp.lpSum(x[d, j] for j in range(n) if j != d) == 1
    prob += pulp.lpSum(x[i, d] for i in range(n) if i != d) == 1

# Solve the problem
prob.solve()

# Extract routes
routes = [[] for _ in range(num_vehicles)]
for d in depots:
    current_location = d
    while True:
        next_locations = [j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1]
        if not next_locations:
            break
        next_location = next_locations[0]
        routes[depots.index(d)].append((current_location, next_location))
        current_location = next_location

# Calculate and print costs
overall_cost = 0
for index, route in enumerate(routes):
    cost = sum(distances[i, j] for i, j in route)
    overall_cost += cost
    print(f"Robot {index} Tour: {[i for i, _ in route] + [route[-1][1]]}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel