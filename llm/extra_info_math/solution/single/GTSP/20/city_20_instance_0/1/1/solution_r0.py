import math
import pulp

# City coordinates
coordinates = [
    (8, 11),  # Depot
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculating Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Creating a model
model = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables: x_ij = {0, 1}
x = {}
for i in range(20):
    for j in range(20):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective function
model += pulp.lpSum(distance(coordinates[i], coordinates[j]) * x[(i, j)] for i in range(20) for j in range(20) if i != j)

# Constraints

# Visit each group exactly once
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in range(20) if j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in range(20) if j not in group) == 1

# Flow conservation 
for i in range(20):
    model += pulp.lpSum(x[(j, i)] for j in range(20) if j != i) - pulp.lpSum(x[(i, j)] for j in range(20) if j != i) == 0

# Solving the model
model.solve()

# Extract the tour from the solution
tour = []
visited = set()
current = 0
while True:
    tour.append(current)
    visited.add(current)
    found_next = False
    for j in range(20):
        if j not in visited and x[(current, j)].value() == 1:
            current = j
            found_next = True
            break
    if not found_next:
        break
        
# Return to depot
tour.append(0)

# Calculate the total travel cost
total_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)