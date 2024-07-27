import pulp as pl
import math

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

# Groups of cities, starting with the depot (included in all groups for modeling purposes)
groups = {
    0: [0, 5, 6, 7, 11, 17],
    1: [0, 1, 4, 8, 13, 16],
    2: [0, 2, 10, 15, 18, 19],
    3: [0, 3, 9, 12, 14]
}

# Euclidean distance calculation
def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cost matrix
cost = {(i, j): euclidean(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Model setup
model = pl.LpProblem("TSP", pl.LpMinimize)

# Variables: x_ij == 1 if path from i to j is chosen.
x = pl.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function
model += pl.lpSum(cost[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints

# Enter and leave each group exactly once
for group in groups.values():
    model += pl.lpSum(x[i, j] for i in group for j in cities if j not in group and (i, j) in x) == 1
    model += pl.lpSum(x[j, i] for i in group for j in cities if j not in group and (j, i) in x) == 1

# Flow conservation
for i in cities:
    model += pl.lpSum(x[j, i] for j in cities if j != i and (j, i) in x) == pl.lp
Sum(x[i, j] for j in cities if i != j and (i, j) in x)

# Solving the problem
model.solve()

# Retrieve solution
tour = []
if pl.LpStatus[model.status] == 'Optimal':
    active_edges = [(i, j) for i in cities for j in cities if i != j and pl.value(x[i, j]) == 1]
    visited = set()
    current = 0
    while active_edges:
        next_step = next((j for i, j in active_edges if i == current), None)
        tour.append(current)
        visited.add(current)
        current = next_step
        active_edges = [(i, j) for i, j in active_edges if i != current]
    tour.append(0) # return to depot

total_cost = sum(cost[i, j] for i, j in zip(tour[:-1], tour[1:]))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")