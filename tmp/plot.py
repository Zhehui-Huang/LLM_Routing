from scipy.spatial.distance import pdist, squareform
from itertools import combinations
import numpy as np
import pulp

# Define places
places = {
    1: (9, 4),
    2: (4, 6),
    3: (4, 4),
    4: (3, 4),
    5: (4, 8),
}

# Calculate the distance matrix
locations = np.array(list(places.values()))
distance_matrix = squareform(pdist(locations, metric='euclidean'))

# Number of locations
n_locations = len(places)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n_locations) for j in range(n_locations) if i != j), cat='Binary')

# Objective
problem += pulp.lpSum(distance_matrix[i][j] * x[(i, j)] for i in range(n_locations) for j in range(n_locations) if i != j)

# Constraints
# Each place must be entered and left only once
for i in range(n_locations):
    problem += pulp.lpSum(x[(i, j)] for j in range(n_locations) if i != j) == 1
    problem += pulp.lpSum(x[(j, i)] for j in range(n_locations) if i != j) == 1

# Sub-tour elimination
u = pulp.LpVariable.dicts("u", range(n_locations), lowBound=0, upBound=n_locations-1, cat='Continuous')
for i, j in combinations(range(n_locations), 2):
    if i != 0 and j != 0:
        problem += u[i] - u[j] + n_locations*x[(i, j)] <= n_locations-1

# Solve the problem
problem.solve()

# Extract the solution
tour = []
visited = [0]
current = 0

while len(visited) < n_locations:
    next_visit = [j for j in range(n_locations) if x[(current, j)].varValue == 1 and j not in visited]
    if next_visit:
        visited.append(next_visit[0])
        tour.append((current, next_visit[0]))
        current = next_visit[0]

# Add return to start
tour.append((current, 0))

print(tour)