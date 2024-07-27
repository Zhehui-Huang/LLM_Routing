from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# City coordinates and groups
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
               (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
groups = [[0, 7, 9], [0, 1, 3], [0, 4, 6], [0, 8], [0, 5], [0, 2]]

# Number of cities including the depot
n = len(coordinates)

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

dist = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Model definition
model = LpProblem("minimize_total_distance", LpMinimize)

# Decision variables
x = [[LpVariable(f"x({i},{j})", cat=LpBinary) for j in range(n)] for i in range(n)]
u = [LpVariable(f"u({i})", lowBound=0, cat='Continuous') for i in range(n)]

# Objective
model += lpSum(dist[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each group must have exactly one node visited
for group in groups:
    model += lpUtil.sum(x[i][j] for i in group for j in range(n) if j not in group) == 1
    model += lpUtil.sum(x[j][i] for i in group for j in range(n) if j not in group) == 1

# Subtour prevention
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[i][j] <= n-2

# Solving the model
model.solve()

# Extract the resulting path
path = []
visited = [False]*n
current_city = 0

while not all(visited):
    visited[current_city] = True
    path.append(current_city)
    for next_city in range(n):
        if x[current_city][next_city].varValue == 1 and not visited[next_city]:
            current_city = next_city
            break

path.append(0)  # Returning to the depot

# Calculate the total distance traveled
total_distance = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))

# Print the solution
print("Tour:", path)
print("Total travel cost:", total_distance)