import math
import mip

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 0),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

n = len(cities)  # Number of cities

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize model
model = mip.Model()

# Variables
x = [[model.add_var(var_type=mip.BINARY) for j in range(n)] for i in range(n)]
z = model.add_var()

# Objective
model.objective = mip.minimize(z)

# Constraints
# Each city must be left and arrived at exactly once
for i in range(n):
    model += mip.xsum(x[i][j] for j in range(n) if i != j) == 1
    model += mip.xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraints (Miller-Tucker-Zemlin (MTZ))
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n-1

# Max distance constraints
for i in range(n):
    for j in range(n):
        model += z >= distances[i][j] * x[i][j]

# Solving the model
model.optimize()

# Extracting the solution
tour = []
if model.num_solutions:
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))

# Reordering the tour according to the actual path
actual_tour = [0]
for _ in range(n-1):
    current = actual_tour[-1]
    for (i, j) in tour:
        if i == current:
            actual_tour.append(j)
            break
actual_tour.append(0)

# Calculating statistics
total_cost = sum(distances[actual_tour[i]][actual_tour[i+1]] for i in range(len(actual_tour) - 1))
max_distance = max(distances[actual_tour[i]][actual_tour[i+1]] for i in range(len(actual_tour) - 1))

print("Tour:", actual_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)