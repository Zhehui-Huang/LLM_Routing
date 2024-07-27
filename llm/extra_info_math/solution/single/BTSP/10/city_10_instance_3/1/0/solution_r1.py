import numpy as
import pulp
from scipy.spatial import distance_matrix

# Define the cities' coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Calculate Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Number of cities including the depot
n = len(cities)

# Create the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Auxiliary variable to represent maximum distance
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective: minimize the maximum distance traveled between any two consecutive cities
prob += max_dist

# Constraints
# Each city must be entered and left exactly once
for i in range(n):
    prob += pulp.lpSum([x[i][j] for j in range(n) if i != j]) == 1
    prob += pulp.lpSum([x[j][i] for j in range(n) if i != j]) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += dist_matrix[i][j] * x[i][j] <= max_dist

# Subtour elimination constraints using the MTZ formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i][j] <= n - 2

# Solve the problem using an available solver
solver = pulp.PULP_CBC_CMD(msg=True, timeLimit=120)
solution_status = prob.solve(solver)

if pulp.LpStatus[solution_status] == 'Optimal':
    # Extract the solution
    tour = [0]  # start at the depot
    current = 0
    for _ in range(n-1):
        next_city = [j for j in range(n) if pulp.value(x[current][j]) == 1][0]
        tour.append(next_city)
        current = next_city
    tour.append(0)  # return to the depot

    # Calculating total travel cost and maximum distance between consecutive cities
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", pulp.value(max_dist))
else:
    print("Failed to find optimal solution. Solver status:", pulp.LpStatus[solution_status])