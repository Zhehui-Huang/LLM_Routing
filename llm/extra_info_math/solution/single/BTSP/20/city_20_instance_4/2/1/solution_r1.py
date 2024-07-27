import math
from itertools import combinations
from mip import Model, xsum, minimize, BINARY

# City coordinates indexed from 0 to 19
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

n = len(coordinates)  # Number of cities including the depot (20)

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distances matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
d = model.add_var()

# Objective: minimize the maximum distance used in a route
model.objective = minimize(d)

# Constraints

# Ensure each city is entered and left once
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination (Miller-Tucker-Zemlin formulation)
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1)*x[i][j] <= n-2

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i][j] * distances[i][j] <= d

# Solve the problem
model.optimize()

# Extract the solution
tour = []
current = 0
visited = [False]*n
for _ in range(n):
    next_city = [j for j in range(n) if x[current][j].x > 0.9 and not visited[j]]
    if next_city:
        next_city = next_city[0]
        visited[next_city] = True
        tour.append(next_city)
        current = next_city

# Append the depot (starting city) to complete the tour
tour.insert(0, 0)
tour.append(0)

# Calculate the total cost and the maximum consecutive distance
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the tour, total travel cost, and maximum distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")