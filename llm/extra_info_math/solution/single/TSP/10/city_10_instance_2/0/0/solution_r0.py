import pulp
import math

# City coordinates
coordinates = [
    (90, 3),   # City 0 - Depot
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

n = len(coordinates)

# Calculate Euclidean Distance between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

dist = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective
prob += pulp.lpSum(dist[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
# Each city must be arrived at from exactly one other city
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Each city must be left to exactly one other city
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour elimination constraint (SEC) using Miller-Tucker-Zemlin (MTZ) formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
prob.solve()

# Collect the results
tour = []
current = 0  # start from depot
while True:
    tour.append(current)
    next_cities = [j for j in range(n) if pulp.value(x[current, j]) == 1]
    if next_cities:
        current = next_cities[0]
    if current == 0:
        break

tour.append(0)  # Return to depot
total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)