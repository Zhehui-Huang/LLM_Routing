import numpy as np
import cvxpy as cp
import itertools

# Coordinates of the cities including the depot city
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

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Matrix of distances
distances = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)])

# Decision variable for paths between cities
x = cp.Variable((n, n), boolean=True)

# Variable to minimize the maximum distance traveled between any two consecutive cities in the tour
z = cp.Variable()

# Constraints

# Each city must be entered and left exactly once
constraints = [
    cp.sum(x[i, :]) == 1 for i in range(n)
] + [
    cp.sum(x[:, i]) == 1 for i in range(n)
]

# Subtour elimination constraint
for S in range(2, n):
    for subset in itertools.combinations(range(n), S):
        constraints.append(cp.sum(x[subset, :][:, subset]) <= len(subset) - 1)

# Link max distance variable z to city distances under decision variables
constraints += [
    x[i, j] * distances[i, j] <= z
    for i in range(n) for j in range(n) if i != j
]

# Objective: Minimize the maximum distance between any two consecutive cities
objective = cp.Minimize(z)

# Problem formulation
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve(solver=cp.GLPK_MI)

# Obtain the tour by extracting the solution
tour = []
current_city = 0

for _ in range(n):
    next_city = np.where(np.isclose(x[current_city, :].value, 1))[0][0]
    tour.append(current_city)
    current_city = next_city

# Close the tour by returning to the depot
tour.append(0)

# Calculate the total travel cost and maximum distance traveled
total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
max_distance_cons = z.value

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance_cons)