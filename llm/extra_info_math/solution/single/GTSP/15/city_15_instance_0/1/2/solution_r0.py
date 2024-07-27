import pulp
import math

# City locations
locations = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Group definitions
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {}
for i in locations:
    distances[i] = {}
    for j in locations:
        if i != j:
            distances[i][j] = euclidean_distance(locations[i], locations[j])

# PuLP model
model = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in locations for j in locations if i != j), cat='Binary')

# Objective function: Minimize total distance
model += pulp.lpSum(distances[i][j] * x[i, j] for i in locations for j in locations if i != j)

# Constraints to ensure exactly one node from each group visits another group
for grp_id, members in groups.items():
    model += pulp.lpSum(x[i, j] for j in locations for i in members if i != j) == 1
    model += pulp.lpSum(x[i, j] for i in locations for j in members if i != j) == 1

# Flow conservation constraints
for k in locations:
    model += (pulp.lpSum(x[i, k] for i in locations if i != k) 
            - pulp.lpSum(x[k, j] for j in locations if j != k)) == 0

# Subtour prevention (MTZ constraints)
n = len(locations)
u = pulp.LpVariable.dicts("u", (i for i in locations if i > 0), lowBound=0, cat='Integer')
for i in locations:
    for j in locations:
        if i != j and i > 0 and j > 0:
            model += u[i] - u[j] + (n-1) * x[i, j] <= n - 2

# Solve the problem
model.solve()

# Extracting the solution
tour = [0]
cost = 0
visited = set()
current = 0
while True:
    next_city = None
    for j in locations:
        if j != current and pulp.value(x[current, j]) == 1:
            next_city = j
            cost += distances[current][j]
            tour.append(j)
            break
    if next_city == 0:
        break
    current = next_city

# Adding back to depot
tour.append(0)
cost += distances[current][0]

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")