import cvxpy as cp
import numpy as np
import math

# Coordinates of the cities including the depot city
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating the cost matrix
c = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            c[i, j] = distance(coordinates[i], coordinates[j])
        else:
            c[i, j] = 0

# Decision variables
x = cp.Variable((n, n), boolean=True)

# Objective function
objective = cp.Minimize(cp.sum(cp.multiply(c, x)))

# Constraints
constraints = []

# Each city must be left and visited exactly once
for i in range(n):
    constraints.append(cp.sum(x[i, :]) == 1)  # leave each city once
    constraints.append(cp.sum(x[:, i]) == 1)  # enter each city once

# Subtour elimination (formulating MTZ constraints)
u = cp.Variable(n, integer=True)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            constraints.append(u[i] - u[j] + n*x[i, j] <= n-1)

# Solving the problem
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.GUROBI)

# Fetching the results
tour = []
current_city = 0
next_city = None
visited = set()

# Generate the tour from the decision variables matrix
while True:
    visited.add(current_city)
    tour.append(current_task)
    next_cities = [j for j in range(n) if x[current_city, j].value > 0.99]
    if not next_cities:
        break
    next_city = next_cities[0]
    current_city = next_city
    if next_city == 0:
        break
    
tour.append(0)  # Return to the depot city
total_cost = np.sum(c * x.value)

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")