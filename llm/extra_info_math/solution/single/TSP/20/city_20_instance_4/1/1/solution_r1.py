import numpy as np
import pulp

# Coordinates of the cities including the depot city
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate the Euclidean distance matrix
def calculate_distances(coords):
    num_cities = len(coords)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return distances

cost_matrix = calculate_distances(coordinates)

# Number of cities including the depot
n = len(coordinates)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("Traveling_Salesman_Problem", pulp.LpMinimize)

# Create variables: x_ij = 1 if traveled from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary', lowBound=0, upBound=1)

# Objective function - Minimize the total traveling cost
problem += pulp.lpSum(cost_matrix[i][j] * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum([x[(i, j)] for j in range(n) if i != j]) == 1 # leave each city once
    problem += pulp.lpSum([x[(j, i)] for j in range(n) if i != j]) == 1 # enter each city once

# Subtour elimination constraint using Miller-Tucker-Zemlin (MTZ)
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Solve the problem
problem.solve()

# Extract the tour from the variables
edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[(i, j)]) == 1]

# Reconstruct the path
tour = [0]
while len(tour) < n:
    for i, j in edges:
        if i == tour[-1]:
            tour.append(j)
            break

# Ensure returning to the depot
tour.append(0)

# Calculate total cost
total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")