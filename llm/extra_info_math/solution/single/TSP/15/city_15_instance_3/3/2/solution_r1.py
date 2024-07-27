import pulp
import math
from itertools import combinations

# City coordinates (indexing from 0, where city 0 is the depot)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Number of cities including depot
n = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n)], cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)), "Total Distance"

# Constraints
# Each city must be entered and left exactly once
for k in range(n):
    prob += pulp.lpSum(x[k, j] for j in range(n) if j != k) == 1, f"Enter_{k}"
    prob += pulp.lpSum(x[i, k] for i in range(n) if i != k) == 1, f"Leave_{k}"

# Subtour elimination constraints using MTZ formulation
# Additional variables for subtour elimination (u) from 0 to n-1
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i,j] <= n-1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
visited = [False] * n
current = 0
count = 0

while not visited[current] and count < n:
    visited[current] = True
    tour.append(current)
    next_city = [j for j in range(n) if pulp.value(x[current, j]) == 1 and not visited[j]]
    if not next_city:
        break
    current = next_city[0]
    count += 1

tour.append(0)  # Back to depot

# Calculate the total travel cost
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Print output as required
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))