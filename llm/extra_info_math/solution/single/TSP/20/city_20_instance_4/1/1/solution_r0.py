import numpy as np
import pulp

# Coordinates of the cities including the depot city
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the Euclidean distance matrix
def calculate_distances(coords):
    num_cities = len(coords)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return distances

cost_matrix = calculate_distances(coordinates)

# Number of cities including the depot
n = len(coordinates)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("Traveling_Salesman_Problem", pulp.LpMinimize)

# Create variables: x_ij = 1 if traveled from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)),
                          cat='Binary', lowBound=0, upBound=1)

# Objective function - Minimize the total traveling cost
problem += pulp.lpSum([cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)])

# Constraint: Enter each city exactly once (excluding depot at start)
for j in range(n):
    problem += pulp.lpSum([x[i][j] for i in range(n) if i != j]) == 1

# Constraint: Leave each city exactly once
for i in range(n):
    problem += pulp.lpSum([x[i][j] for j in range(n) if i != j]) == 1

# Subtour elimination constraints (to prevent subtours, using Miller-Tucker-Zemlin method)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
problem.solve()

# Check which paths are chosen
route = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i][j]) == 1:
            route.append((i, j))

# Construct the route order from the solution
route_order = [0]
for _ in range(n-1):
    for r in route:
        if r[0] == route_order[-1]:
            route_order.append(r[1])
            break

# Adding depot city at the end
route_order.append(0)

# Calculate the total travel cost
total_cost = sum(cost by the route)
total_cost = sum(cost_matrix[route_order[i]][route_order[i+1]] for i in range(len(route_order)-1))

print("Tour:", route_order)
print("Total travel cost:", round(total_cost, 2))