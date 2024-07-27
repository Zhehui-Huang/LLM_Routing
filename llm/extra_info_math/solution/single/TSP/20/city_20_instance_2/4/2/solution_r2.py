import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define dataset
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Helper function: Euclidean distance calculator
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Prepare distance (cost) matrix
n = len(coordinates)
cost_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] 
    for i in range(n)
]

# Define the model
model = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n)], cat=LpBinary)

# Objective
model += lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave i
    model += lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter i

# Subtour elimination constraints
for m in range(2, n):
    for S in combinations(range(1, n), m):
        model += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
model.solve()

# Extract solution and route
tour = []
current_city = 0
visited_cities = [False] * n
visited_cities[current_city] = True
tour.append(current_city)

while True:
    next_city = next((j for j in range(n) if x[current_city, j].value() == 1 and not visited_cities[j]), None)
    if next_city is None:
        break
    tour.append(next_city)
    visited_cities[next_city] = True
    current_city = next_city

# Closing the tour by returning to depot
tour.append(0)

# Calculate the total travel cost
total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")