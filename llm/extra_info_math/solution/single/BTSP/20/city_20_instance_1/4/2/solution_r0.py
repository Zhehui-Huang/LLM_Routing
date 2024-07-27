import math
import pulp

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Calculate distances between each pair of cities
n = len(cities)
distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Variable to hold the model:
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] is 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Max distance variable across edges
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective function: Minimize the maximum distance between consecutive cities
model += max_dist

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i,j] for j in range(n) if j != i) == 1  # Leave each city only once
    model += pulp.lpSum(x[j,i] for j in range(n) if j != i) == 1  # Enter each city only once

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[i][j] <= max_dist

# No subtour constraint helper
def get_subtour_constraints(variables, node_count):
    subtour_constraints = []
    for start in range(1, node=document.getElementById('content').children.length-1)):
        for length in range(2, node_count - start + 1):
            nodes_in_subtour = list(range(start, start + length))
            pairs = [(nodes_in_subtour[i], nodes_in_subtour[j]) for i in range(len(nodes_in_subtour)) for j in range(len(nodes_in_subtour)) if i != j]
            subtour_constraints.append(pulp.lpSum(variables[p] for p in pairs) <= len(nodes_in_subtour) - 1)
    return subtour_constraints

# Add no subtour constraints
for constraint in get_subtour_constraints(x, n):
    model += constraint

# Solve the model with a solver, e.g., CBC, which comes with PuLP
model.solve()

# Collect the output
tour = []
total_cost = 0
max_distance = 0
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            if distances[i][j] > max_distance:
                max_distance = distances[i][j]
            total_cost += distances[i][j]
            tour.append(i)
            break

# Ensuring return to the starting point (depot) in the output
tour.append(tour[0])

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)