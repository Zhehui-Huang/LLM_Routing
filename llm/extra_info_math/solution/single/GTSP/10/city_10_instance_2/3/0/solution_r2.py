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

n = len(positions)
k = len(city_groups)

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
dist = [[euclidean_distance(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Create a MIP model
model = Model()

# Binary variables indicating whether to travel from city i to city j
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# Objective function: Minimize the total distance
model.objective = minimize(xsum(dist[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j))

# Constraints ensuring one departure and arrival for each node
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Picking exactly one city from each group
for group in city_groups:
    model += xsum(x[i][j] for i in group for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) for i in group if i != j) == 1

# Eliminating subtours
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Solving the model
model.optimize()

# Extract the tour from the model solution
tour = [0]
for _ in range(n-1):
    next_city = next(j for j in range(n) if x[tour[-1]][j].x >= 0.99)
    if next_city == 0:
        break
    tour.append(next_city)
tour.append(0)

# Calculate the total travel distance
total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)