import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates including the depot
coordinates = [
    (145, 215), # Depot
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
    problem += sum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for i in range(1, n):
        problem += sum(x[(i, j, k)] for j in range(n) if i != j) == sum(x[(j, i, k)] for j in range(n) if i != j)

# Each salesman leaves the depot
for k in range(m):
    problem += sum(x[(0, j, k)] for j in range(1, n)) == 1

# Each salesman returns to the depot
for k in range(m):
    problem += sum(x[(i, 0, k)] for i in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Ensure max_distance is at least as large as each individual route distance
for k in range(m):
    problem += sum(distance[i, j] * x[i, j, k] for (i, j) in distance) <= max_distance

# Solve the problem
status = problem.solve()

# Output results
print("Status:", pulp.LpStatus[status])

routes = list()
costs = list()

for k in range(m):
    route = [0]
    while True:
        found = False
        for j in range(n):
            if j != route[-1] and pulp.value(x[(route[-1], j, k)]) == 1:
                route.append(j)
                found = True
                break
        if not found or route[-1] == 0:
            break
    routes.append(route)
    cost = sum(distance[route[i], route[i + 1]] for i in range(len(route) - 1))
    costs.append(cost)
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {cost:.2f}")

print("Maximum Travel Cost among all tours: {:.2f}".format(pulp.value(max_distance)))