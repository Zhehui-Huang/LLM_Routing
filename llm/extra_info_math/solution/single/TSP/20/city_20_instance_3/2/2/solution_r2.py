import pulp
import math

# Coordinates of cities including the depot
coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coords)
distance_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Setup the Linear Programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city once
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city once

# Subtour Elimination Constraints
for size in range(2, n):
    for subset in combinations(range(1, n), size):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=0))

tour = []
current_city = 0
visited = [False] * n
visited[0] = True

# Extract the tour from the decision variables
for _ in range(n - 1):  # exclude the return to the starting point
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j])==1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(current_city)
    current_city = next_city
    visited[current_city] = True

tour.append(current_city)  # To include the last city
tour.append(0)             # To come back to the depot

# Calculate the total travel cost
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)