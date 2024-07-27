import numpy as np
import pulp

# City coordinates (including the depot, index 0)
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(coordinates)

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

dist_matrix = np.zeros((n, n), dtype=float)
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Setting up the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}

# Objective Function
model += pulp.lpSum(dist_matrix[i][j] * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"Depart_from_{i}"
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"Arrive_at_{i}"

# Subtour Elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):
        model += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve()

# Extract the tour
tour = []
current_city = 0
remaining_cities = set(range(n))
remaining_cities.remove(0)

while remaining_cities:
    next_city = [j for j in range(n) if j != current_city and j in remaining_cities and pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

tour = [0] + tour + [0]

# Calculate the total travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")