import pulp
import math

# Coordinates of depot and cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Number of cities (including the depot)
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
y = pulp.LpVariable("y", lowBound=0)

# Objective
problem += y

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination using the Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[i, j] <= n-1

# Min-max constraint to minimize the maximum distance traveled
for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[i][j]*x[i, j] <= y

# Solve problem
problem.solve()

# Extract tour
tour = []
current = 0
for _ in range(n):
    tour.append(current)
    for j in range(n):
        if pulp.value(x[current, j]) == 1:
            current = j
            break
tour.append(0)  # return to the depot

# Total cost and maximum distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(n))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(n))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)