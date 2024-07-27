import numpy as np
import cvxpy as cp

# Given coordinates
coordinates = np.array([
    [79, 15],  # Depot city 0
    [79, 55],
    [4, 80],
    [65, 26],
    [92, 9],
    [83, 61],
    [22, 21],
    [97, 70],
    [20, 99],
    [66, 62]
])

# Number of cities
n = coordinates.shape[0]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(p1, p2):
    return np.linalg.norm(p1 - p2)

distances = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)])

# Variables
x = cp.Variable((n, n), boolean=True)

# Maximum distance in the solution to be minimized
z = cp.Variable()

# Constraints
constraints = []

# Each city must be entered and left exactly once
for i in range(n):
    constraints.append(cp.sum(x[i, :]) == 1)
    constraints.append(cp.sum(x[:, i]) == 1)

# No subtours
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        constraints.append(cp.sum(x[np.ix_(subset, subset)]) <= len(subset) - 1)

# Link x and maximum distance z
constraints += [x[i, j] * distances[i, j] <= z for i in range(n) for j in range(n) if i != j]

# Objective function
objective = cp.Minimize(z)

# Problem
problem = cp.Problem(objective, constraints)

# Solve the problem using GLPK_MI solver
result = problem.solve(solver=cp.GLPK_MI)

# Extract the tour from solution 'x' variable
tour = []
visited = np.full(n, False)
current_city = 0

while True:
    visited[current_city] = True
    tour.append(current_city)
    next_city_candidates = np.where(np.round(x[current_city, :].value) == 1)[0]
    if next_city_candidates.size == 0:
        break
    current_city = next_city_candidates[0]

# For returning to the starting point
tour.append(0)

# Calculate total cost and maximum distance
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", result)