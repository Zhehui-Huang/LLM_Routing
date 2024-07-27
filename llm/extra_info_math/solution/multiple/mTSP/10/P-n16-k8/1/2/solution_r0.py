from scipy.spatial import distance
import numpy as np
from mip import Model, xsum, minimize, BINARY

# Define the coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Parameters
n = len(coordinates)  # Total number of nodes including the depot
m = 8  # Number of robots

# Calculate the Euclidean distance matrix
c = [[distance.euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = Model()

# Decision variables
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]

# Objective function: Minimize the total travel cost
model.objective = minimize(xsum(c[i][j]*x[i][j][k] for i in range(n) for j in range(n) for k in range(m)))

# Constraints
# Each city is visited exactly once by a single robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Flow conservation for each robot
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n)) == xsum(x[j][i][k] for i in range(n))

# Each robot leaves the depot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            model += u[i] - u[j] + n * xsum(x[i][j][k] for k in range(m)) <= n - 1

# Solve model
model.optimize()

# Extract the tours for each robot and calculate costs
tours = [[] for _ in range(m)]
costs = [0.0 for _ in range(m)]

for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[i][j][k].x >= 0.99:  # Threshold to account for numerical issues
                if i == 0:
                    tours[k].append(0)
                tours[k].append(j)
                costs[k] += c[i][j]

# Add the depot as the final destination for each tour
for tour in tours:
    tour.append(0)
    
# Output tour and costs
total_cost = 0
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
    total_path = ' -> '.join(map(str, tours[k]))
    print(f"Path: {total_path}")
    total_cost += costs[k]

print(f"Overall Total Travel Fee: {total_cost}")