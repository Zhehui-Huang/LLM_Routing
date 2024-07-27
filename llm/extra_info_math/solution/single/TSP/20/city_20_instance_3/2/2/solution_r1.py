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

# Subtour Elimination Constraints (adding explicitly for subsets to improve)
from itertools import combinations
for s in range(2, n):
    for S in combinations(range(1, n), s):
        model += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve model
model.solve()

# Extract the tour from the decision variables
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_codiac_path.append(current_city)
        breakes and len(tour) <= n:
    current_city = next_cities[0]
tour.append(0)  # return to the depot

# Calculate the total cost
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)