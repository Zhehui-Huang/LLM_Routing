import pulp
from math import sqrt

# Define the city coordinates and the groups
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
               (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
groups = [[0, 5, 6, 7], [0, 2, 3], [0, 1, 9], [0, 4, 8]]
num_groups = len(groups)

# Calculate Euclidean distances
def euclidean_distance(a, b):
    return sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Creating the LP problem
prob = pulp.LpProblem("MinimizeTourCost", pulp.LpMinimize)

# Variables: x_ij
x = {}
for group in groups:
    for i in group:
        for j in group:
            if i != j:
                x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, cat='Binary')

u = {i: pulp.LpVariable(f"u_{i}", 0, len(coordinates) - 1, cat='Integer') for i in range(len(coordinates))}

# Objective Function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for group in groups for i in group for j in group if i != j)

# Constraints
for gr in groups:
    cities = [c for c in gr if c != 0]
    prob += pulp.lpSum(x[(0, j)] for j in cities) == 1  # Exiting the depot to group
    prob += pulp.lpToEnd(x[(j, 0)] for j in cities) == 1  # Entering the depot from group

for group in groups:
    for i in group:
        if i != 0:
            prob += (sum(x[(j, i)] for j in group if j != i) == 1)  # One input per city
            prob += (sum(x[(i, j)] for j in group if j != i) == 1)  # One output per city

# Subtour elimination
for group in groups:
    for i in group:
        for j in group:
            if i != j and i != 0 and j != 0:
                prob += (u[i] - u[j] + (len(coordinates)-1)*x[(i, j)]) <= (len(coordinates)-2)

# Solve the problem
prob.solve()

# Retrieve the tour and calculate cost
tour = []
current = 0
prev = -1
n = len(coordinates)

while len(tour) < n:
    found = False
    for j in range(n):
        if j != current and pulp.value(x[current, j]) == 1:
            tour.append(j)
            prev, current = current, j
            found = True
            break
    if not found or prev == 0:
        break

# Correctly closing the loop
tour = [0] + tour

total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)