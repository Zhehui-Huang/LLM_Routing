import pulp
from itertools import product
from math import sqrt

# Helper to calculate Euclidean distance
def distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Data from description
coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

groups = [
    [0, 5, 6, 7, 11, 17],
    [0, 1, 4, 8, 13, 16],
    [0, 2, 10, 15, 18, 19],
    [0, 3, 9, 12, 14]
]

# All cities indices
all_cities = set(range(len(coords)))

# Problem setup
model = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j], cat='Binary')

# Objective
model += pulp.lpSum(distance(coords[i], coords[j]) * x[(i, j)] for i in all_cities for j in all_cities if i != j)

# Constraints
# Visit each group exactly once
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in all_cities if i != j and j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in all_cities if i != j and j not in group) == 1

# Ensure tour is connected and returns to the start
for k in all_cities:
    model += pulp.lpSum(x[(k, j)] for j in all_cities if j != k) == 1
    model += pulp.lpSum(x[(j, k)] for j in all_cities if j != k) == 1

# Solve the model
model.solve()

# Extract the solution
tour = []
current_node = 0
for _ in range(len(coords)):
    for j in all_cities:
        if j != current_node and pulp.value(x[(current_node, j)]) == 1:
            tour.append(current_node)
            current_node = j
            break
tour.append(0)  # To complete the cycle

# Calculate the total distance
total_distance = sum(distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour)-1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_distance)