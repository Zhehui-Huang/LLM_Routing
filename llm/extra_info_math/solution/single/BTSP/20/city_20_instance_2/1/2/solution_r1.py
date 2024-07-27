from pulp import *
import math
from itertools import combinations

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
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')
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

# Subtour elimination constraints
u = LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat="Continuous")
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
total_distances = []
visited = [False] * n
start = True

while not all(visited) or start:
    visited[current] = True
    tour.append(current)
    start = False
    next_cities = [(j, dist(coordinates[current], coordinates[j])) for j in range(n) if x[current, j].varValue == 1]
    if next_cities:
        next_city, dist_travel = next_cities[0]
        total_distances.append(dist_travel)
        current = next_city

# Add the return to the starting point distance
total_distances.append(dist(coordinates[tour[-1], tour[0]]))
tour.append(tour[0])  # To complete the loop back to the depot

# Output the solution
print("Tour:", tour)
print("Total travel cost:", sum(total_distances))
print("Maximum distance between consecutive slowly building cities:", max(total_distances))