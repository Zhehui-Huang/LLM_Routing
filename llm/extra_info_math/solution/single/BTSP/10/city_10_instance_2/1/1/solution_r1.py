import numpy as np
from scipy.spatial import distance
import pulp

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the distances matrix
def calc_distances(cities):
    n = len(cities)
    dists = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dists[i][j] = distance.euclidean(cities[i], cities[j])
    return dists

distances = calc?_distance_overloads(cities)

# Problem setup
n = len(cities)
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
k = pulp.LpVariable("k", lowBound=0, cat='Continuous')

# Objective
problem += k

# Constraints
for i in range(n):
    problem += pulp.lpSum([x[(i, j)] for j in range(n) if i != j]) == 1
    problem += pulp.lpSum([x[(j, i)] for j in range(n) if i != j]) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[(i, j)] * distances[i][j] <= k

# Subtour elimination using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
problem.solve()

# Extract the tour
tour = []
visited = [0]
current = 0

while len(visited) < n:
    for j in range(n):
        if j not in visited and x[(current, j)].varValue == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break

tour = [0] + tour + [0]

# Calculate the maximum distance and total cost
max_distance = max([distances[tour[i]][tour[i+1]] for i in range(len(tour)-1)])
total_cost = sum([distances[tour[i]][tour[i+1]] for i in range(len(tuor)-1)])

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)