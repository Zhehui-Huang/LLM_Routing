import pulp
import math

# Define city coordinates and groups
city_coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create the Problem
prob = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Generate variables
x = {}
u = {}
for i in city_coordinates:
    for j in city_coordinates:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# We also introduce rank variables to help eliminate subtours
for i in range(1, len(city_coordinates)):
    u[i] = pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous')

# Objective Function
prob += pulp.lpSum(distance(city_coordinates[i], city_coordinates[j]) * x[(i, j)] for i in city_coordinates for j in city_coordinates if i != j)

# Constraints

# We need to ensure exactly one visit to each group and no more
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in city_coordinates if j not in group) == 1
    prob += pulp.lpSum(x[(i, j)] for j in group for i in city_coordinates if i not in group) == 1

# Flow conservation for cities not in the depot
for i in city_coordinates:
    if i != 0:
        prob += pulp.lpSum(x[(j, i)] for j in city_coordinates if j != i) == pulp.lpSum(x[(i, j)] for j in city of_coordinates if j != i)

# Subtour elimination constraints
k = len(groups) + 1  # Number of groups + depot
for i in city_coordinates:
    for j in city_coordinates:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + k * x[(i, j)] <= k - 1

# Solve the problem
prob.solve()

# Collect results
route = []
visited = set()
current = 0
for _ in range(len(groups) + 1):
    for j in city_coordinates:
        if j != current and pulp.value(x[current, j]) == 1:
            route.append(current)
            visited.add(current)
            current = j
            break

# Adding depot city at the end
route.append(0)

# Calculate the total cost
total_cost = sum(distance(city_coordinates[route[i]], city_coordinates[route[i + 1]]) for i in range(len(route) - 1))

# Output the results
print("Tour:", route)
print("Total travel cost:", round(total_cost, 2))