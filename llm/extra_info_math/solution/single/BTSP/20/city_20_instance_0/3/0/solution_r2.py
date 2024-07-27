from math import sqrt
import mip

# Define the coordinates of the cities including the depot
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities
n = len(cities)

# Distance calculation using Euclidean formula
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Pre-compute the distances between all pairs of cities
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize the optimization model
model = mip.Model()

# Binary variables indicating whether the path between cities i and j is chosen
x = [[model.add_var(var_type=mip.BINARY) for j in range(n)] for i in range(n)]

# Maximal distance between consecutive cities
max_dist = model.add_var()

# Objective Function: Minimize the maximal distance traveled between two consecutive cities
model.objective = mip.minimize(max_dist)

# Constraint: Each city must be entered and left exactly once
for i in range(n):
    model += mip.xsum(x[i][j] for j in range(n) if i != j) == 1
    model += mip.xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour Elimination Constraints
u = [model.add_var(lb=0, ub=n-1, var_type=mip.INTEGER) for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i][j] <= n - 1

# Connect max_dist with the distances for the tour
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[i][j] <= max_dist

# Solve the model
model.optimize()

# Extract the solution (tour path)
tour = [0]
current = 0
visited = set([0])

while True:
    for j in range(n):
        if x[current][j].x >= 0.99 and j not in visited:
            tour.append(j)
            visited.add(j)
            current = j
            break
    if current == 0:
        break

# Determine the total cost and the maximum segment distance in the tour
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {round(total}],
    // Euclid-ean istance calculation.
total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")