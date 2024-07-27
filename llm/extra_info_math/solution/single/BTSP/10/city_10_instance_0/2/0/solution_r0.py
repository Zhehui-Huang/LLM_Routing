import pulp as pl
import math

# Define the cities and their positions
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
    9: (42, 49),
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Set up the problem
problem = pl.LpProblem("TSP", pl.LpMinimize)
x = [[pl.LpVariable(f"x_{i}_{j}", cat=pl.LpBinary) for j in range(n)] for i in range(n)]
z = pl.LpVariable("z", lowBound=0)

# Objective: minimize the maximum distance used in the tour
problem += z

# Constraints
for i in range(n):
    problem += pl.lpSum(x[i][j] for j in range(n) if i != j) == 1  # leave city i exactly once
    problem += pl.lpSum(x[j][i] for j in range(n) if i != j) == 1  # arrive at city i exactly once

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[i][j] * x[i][j] <= z

# Subtour elimination: using Miller-Tucker-Zemlin formulation
u = [pl.LpVariable(f"u_{i}", lowBound=0, cat=pl.LpContinuous) for i in range(n)]  # ordering variables
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
problem.solve()

# Extract the tour based on the variables x_ij that are set to 1
tour = []
current = 0
for _ in range(n):
    tour.append(current)
    for j in range(n):
        if pl.value(x[current][j]) == 1:
            current = j
            break
tour.append(0)  # return to the depot

# Calculate the total cost and the maximum distance in the final tour
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")