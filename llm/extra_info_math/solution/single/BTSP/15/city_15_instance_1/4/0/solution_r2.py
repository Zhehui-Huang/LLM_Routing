import pulp
import math

# Indexed coordinates of cities including the depot
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

n = len(cities)  # number of cities

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create problem
problem = pulp.LpProblem("MinimizeMaxDistanceTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), lowBound=0, upBound=1, cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Objective
problem += z

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[(i, j)] * euclidean_distance(cities[i], cities[j]) <= z

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Solve the problem
problem.solve()

# Extract the tour
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Sort the tour starting from depot
sorted_tour = [0]
current_city = 0
while len(sorted_tour) < n:
    for (i, j) in tour:
        if i == current_city:
            sorted_tour.append(j)
            current_city = j
            break

# Add return to the start
sorted_tour.append(0)

# Calculate the objective metrics
max_distance = max(euclidean_distance(cities[sorted_tour[i]], cities[sorted_tour[i+1]]) for i in range(len(sorted_tour)-1))
total_cost = sum(euclidean_distance(cities[sorted_tour[i]], cities[sorted_tour[i+1]]) for i in range(len(sorted_tour)-1))

# Results output
print("Tour:", sorted_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)