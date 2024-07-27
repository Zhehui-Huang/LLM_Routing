import pulp as pl
import math

# City coordinates
coords = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Grouping information
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to compute Euclidean distance
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Set of cities and groups
V = list(coords.keys())
k = len(groups)

# Full connectivity between selected nodes
A = [(i, j) for i in V for j in V if i != j]

# Integer Programming Model
model = pl.LpProblem("TSP_Groups", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts('x', A, cat='Binary')
u = pl.LpVariable.dicts('u', range(2, k+1), lowBound=0, cat='Continuous')

# Objective - Minimize the cost of the tour
model += pl.lpSum(x[i, j] * distance(i, j) for i, j in A)

# Constraints
# Sub-tour constraints
for p in range(k):
    model += pl.lpSum(x[i, j] for i in groups[p] for j in V if j not in groups[p]) == 1
    model += pl.lpSum(x[j, i] for i in groups[p] for j in V if j not in groups[p]) == 1
    
# Flow conservation
for i in V:
    model += pl.lpSum(x[j, i] for j in V if (j, i) in x) == pl.lpSum(x[i, j] for j in V if (i, j) in x)
    
# Sub-tour elimination
for p in range(2, k+1):
    for q in range(2, k+1):
        if p != q:
            model += u[p] - u[q] + k * pl.lpSum(x[i, j] for i in groups[p-1] for j in groups[q-1]) + (
                k-2) * pl.lpSum(x[j, i] for j in groups[q-1] for i in groups[p-1]) <= k-1

# Solve the problem
model.solve()

# Outputting the results
tour = []
visited = {0}
current = 0
tour.append(current)

while True:
    found = False
    for j in V:
        if x[current, j].varValue > 0.5 and j not in visited:
            tour.append(j)
            visited.add(j)
            current = j
            found = True
            break
    if not found:
        break

tour.append(0)  # Complete the tour back to the depot

# Calculate the total cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)