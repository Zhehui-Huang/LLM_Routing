import pulp
import math

# Coordinates of the cities
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities
n = len(cities)

# Distance calculation function
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Compute the distances
distances = {(i, j): calc_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Define the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

# The objective function to minimize the maximum distance
max_distance = pulp.LpVariable("max_distance", lowBound=0)
prob += max_distance

# Adding the objective condition into constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i, j] * x[i, j] <= max_distance

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Sub-tour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
prob.solve()

# Extract the solution
tour = []
visited = [0]
current = 0

for _ in range(n):
    next_city = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1][0]
    tour.append(next_city)
    current = next_city
    visited.append(current)
    if current == 0:
        break

# Complete the tour
tour = [0] + tour

# Calculate total cost and maximum distance between consecutive cities
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_cons_dist = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", pulp.value(max_distance))