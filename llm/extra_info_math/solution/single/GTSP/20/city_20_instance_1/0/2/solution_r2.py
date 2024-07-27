import pulp
import math

# Cities coordinates
coordinates = {
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

# Groups
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# ALL CITIES including depot
V = [0] + [city for sublist in groups.values() for city in sublist]

# Problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in V for j in V if i != j}

# Objective: Minimize travel cost
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in V for j in V if i != j)

# Constraint: Exactly one outgoing from each group and from depot to one of the cities in a group
for k, group in groups.items():
    prob += pulp.lpSum(x[0, j] for j in group) == 1  # From depot to one in each group
    prob += pulp.lpSum(x[j, 0] for j in group) == 1  # From group to depot
    prob += pulp.lpSum(x[i, j] for i in group for j in V if j not in group) == 1  # From each group to all others not in group

# Constraint: Enter and leave each city exactly once, besides depot, entered and left only by visiting group members
for j in [c for c in V if c != 0]:
    prob += pulp.lpSum(x[i, j] for i in V if i != j) == 1
    prob += pulp.lpSum(x[j, i] for i in V if i != j) == 1

# Solve
prob.solve()

# Get output route and cost
tour = [0]
current = 0
total_cost = 0.0

for _ in range(len(V)):
    next = [j for j in V if j != current and pulp.value(x[current, j]) == 1]
    if not next:
        break
    next_city = next[0]
    total_cost += distance(current, next_city)
    current = next_city
    tour.append(next_city)
    if next_city == 0:
        break

total_cost += distance(tour[-1], 0)
tour.append(0)  # ensure return to depot

print("Tour:", tour)
print("Total travel cost:", total_cost)