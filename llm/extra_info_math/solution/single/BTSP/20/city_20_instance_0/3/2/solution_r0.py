import pulp
import math

# Define the cities' coordinates
coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

n = len(coordinates)  # Number of cities including the depot

# Calculate Euclidean distance between each pair of nodes
def euclidean(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Create the problem
problem = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
d = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum distance used in any step of the tour
problem += d

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1

# Distance constraint: if x[i][j] is used, its distance should not exceed the current maximum distance d
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * euclidean(i, j) <= d

# Subtour Elimination (implemented using the Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
problem.solve()

# Retrieve the solution
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Order the tour starting from depot city 0
organized_tour = [0]
current_city = 0
while len(organized_tour) < n:
    for i, j in tour:
        if i == current_city:
            organized_tour.append(j)
            current_city = j
            tour.remove((i, j))
            break

# Add the start city at the end to complete the tour
organized_tour.append(0)

# Calculate the total travel cost and maximum distance between consecutive cities
total_distance = 0
max_distance = 0
for i in range(len(organized_tour)-1):
    dist = euclidean(organized_tour[i], organized_tour[i+1])
    total_distance += dist
    if dist > max_distance:
        max_distance = dist

# Output
print("Tour:", organized_tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)