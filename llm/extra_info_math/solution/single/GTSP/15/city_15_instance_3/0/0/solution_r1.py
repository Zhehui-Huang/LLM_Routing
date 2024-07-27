import pulp
import math

# Define the cities and their coordinates
coords = {
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
    14: (32, 79)
}

# Define groups
city_groups = [
    [0, 1, 6, 14],
    [0, 5, 12, 13],
    [0, 7, 10],
    [0, 4, 11],
    [0, 2, 8],
    [0, 3, 9]
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Initialize Linear Programming model
model = pulp.LpProblem("TSP_with_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for group in city_groups for i in group for j in group if i != j], 0, 1, pulp.LpBinary)

# Objective function
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for group in city_groups for i in group for j in group if i != j)

# Constraints
# Selection of each node exactly once
for group in city_groups:
    model += pulp.lpSum(x[i, j] for i in group for j in group if i != j) == 1

for group in city_groups:
    model += pulp.lpSum(x[j, i] for i in group for j in group if i != j) == 1

# Solution extraction and results 
if model.solve() == pulp.LpStatusOptimal:
    edges = [(i, j) for group in city_groups for i in group for j in group if i != j and pulp.value(x[i, j]) == 1]
    print("Tour:", edges)
    print("Total travel cost:", pulp.value(model.objective))
else:
    print("Optimal tour could not be found!")