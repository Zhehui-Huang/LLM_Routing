from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary, value, PULP_CBC_CMD
import math

# Coordinates of the cities including the depot city 0
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

n = len(coordinates)

# Problem
problem = LpProblem("Minimax_Consecutive_City_Distance", LpMinimize)

# Variables: x_ij (1 if travel from city i to city j, 0 otherwise)
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=LpBinary)

# Maximum distance variable
d_max = LpVariable("d_max", lowBound=0)

# Objective function
problem += d_max

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance(i, j) <= d_max

# Avoid subtours
for s in range(2, n):
    for subset in combinations(range(1, n), s):
        problem += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve
problem.solve(PULP_CBC_CMD(msg=0))

# Extracting the route
route = []
visited = [False]*n
current = 0
route.append(current)
visited[current] = True

while True:
    next_city = next(j for j in range(n) if x[current, j].value() == 1 and not visited[j])
    route.append(next_city)
    visited[next_city] = True
    current = next_city
    if next_city == 0:
        break

# Calculating results
total_distance = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))
max_distance = max(distance(route[i], route[i+1]) for i in range(len(route) - 1))

print(f"Tour: {route}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")