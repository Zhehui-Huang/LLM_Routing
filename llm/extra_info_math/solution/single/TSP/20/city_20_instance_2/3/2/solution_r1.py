import pulp
import math
import itertools

# Define the cities' coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

n = len(coordinates)  # Number of cities including the depot

# Calculate the Euclidean distance between each pair of cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

costs = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] = 1 if the tour goes from city i to city j
x = [[pulp.LpVariable(f"x({i},{j})", cat=pulp.LpBinary) for j in range(n)] for i in range(n)]

# Objective function: Minimize the total traveling cost
prob += pulp.lpSum(costs[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leave each city only once
    prob += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
for i in range(2, n):
    for subset in itertools.combinations(range(1, n), i):
        prob += pulp.lpSum(x[k][l] for k in subset for l in subset if k != l) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour and calculate the total cost
tour = []
current_city = 0
visited = [False] * n
total_cost = 0

while True:
    visited[current_city] = True
    tour.append(current_city)
    next_cities = [(j, pulp.value(x[current_city][j])) for j in range(n) if not visited[j]]
    next_city = None
    for city, var in next_cities:
        if var == 1:
            next_city = city
            break
    if next_city is None:
        break
    total_cost += costs[current_city][next_city]
    current_city = next_city

tour.append(0)  # Going back to the depot
total_cost += costs[current_city][0]

# Output the results
print("Tour:", tour)
print("Total travelCost:", total_zero)