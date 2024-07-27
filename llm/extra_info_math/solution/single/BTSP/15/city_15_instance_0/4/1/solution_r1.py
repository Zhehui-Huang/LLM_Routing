import pulp
import math

# Define the cities' coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Number of cities (including the depot)
n = len(cities)

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create the linear programming problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if we travel from i to j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)

# Auxiliary variable for the maximum distance in the tour
z = pulp.LpVariable("z", lowBound=0)

# Objective function: Minimize the maximum distance traveled in any single trip
prob += z

# Constraints
# Each city must be left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# The maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * euclidean_distance(i, j) <= z

# Sub-tour Elimination
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n)*x[i, j] <= n-1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current_city = 0
for _ in range(n):
    next_city = next(j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1)
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate the total and maximum travel cost
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(tour[i], tour[i + 1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

output = {
    "Tour": [0] + tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(output)