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

# Subtour elimination constraints
u = [model.add_var() for _ in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2

# Flow conservation constraints
for v in range(n):
    model += xsum(x[i][v] for i in range(n) if i != v) == xsum(x[v][j] for j in range(n) if j != v)

# Adding connection to the depot constraints
model += xsum(x[0][j] for j in range(n) if j != 0) == 1
model += xsum(x[j][0] for j in range(n) if j != 0) == 1

# Group constraints: exactly one outgoing and one incoming edge
for group in city_groups:
    nodes_outside_group = list(set(range(n)) - set(group))
    model += xsum(x[i][j] for i in group for j in nodes_outside_group) == 1
    model += xsum(x[j][i] for i in group for j in nodes_outside_group) == 1

# Solve the model
status = model.optimize()

if status == model.Optimal:
    tour = [0]
    current = 0
    visited = set([0])
    # Extract the tour from the variables
    while True:
        next_city = None
        for j in range(n):
            if int(x[current][j].x) == 1 and j not in visited:
                next_city = j
                break
        if next_city is None:  # No unvisited cities are found, may be returning to the depot
            next_city = 0
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
        if current == 0:  # If returned to the depot, stop
            break

    # Calculate total cost
    total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")