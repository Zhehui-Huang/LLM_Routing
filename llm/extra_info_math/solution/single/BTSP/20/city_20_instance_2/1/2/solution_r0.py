from pulp import *
import math

# Coordinates of the cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

n = len(coordinates)

# Calculate Euclidean distance between cities
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create problem instance
prob = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n)], cat='Binary')
d = LpVariable("d", lowBound=0)

# Objective
prob += d

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * dist(coordinates[i], coordinates[j]) <= d

# Subtour elimination constraint
for m in range(2, n):
    for S in combinations(range(1, n), m):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
total_distance = 0
max_distance = 0
visited = [False] * n
while True:
    visited[current] = True
    tour.append(current)
    for j in range(n):
        if x[current, j].varValue == 1:
            total_distance += dist(coordinates[current], coordinates[j])
            max_distance = max(max[]={current_distance)
            current = j
            break
    if current == 0:
        break

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)