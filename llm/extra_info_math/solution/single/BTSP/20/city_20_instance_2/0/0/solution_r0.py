import math
from pulp import *

# Given city coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Number of cities
n = len(coordinates)

# Calculating the distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem using PuLP
problem = LpProblem("MinimaxConsecutiveDistance", LpMinimize)

# Create decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Create variable for the maximum distance in route
z = LpVariable("z", lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum distance traveled between consecutive cities
problem += z

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city i
    problem += lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city i

# Constraint that x_{ij} = 0 if i = j
for i in range(n):
    x[i, i].setInitialValue(0)

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i][j] <= z

# Subtour elimination using Miller-Tucker-Zemlin (MTZ) formulation or a similar subtour elimination technique
u = LpVariable.dicts("u", range(n), 1, n, LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
problem.solve()

# Extract the tour from the solution
tour = []
visited = set()
current = 0
while True:
    tour.append(current)
    visited.add(current)
    next_city = None
    for j in range(n):
        if x[current, j].varValue == 1:
            next_city = j
            break
    if next_city == 0:
        break
    current = next_city

tour.append(0)  # complete the tour by returning to the depot

# Calculate the objective values
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")