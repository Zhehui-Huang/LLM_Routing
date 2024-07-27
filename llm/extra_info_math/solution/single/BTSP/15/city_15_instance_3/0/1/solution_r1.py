import pulp
from math import sqrt

# Define the positions of the cities
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), 
          (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Number of cities
n = len(cities)

# Distance function using Euclidean distance
def distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the distance matrix
dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 
                          cat=pulp.LpBinary)

u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)

# Minimax Objective
L = pulp.LpVariable("L", lowBound=0)
prob += L

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1  # Leave node i
    prob += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1  # Enter node i

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += dist[i][j] * x[i, j] <= L

# Solve the problem
prob.solve()

# Output results
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Reorder the tour based on the decision variables
ordered_tour = []
current_location = 0
while len(ordered_tour) < n:
    for link in tour:
        if link[0] == current_location:
            ordered_tour.append(link[0])
            current_location = link[1]
            tour.remove(link)
            break
ordered_tour.append(0)  # End at the starting node

# Calculate total path cost and maximum segment length
total_cost = 0
max_distance = 0
for i in range(len(ordered_tour) - 1):
    segment_length = dist[ordered_tour[i]][ordered_tour[i + 1]]
    total_cost += segment_length
    if segment_length > max_distance:
        max_distance = segment_length

print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)