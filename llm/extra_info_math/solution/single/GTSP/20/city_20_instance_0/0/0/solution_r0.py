import pulp
from math import sqrt

# Define the city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# City groups:
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Integer programming setup using PuLP
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Define all cities set and the decisions variables for paths between cities
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
     for i in cities for j in cities if i != j}

# Objective Function
model += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j), "Total_Travel_Cost"

# Constraints

# Ensure each city group has exactly one exit and entry from and to the tour
for group in groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Ensure flow conservation - entering and leaving each city
for i in cities:
    model += (pulp.lpSum(x[j, i] for j in cities if j != i) ==
              pulp.lpSum(x[i, j] for j in cities if i != j))

# Subtour elimination constraints
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in cities if i != 0}

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))
if status == pulp.LpStatusOptimal:
    print("Model solved successfully.")
else:
    print("Solution is suboptimal or infeasible.")

# Extract the route
path = []
visited = set()
current_node = 0
while True:
    next_node = next(j for j in cities if pulp.value(x[current_node, j]) == 1 and j not in visited)
    path.append(next_node)
    current_node = next_node
    visited.add(current_node)
    if current_node == 0:
        break

# Calculate total distance
total_distance = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))

# Output results
print(f"Tour: {path}")
print(f"Total travel cost: {total_distance:.2f}")