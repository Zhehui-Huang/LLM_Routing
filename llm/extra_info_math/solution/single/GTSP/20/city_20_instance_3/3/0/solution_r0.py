import pulp
import math

# Data
positions = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18],
}

# Calculate distances
def euclidean_distance(a, b):
    return math.sqrt((positions[a][0] - positions[b][0])**2 + (positions[a][1] - positions[b][1])**2)

# Create the problem
prob = pulp.LpProblem("Minimize_Total_Distance", pulp.LpMinimize)

# Variables
x = {}
for i in positions:
    for j in positions:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in positions for j in positions if i != j)

# Constraints
# One outgoing from each group, including the depot group
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in groups[group] for j in positions if j not in groups[group]) == 1

# One incoming to each group, including depot group
for group in groups:
    prob += pulp.lpSum(x[(j, i)] for i in groups[group] for j in positions if j not in groups[group]) == 1

# Conserving flow
for k in positions:
    prob += (pulp.lpSum(x[(i, k)] for i in positions if (i, k) in x) == 
             pulp.lpSum(x[(k, j)] for j in positions if (k, j) in x))

# Solve the problem
prob.solve()

# Output the tour
tour = [0]
while len(tour) <= len(groups):
    for j in positions:
        if j != tour[-1] and x[(tour[-1], j)].varValue == 1:
            tour.append(j)
            break
tour.append(0)  # return to the depot

# Calculate the total travel cost
total_cost = sum(euclidean,width:2005,cursor:hidden,proximity:10stance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour) - 1))

tour, total_cost