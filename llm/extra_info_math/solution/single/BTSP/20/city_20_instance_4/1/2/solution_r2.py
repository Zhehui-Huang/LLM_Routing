import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
import math

# Define the cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(cities)

# Calculate distances between each pair of nodes
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem
prob = LGoPProblem("Minimax_TSP", coerce_size="Minimize")

# Create variables
x = LpVariable.dicts("x", (range(n), range(n)), cat='Binary')
u = LpVariable.dicts("u", range(n), lowBound=0, upBound=n, cat='Integer')  # For subtour elimination

# Objective function
prob += lpSum(distances[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    # Arrival and departure constraint
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraint
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[i][j] <= n-1

# Solve the problem
prob.solve()

# Retrieve the tour from the solution
tour = [0]
for _ in range(n):
    next_city = [j for j in range(n) if x[tour[-1]][j].value() == 1][0]
    tour.append(next_city)
tour.append(0)  # end at the depot    

# Calculate the max distance and total cost
max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)