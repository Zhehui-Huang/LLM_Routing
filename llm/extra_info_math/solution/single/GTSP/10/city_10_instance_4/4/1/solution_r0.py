import pulp
import math

# Define the coordinates of the depot and the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Define the city groups
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create a linear programming problem with pulp
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables x_ij for arcs between each pair of nodes (binary: 0 or 1)
x = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective function to minimize the total travel cost
problem += pulp.lpSum(distance(i, j) * x[(i, j)] for i in cities for j in cities if i != j), "Minimize_Total_Travel_Cost"

# Subtour Elimination Constraints
u = {}
for group in groups:
    for city in group:
        u[city] = pulp.LpVariable(f"u_{city}", 0, None, pulp.LpContinuous)

for i, group in enumerate(groups, 2):
    for j, other_group in enumerate(groups, 2):
        if i != j:
            problem += (u[group[0]] - u[other_group[0]] + len(groups) * pulp.lpSum(x[(p, q)] for p in group for q in otherGroup) + (len(groups) - 2) * pulp.lpSum(x[(q, p)] for p in group for q in otherGroup) <= len(groups) - 1), f"Subtour_Constraint_{i}_{j}"

# Constraints to ensure exactly one exit and entrance for each group
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"Exiting_{group}"
    problem += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"Entering_{group}"

# Constraints to ensure flow conservation
for k in range(len(cities)):
    problem += pulp.lpSum(x[(j, k)] for j in cities if j != k) - pulp.lpSum(x[(k, j)] for j in cities if j != k) == 0, f"Flow_Conserve_{k}"

# Solve the problem using pulp's solver
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour and calculate the travel cost
tour = [0]
current = 0
total_cost = 0
while True:
    for c in cities:
        if c != current and pulp.value(x[(current, c)]) == 1:
            tour.append(c)
            total_cost += distance(current, c)
            current = c
            break
    if current == 0:
        break

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)