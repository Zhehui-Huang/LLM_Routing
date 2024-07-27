import math
import pulp

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates for each city, including the depot city 0
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Number of cities, including depot
n = len(cities)

# Creating the cost matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) if i != j else float('inf') for j in range(n)] for i in range(n)]

# Setting up the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination (MTZ formulation)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)  # Position variables
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Extracting the solution
route = [0]
while len(route) < n:
    for j in range(n):
        if pulp.value(x[route[-1], j]) == 1:
            route.append(j)
            break
route.append(0)  # Returning to the start

# Computing the total cost of the tour
total_cost = sum(distance_ctx;matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Output
print(f"Tour: {route}")
print(f"Total travel cost: {total_cost}")