import pulp
import math

# Coordinates of the depot and cities (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

n = len(coordinates)  # Number of nodes
m = 4  # Number of robots or salesmen
cities = range(1, n)  # Exclude the depot (index 0)

# Function for Euclidean distance
def euclidean_distance(idx1, idx2):
    return math.sqrt((coordinates[idx1][0] - coordinates[idx2][0]) ** 2 
                     + (coordinates[idx1][1] - coordinates[idx2][1]) ** 2)

# Distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(i, j)

# Problem setup
prob = pulp.LpProblem("Multiple VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Objective
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints
for k in range(m):
    prob += pulp.lpSum(x[(0, j, k)] for j in cities) == 1
    prob += pulp.lpSum(x[(j, 0, k)] for j in cities) == 1

for j in cities:
    prob += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1

for i in range(n):
    for k in range(m):
        if i != 0:
            prob += pulp.lpSum(x[(i, j, k)] for j in range(n) if i != j) == pulp.lpSum(x[(j, i, k)] for j in range(n) if i != j)

for k in range(m):
    prob += pulp.lpSum(x[(i, j, k)] * distance_matrix[i, j] for i in range(n) for j in range(n) if i != j) <= max_distance

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n-2

# Solve the problem
prob.solve()

# Extract routes
result = {}
max_cost = 0
for k in range(m):
    node = 0
    next_node = None
    route = [0]
    cost = 0
    while True:
        next_node = next(j for j in range(n) if pulp.value(x[(node, j, k)]) == 1)
        route.append(next_node)
        cost += distance_matrix[node, next_node]
        node = next_node
        if next_node == 0:
            break
    result[k] = (route, cost)
    max_cost = max(max_cost, cost)
    print("Robot", k, "Tour:", route)
    print("Robot", k, "Total Travel Cost:", cost)

print("Maximum Travel Cost:", max_cost)