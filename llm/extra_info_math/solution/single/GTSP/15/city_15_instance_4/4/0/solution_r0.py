from pulp import *
import math

# City coordinates
coords = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Function to calculate Euclidean distance
def dist(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Define the problem
prob = LpProblem("Minimize_Tour_Cost", LpMinimize)

V = list(coords.keys())
group_count = len(groups)
x = LpVariable.dicts("x", (V, V), 0, 1, LpBinary)
u = LpVariable.dicts("u", list(range(2, group_count+2)), lowBound=0)

# Objective function
prob += lpSum(x[i][j] * dist(i, j) for i in V for j in V if i != j), "Total_Travel_Cost"

# Constraints
# Each group must have exactly one outgoing and one incoming connection
for p, group in enumerate(groups, 1):
    prob += lpSum(x[i][j] for i in group for j in V if j not in group) == 1, f"Outgoing_from_group_{p}"
    prob += lpSum(x[j][i] for i in group for j in V if j not in group) == 1, f"Incoming_to_group_{p}"

# Flow conservation
for i in V:
    prob += lpSum(x[j][i] for j in V if j != i) == lpSum(x[i][j] for j in V if i != j), f"Flow_conservation_{i}"

# Subtour prevention
k = group_count + 1
for p in range(2, group_count + 2):
    for q in range(2, group_count + 2):
        if p != q:
            prob += u[p] - u[q] + k * lpSum(x[i][j] for i in groups[p-2] for j in groups[q-2]) + (k-2) * lpSum(x[i][j] for i in groups[q-2] for j in groups[p-2]) <= k-1, f"Subtour_{p}_{q}"

# Solve the problem
prob.solve()

# Extract the solution
tour = []
cost = 0

for v in V:
    for w in V:
        if x[v][w].varValue == 1:
            tour.append((v, w))
            cost += dist(v, w)

# Organize the tour starting from the depot
organized_tour = [0]
while len(organized_tour) < len(tour):
    last = organized_tour[-1]
    next_city = next(w for v, w in tour if v == last)
    organized_tour.append(next_city)

# Output
print("Tour:", organized_tour)
print("Total travel cost:", cost)