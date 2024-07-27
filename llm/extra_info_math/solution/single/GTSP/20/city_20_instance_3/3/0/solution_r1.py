import pulp
import math

# Define positions of cities
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
    19: (19, 72)
}

# Define groups of cities
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((positions[a][0] - positions[b][0])**2 + (positions[a][1] - positions[b][1])**2)

# Define the optimization problem
prob = pulp.LpProblem("Minimize_Total_Distance", pulp.LpMinimize)

# Variables for paths between cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in positions for j in positions if i != j), cat="Binary")

# Objective function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in positions for j in positions if i != j)

# Constraints
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in groups[group] for j in positions if j not in groups[group]) == 1
    prob += pulp.lpSum(x[(j, i)] for i in groups[group] for j in positions if j not in groups[group]) == 1

for k in positions:
    prob += pulp.lpSum(x[(i, k)] for i in positions if (i, k) in x) == pulp.lpSum(x[(k, j)] for j in positions if (k, j) in x)

# Solve the model
prob.solve()

# Extract tour
current_pos = 0
tour = [0]
while len(tour) < len(groups) + 1:
    next_city = [j for j in positions if j != current_pos and pulp.value(x[(current_pos, j)]) == 1]
    if next_city:
        next_city = next_city[0]
        tour.append(next_city)
        current_pos = next_city

# Append the start city to complete the tour
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")