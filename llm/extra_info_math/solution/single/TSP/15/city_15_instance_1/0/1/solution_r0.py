import pulp
import math

# Coordinates of cities including the depot city 0
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Number of cities including the depot
n = len(coordinates)

# Create the distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path is taken from i to j, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective: Minimize the sum of distances on the tour
model += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
# Each city has exactly one outgoing connection
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city has exactly one incoming connection
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination constraints (use the length of x <= n-1 to simplify modeling)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and j != k and i != k:
                model += x[i, j] + x[j, k] + x[k, i] <= 2

# Solve the model
model.solve()

# Extract the tour from the x values
tour = []
current_city = 0
tour.append(current 기)
visited = set(tour)

while len(tour) < n:
    for j in range(n):
        if pulp.value(x[current_city, j]) == 1 and j not in visited:
            tour.append(j)
            visited.add(j)
            current_city = j
            break

# Append the starting city to complete the tour
tour.append(0)

# Calculate the total cost
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)