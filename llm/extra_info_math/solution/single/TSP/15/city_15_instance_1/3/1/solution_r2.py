import pulp
import math
import itertools

# Coordinates of the cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Calculating Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
n = len(coordinates)
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# TSP Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
model += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints (using Miller Tucker Zemlin formulation)
u = pulp.LpVariable.dicts('u', (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the model
model.solve()

# Extracting the solution
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Organize tour in order starting from the depot
resolved_tour = [0]
while len(resolved_tour) < n:
    last = resolved_tour[-1]
    for (i, j) in tour:
        if i == last:
            resolved_tour.append(j)
            break

# Append depot to complete the tour
resolved_tour.append(0)

# Calculate the total cost
total_cost = sum(cost[resolved_tour[i]][resolved_tour[i + 1]] for i in range(len(resolved_tour) - 1))

# Output the results
print("Tour:", resolved_tour)
print("Total travel cost:", total_cost)