import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, PULP_CBC_CMD
from itertools import combinations

# Define city coordinates
cities = {
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
    14: (32, 79),
}

num_cities = len(cities)

# Distance calculation (Euclidean)
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distances matrix
dist = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Setup the problem
problem = LpProblem("Minimize_Max_Distance", LpMinimize)

# Setup variables
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], cat='Binary')
z = LpVariable("maximum_distance", lowBound=0, cat='Continuous')

# Objective function
problem += z

# Constraints
for i in range(num_cities):
    problem += lpSum([x[i, j] for j in range(num_cities) if i != j]) == 1
    problem += lpSum([x[j, i] for j in range(num_cities) if i != j]) == 1

# Maximum distance constraint
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            problem += x[i, j] * dist[i][j] <= z

# Subtour elimination constraints
for S in range(3, num_cities):
    for subset in combinations(range(num_cities), S):
        subset = list(subset)
        if 0 in subset:
            problem += lpSum([x[i, j] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Solve the problem
problem.solve(PULP_CBC_CMD(msg=False))

# Extract the solution
tour = []
current = 0
tour.append(current)
visited = set()
visited.add(current)

for _ in range(num_cities):
    for j in range(num_cities):
        if j not in visited and x[current, j].varValue == 1:
            tour.append(j)
            visited.add(j)
            current = j
            break

tour.append(0)  # returning to the depot

# Calculating total cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist_ij = dist[tour[i]][tour[i + 1]]
    total_cost += dist_ij
    if dist_ij > max_distance:
        max_distance = dist_ij

# Output the results
result = {
    "Tour": tour,
    "Total travel cost": round(total_cost, 2),
    "Maximum distance between consecutive cities": round(max_distance, 2)
}

print(result)