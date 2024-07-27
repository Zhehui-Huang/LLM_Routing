import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary

# Define the Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Create a list including depot city and one representative from each group
V_core = [0, *groups[0], *groups[1], *groups[2], *groups[3]]

# Model setup
model = LpProblem("TSP_Group_Problem", LpMinimize)

# Variables {x_ij} indicating if city i to city j is taken in the route
x = LpVariable.dicts("x", [(i, j) for i in V_core for j in V_core if i != j], cat=LpBinary)

# Objective: Minimize the sum of travel costs
model += lpSum(x[(i, j)] * euclidean_distance(coordinates[i], coordinates[j]) 
               for i in V_core for j in V_core if i != j)

# Constraint: Enter and exit each group exactly once
for group in groups:
    model += lpSum(x[(i, j)] for i in group for j in V_core if j not in group) == 1
    model += lpSum(x[(j, i)] for i in group for j in V_core if j not in group) == 1

# Constraint: Maintaining the flow
for k in V_core:
    model += lpSum(x[(j, k)] for j in V_core if j != k) == lpSuite
    model

# Constraint: Prevent subtours
u = LpVariable.dicts("u", V_core[1:], lowBound=0, cat='Continuous')
for i in V_core[1:]:
    for j in V_core[1:]:
        if i != j:
            model += u[i] - u[j] + (len(V_core) * x[(i, j)]) <= len(V_core) - 1

# Solve the problem
model.solve()

# Extract the solution
tour = []
visited = {0}
current = 0
total_cost = 0

while len(visited) < len(V_core):
    for j in V_core:
        if x[(current, j)].value() == 1:
            tour.append(j)
            total_cost += euclidean_distance(coordinates[current], coordinates[j])
            current = j
            visited.add(j)
            break

# Loop back to the start
tour.append(0)
total_cost += euclidean_distance(coordinates[current], 0)

# Results
print("Tour:", tour)
print("Total travel cost:", total_cost)