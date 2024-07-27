import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates including the depot
coordinates = [
    (145, 215),  # Depot
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

# Number of salesmen (robots)
m = 4
n = len(coordinates)

# Create a dictionary to hold the distances between each pair of nodes
distance = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Setup the problem
problem = pulp.LpProblem("Minimax_Multi_Traveling_Salesman_Problem", pulp.LpMinimize)

# Decision variables: x_ijk
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat='Binary')

# Continuous variables for sub-tour elimination
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Assignment constraints: each city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for j in range(n):
        problem += (pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) -
                    pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j) == 0)

# Each salesman starts at the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1

# Each salesman ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[(i, 0, k)] for i in range(1, n)) == 1

# Subtour elimination constraints
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                problem += u[i] - u[j] + (n - 1) * x[(i, j, k)] <= n - 2

# Ensure max_distance is at least as large as each individual route distance
for k in range(m):
    problem += pulp.lpSum(distance[i, j] * x[i, j, k] for (i, j) in distance) <= max_distance

# Solve the problem
status = problem.solve()

# Output results
print("Status:", pulp.LpStatus[status])

routes = []
costs = []

for k in range(m):
    route = [0]
    while True:
        extensions = [(j, x[(route[-1], j, k)]) for j in range(n) if route[-1] != j and pulp.value(x[(route[-1], j, k)]) == 1]
        if not extensions:
            break
        next_city = extensions[0][0]
        route.append(next_city)
    route.append(0)  # Return to depot
    routes.append(route)
    route_cost = sum(distance[route[i], route[i + 1]] for i in range(len(route) - 1))
    costs.append(route_cost)
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {route_cost:.2f}")

max_cost = max(costs)
print("Maximum Travel Cost among all tours: {:.2f}".format(max_cost))