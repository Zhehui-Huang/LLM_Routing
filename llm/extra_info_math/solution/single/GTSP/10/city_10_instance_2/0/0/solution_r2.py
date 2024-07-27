import pulp as pl
import math

# City coordinates
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Constructing distance matrix
distance_matrix = {(i, j): euclidean_distance(coords[i], coords[j]) for i in coords for j in coords if i != j}

# Model
model = pl.LpProblem("TSP_Groups", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", distance_matrix, 0, 1, pl.LpBinary)
u = pl.LpVariable.dicts("u", list(range(2, len(groups)+2)), 0, None)

# Objective
model += pl.lpSum([distance_matrix[i, j] * x[(i, j)] for (i, j) in distance_matrix])

# Constraints for linking groups to the depot
for i in range(5):  # number of groups
    model += pl.lpSum(x[(0, j)] for j in groups[i]) == 1  # from depot to group
    model += pl.lpSum(x[(j, 0)] for j in groups[i]) == 1  # from group to depot

# Intra-group constraints
for k in groups:
    group = groups[k]
    if len(group) > 1:
        for i in group:
            model += pl.lpSum(x[(i, j)] for j in group if j != i) == 1

# Subtour avoidance between groups
for k1 in groups:
    for k2 in groups:
        if k1 != k2:
            group1 = groups[k1]
            group2 = groups[k2]
            model += pl.lpSum(x[(i, j)] for i in group1 for j in group2) == 1

# Solve model
model.solve()

# Extract the tour from the variables
tour = [0]
current_node = 0
for _ in range(len(groups) + 1):
    for j in range(len(coords)):
        if j != current_node and pl.value(x[(current_node, j)]) == 1:
            tour.append(j)
            current_node = j
            break
tour.append(0)  # adding the return to depot

# Calculate the total travel cost
total_cost = sum([distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)])

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)