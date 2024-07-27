import pulp
import math

# City coordinates (including depot as city 0)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # number of nodes including the depot
m = 2  # number of robots

# Distance function
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# PuLP Model
model = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x",
                          ((i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j), 
                          cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=pulp.LpContinuous)

# Objective Function
model += pulp.lpSum(euclidean_distance(i, j) * x[(i, j, k)] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints
# Each node must be entered and left once
for j in range(1, n):
    model += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1
    model += pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j for k in range(m)) == 1
    
# Each robot starts and ends at the depot
for k in range(m):
    model += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    model += pulp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n * x[(i, j, k)]) <= n - 1

# Solve model
model.solve()

# Output results
routes = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[(i, j, k)]) == 1:
                routes[k].append((i, j))

# Display results as tours starting and ending at the depot
for k in range(m):
    print(f"Robot {k} Tour:", end=" ")
    next_node = 0
    route = [0]
    while True:
        next_moves = [(j) for (i, j) in routes[k] if i == next_node]
        if not next_moves:
            break
        next_node = next_moves[0]
        route.append(next_node)
        if next_node == 0:
            break
    print(route)
    tour_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

overall_cost = sum(sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1)) for k, route in routes.items() for route in [route])
print(f"Overall Total Travel Cost: {overall_cost}")