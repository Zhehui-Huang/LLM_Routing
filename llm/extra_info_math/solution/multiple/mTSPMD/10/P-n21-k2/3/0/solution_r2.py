import numpy as np
import pulp

# Define all the city coordinates including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute Euclidean distance matrix
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initiate LP model
model = pulp.LpProblem("Minimize_Total_Distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
model += pulp.lpSum(x[i, j, k] * distance_matrix[i][j] for i in range(n) for j in range(n) for k in range(2) if i != j), "Total Travel Cost"

# Constraints
# Each city is visited exactly once by exactly one robot
for j in range(2, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(2) if i != j) == 1

# Each robot departs from and returns to its starting depot
for k in range(2):
    model += pulp.lpSum(x[k, j, k] for j in range(n) if j != k) == 1
    model += pulp.lpSum(x[j, k, k] for j in range(n) if j != k) == 1

# Subtour elimination constraints
for k in range(2):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                model += u[i] - u[j] + (n+1) * x[i, j, k] <= n

# Solve the problem using the available solver
solver = pulp.PULP_CBC_CMD(msg=0)
model.solve(solver)

# Extract the solution
tours = {0: [], 1: []}
for k in range(2):
    start = k
    next_city = start
    while True:
        tours[k].append(next_city)
        next_city = next(j for j in range(n) if j != next_city and pulp.value(x[next_city, j, k]) == 1)
        if next_city == start:
            tours[k].append(next_city)
            break

# Print the tours and their total cost
total_cost = 0
for k in range(2):
    tour_cost = sum(distance_matrix[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")