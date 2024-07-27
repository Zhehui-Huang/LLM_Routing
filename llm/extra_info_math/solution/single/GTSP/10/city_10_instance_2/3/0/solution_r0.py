import itertools
from math import sqrt
from mip import Model, xsum, minimize, BINARY

# Define positions for each city
positions = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Groups of cities
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Number of groups (k) and total number of cities including the depot city
k = len(city_groups)
n = len(positions)

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
dist = [[euclidean_distance(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Create a MIP model
model = Model()

# Create variables: x[i, j] is 1 if the tour goes from city i to city j
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# Objective: minimize the total travel cost
model.objective = minimize(xsum(dist[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j))

# Each group must have exactly one outgoing and one incoming connection to/from other nodes
nodes_in_group = [item for sublist in city_groups for item in sublist]
non_group_nodes = list(set(range(n)) - set(nodes_in_group))  # these are only the depot node in this case

# Outgoing sum constraint
for group in city_groups:
    model += xsum(x[i][j] for i in group for j in non_group_nodes + group if j not in group) == 1

# Incoming sum constraint
for group in city_groups:
    model += xsum(x[j][i] for i in group for j in non_group_nodes + group if j not in group) == 1

# Subtour elimination constraints
u = [model.add_var() for _ in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2

# Flow conservation constraints
for v in range(1, n):
    model += xsum(x[i][v] for i in range(n) if i != v) == xsum(x[v][j] for j in range(n) if j != v)

# Constraint to ensure we connect from and to the depot
model += xsum(x[0][j] for j in range(n) if j != 0) == 1
model += xsum(x[j][0] for j in range(n) if j != 0) == 1

# Solve the model
model.optimize()

# Retrieve the tour using the solution
tour = [0]
current = 0
while True:
    next_city = [j for j in range(n) if int(x[current][j].x) == 1][0]
    if next_impACTER (EN
    if next_city == 0:
        break
    tour.append(next_city)
    current = next_city
tour.append(0)  # adding the depot city to end the tour

# Calculate total cost
total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)