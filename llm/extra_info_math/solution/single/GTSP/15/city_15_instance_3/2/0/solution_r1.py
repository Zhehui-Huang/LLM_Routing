import math
import pulp

# City coordinates
cities = {
    0: (16, 90), 
    1: (43, 99), 
    2: (80, 21), 
    3: (86, 92), 
    4: (54, 93), 
    5: (34, 73), 
    6: (6, 61), 
    7: (86, 69), 
    8: (30, 50), 
    9: (35, 73), 
    10: (42, 64), 
    11: (64, 30), 
    12: (70, 95), 
    13: (29, 64), 
    14: (32, 79)
}

# City groups
groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Calculate Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Set up the optimization problem
model = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat="Binary")

# Objective function
model += pulp.lpSum(x[(i, j)] * distances[(i, j)] for i in cities for j in cities if i != j), "Minimize_Total_Distance"

# Constraints
# Each city group sends and receives only one connection from outside
for k, group in groups.items():
    model += sum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"Outflow_group_{k}"
    model += sum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"Inflow_group_{k}"

# Each city is visited exactly once and flows are conserved
for i in cities:
    model += sum(x[(j, i)] for j in cities if j != i) == sum(x[(i, j)] for j in cities if j != i), f"Flow_conservation_{i}"

# Solving the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the solution
path = []
current_city = 0
remaining_cities = set(cities)

# Retrieve the path
for _ in range(len(groups) + 1):
    next_cities = [j for j in remaining_cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if next_cities:
        next_city = next_cities[0]
        path.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

# Complete the tour by adding the depot
path.insert(0, 0)
path.append(0)

# Calculate the total cost
total_cost = sum(distances[(path[i], path[i + 1])] for i in range(len(path) - 1))

# Output
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")