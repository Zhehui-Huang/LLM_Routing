import cvxpy as cp
import numpy as np
import math

# Define the coordinates of the cities including the depot city
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Define the number of cities including the depot
n = len(coordinates)

# Euclidean distance calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Constructing cost matrix
cost_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i, j] = distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[i, j] = 0

# Initialization of decision variables
x = cp.Variable((n, n), boolean=True)

# Objective function: minimize the total travel cost
objective = cp.Minimize(cp.sum(cp.multiply(cost_matrix, x)))

# Constraints
constraints = []

# Ensuring every city is visited and left exactly once
for i in range(n):
    constraints.append(cp.sum(x[i, :]) == 1)
    constraints.append(cp.sum(x[:, i]) == 1)

# Subtour elimination constraints
u = cp.Variable(n, integer=True)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            constraints.append(u[i] - u[j] + n * x[i, j] <= n - 1)

# Problem definition and solving
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.CBC)

# Extracting the tour from the decision variables
tour = [0]
current_city = 0
while len(set(tour)) < n:
    next_city = np.argmax(x.value[current_city, :])
    tour.append(next_city)
    current_city = next_single

# Adding the depot city to complete the tour
tour.append(0)

# Calculating the total cost
total_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Displaying the results
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")