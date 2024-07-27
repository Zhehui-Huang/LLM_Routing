from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
from math import sqrt

# Define the city coordinates
coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 
    3: (53, 40), 4: (54, 42), 5: (36, 30), 
    6: (52, 82), 7: (93, 44), 8: (21, 78), 
    9: (68, 14), 10: (51, 28), 11: (44, 79), 
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Define the city groups
groups = [
    [0, 8, 12, 14],  # Group with depot included for start and end point
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate distances
def distance(city1, city2):
    cx1, cy1 = coords[city1]
    cx2, cy2 = coords[city2]
    return sqrt((cx2 - cx1)**2 + (cy2 - cy1)**2)

# Optimization Problem Setup
problem = LpProblem("ShortestTour", LpMinimize)

# Decision Variables
x = {(i, j): LpVariable(f"x_{i}_{j}", cat="Binary") for i in coords for j in coords if i != j}

# Objective Function
problem += lpSum(x[i, j] * distance(i, j) for i in coords for j in coords if i != j)

# Constraints
# Exactly one city from each group participates in the tour
for group in groups:
    problem += lpSum(x[0, j] for j in group if 0 != j) == 1  # From depot
    problem += lpSum(x[j, 0] for j in group if 0 != j) == 1  # To depot

# Each group must have exactly one outgoing edge to a node outside the cluster and one coming back.
for group in groups:
    for j in group:
        if j != 0:
            problem += lpSum(x[j, k] for k in coords if k not in group and k != j) == 1
            problem += lpSum(x[k, j] for k in coords if k not in group and k != j) == 1

# Flow Conservation
for j in coords:
    problem += lpSum(x[i, j] for i in coords if i != j) == lpSum(x[j, k] for k in coords if k != j)

# Solve
problem.solve(PULP_CBC_CMD(msg=False))

# Extract solution
tour = [0]
current = 0
total_distance = 0
visited = set([0])

while True:
    next_city = None
    for j in coords:
        if j != current and x[current, j].value() == 1 and j not in visited:
            next_city = j
            break
    if next
_city is None:
        break
    tour.append(next_city)
    visited.add(next_city)
    total_distance += distance(current, next_city)
    current = next_city

# Closing loop to depot
tour.append(0)
total_distance += distance(current, 0)

# Display the outputs
print("Tour:", tour)
print(f"Total travel cost: {total_distance:.2f}")