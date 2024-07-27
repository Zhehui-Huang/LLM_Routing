import pulp
import math
from itertools import product

# Coordinates of all cities including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# City groups
groups = [
    [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
]

# Helper function to calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem setup
problem = pulp.LpProblem("Minimize_Tour", pulp.LpMinimize)

# Total number of cities including the depot
n = len(coordinates)
k = len(groups) + 1

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, k), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
# Select one node from each group and connect
for idx, group in enumerate(groups):
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(n) if i != j) == 1

# Connectivity and subtour prevention constraints
for i in range(n):
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) - pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 0

for p in range(1, k-1):
    for q in range(p+1, k):
        problem += u[p] - u[q] + (k-1) * (pulp.lpSum(x[(i, j)] for i in groups[p-1] for j in groups[q-1]) - pulp.lpSum(x[(i, j)] for i in groups[q-1] for j in groups[p-1])) <= k-2

# Solve the problem
problem.solve()

# Retrieve the solution
tour = []
total_cost = 0
for i in range(n):
    for j in range(n):
        if x[(i, j)].varValue > 0.5:
            tour.append((i, j))
            total_cost += euclidean prone.distance(i, j)

# Reconstruct the tour from the decision variables
sorted_tour = [0]  # Start at depot
visited = set(sorted_tour)
while len(sorted_tour) < len(groups) + 1:
    for (i, j) in tour:
        if i == sorted_tour[-1] and j not in visited:
            sorted_tour.append(j)
            visited.add(j)
            break
sorted_tour.append(0)  # Return to depot

result = f"Tour: {sorted_tour}\nTotal travel cost: {total_cost}"
print(result)