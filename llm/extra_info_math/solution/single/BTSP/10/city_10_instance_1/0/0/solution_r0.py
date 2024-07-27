import math
from pulp import *

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the coordinates of the cities
cities_coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80), 
    (18, 63), (54, 91), (70, 14), (97, 44), 
    (17, 69), (95, 89)
]

n = len(cities_coordinates)

# Calculate distances between all pairs of cities
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Define the problem
prob = LpProblem("Min-Max_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", distances, 0, 1, LpBinary)
max_link = LpVariable("max_link", 0)

# Objective function
prob += max_link

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if (i, j) in x) == 1  # Leave each city only once
    prob += lpSum(x[(j, i)] for j in range(n) if (j, i) in x) == 1  # Enter each city only once

# Maximum link constraint
for (i, j) in distances:
    prob += distances[(i, j)] * x[(i, j)] <= max_link

# Subtour elimination constraints (using lifted Miller-Tucker-Zemlin formulation)
u = LpVariable.dicts("u", range(n), 0, n-1, LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[(i, j)] <= n-1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
for v in prob.variables():
    if v.varValue == 1 and v.name.startswith('x'):
        _, frm, to = v.name.split('_')
        tour.append((int(frm), int(to)))

# Determine tour order
next_city = 0
ordered_tour = [0]
while len(ordered_tour) < n:
    for (frm, to) in tour:
        if frm == next_city:
            ordered_tour.append(to)
            next_city = to
            break

# Complete the tour to the depot
ordered_tour.append(0)

# Calculate cost details
total_cost = sum(distances[(ordered_tour[i], ordered_tour[i + 1])] for i in range(len(ordered_tour)-1))
max_distance = max(distances[(ordered_tour[i], ordered_tour[i + 1])] for i in range(len(ordered_tour)-1))

# Output results
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)