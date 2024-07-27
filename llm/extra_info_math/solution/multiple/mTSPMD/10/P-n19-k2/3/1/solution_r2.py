import pulp
from math import sqrt

# City coordinates
coordinates = [
    (30,  nos30), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the distance matrix
n = len(coordinates)
cost_matrix = [[distance(coordinates[i], coordinates[j]) if i != j else float('inf') for j in range(n)] for i in range(n)]

# Initialization of the LP problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables x[(i, j, k)] for routes
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2)), cat='Binary')

# Objective: Minimize the total traveling cost
prob += pulp.lpSum(cost_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(2))

# Constraints

# Each city must be connected into the route
for j in range(2, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(2) if i != j) == 1

# Start from each depot
for k in range(2):
    prob += pulp.lpSum(x[k, j, k] for j in range(n) if j != k) == 1

# Return to each depot
for k in range(2):
    prob += pulp.lpSum(x[j, k, k] for j in range(n) if j != k) == 1

# Continuity of routes
for k in range(2):
    for i in range(n):
        if i != k:  # Exclude depot itself
            prob += pulp.lpSum(x[i, j, k] for j in range(n) if j != i) == pulp.lpSum(x[j, i, k] for j in range(n) if j != i)

# Solve the problem using a solver that provides more visibility, e.g., CBC with msg=True
prob.solve(pulp.PULP_CBC_CMD(msg=1))  # Enable solver output to see what happens during the solve

# Output results
for k in range(2):
    tour = [k]
    next_location = k
    for _ in range(n):
        next_location = [j for j in range(n) if pulp.value(x[next_location, j, k]) == 1][0]
        tour.append(next_location)
        if next_location == k:
            break
  
    tour_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

total_travel_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for k in range(2) for i in range(len(tour) - 1))
print(f"Overall Total Travel Cost: {total_travel_cost}")