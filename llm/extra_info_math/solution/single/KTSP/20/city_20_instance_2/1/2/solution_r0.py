import pulp
from itertools import combinations
import math

# Coordinates of cities including the depot city at the first position
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities
n = len(coords)
# Number of cities to visit including the depot
k = 10
# Create a distance matrix
dist = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Creating a linear programming problem
model = pulp.LpProblem('k-TSP', pulp.LpMinimize)

# Define variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)),
                         cat=pulp.LpBinary)
y = pulp.LpVariable.dicts("y", (i for i in range(n)),
                         cat=pulp.LpBinary)

# Objective function to minimize total distance
model += pulp.lpSum(dist[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraint: k cities are visited exactly
model += pulp.lpSum(y) == k, "Visit_k_Cities"

# Constraints: start and end tour at the depot city
for i in range(1, n):
    model += x[0, i] <= y[i]
    model += x[i, 0] <= y[i]

# Degree constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 2 * y[i]

# Subtour elimination using Miller-Tucker-Zemlin (MTZ) constraints
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=k-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve the model
model.solve()

# Extracting the solution
tour = []
visited_cities = [i for i in range(n) if y[i].varValue == 1]

# Start creating the tour based on variable values
current_city = 0
tour.append(current_city)

for _ in range(k):
    next_city = next(j for j in visited_cities if x[current_city, j].varValue == 1)
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculating total travel cost
total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)