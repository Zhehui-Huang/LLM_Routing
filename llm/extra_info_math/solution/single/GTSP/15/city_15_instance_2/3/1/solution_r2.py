import pulp
import math

# Constants
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Euclidean distance function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Creating optimization model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], 0, 1, pulp.LpBinary)

# Minimize the travel cost
model += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j), "Objective"

# Select exactly one city from each group
for group in groups.values():
    model += sum(x[0, j] for j in group) == 1

# Ensure there's a return to the depot
for group in groups.values():
    model += sum(x[j, 0] for j in group) == 1

# Subtour constraints
for g in range(len(groups)):
    for i in groups[g]:
        model += sum(x[j, i] for j in cities if j != i) - sum(x[i, k] for k in cities if i != k) == 0

# Solve
model.solve()

# Output tour and total cost
tour = [0]
current_node = 0
while True:
    next_node = [j for j in cities if j != current_node and pulp.value(x[current_node, j]) == 1]
    if not next_node:
        break
    next_node = next_node[0]
    tour.append(next_node)
    current_node = next_node
    if current_node == 0:
        break

# Calculate total cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))